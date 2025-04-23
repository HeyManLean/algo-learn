# -*- coding: utf-8 -*-
import threading
import time
import redis


LUA_SCRIPT = """
local tokens_key = KEYS[1]
local last_time_key = KEYS[2]
local rate = tonumber(ARGV[1])
local capacity = tonumber(ARGV[2])

local now = tonumber(redis.call('TIME')[1])
local last_time = tonumber(redis.call('GET', last_time_key) or '0')
local tokens = capacity
if last_time > 0
then
    local new_tokens = (now - last_time) * rate
    tokens = tonumber(redis.call('GET', tokens_key) or '0') + new_tokens
    if tokens > capacity
    then
        tokens = capacity
    end
end

-- 判断是否有 token
if tokens > 0
then
    redis.call('SET', last_time_key, now)
    redis.call('SET', tokens_key, tokens - 1)
    return 1
else
    return 0
end
"""


class RedisTokenRatelimit:
    def __init__(self, rate, capacity):
        self._rate = rate
        self._capacity = capacity

        client = redis.StrictRedis()
        self._lua_script = client.register_script(LUA_SCRIPT.strip())

    def apply(self):
        result = self._lua_script(keys=['my_tokens_key', 'my_last_time_key'], args=[self._rate, self._capacity])
        return result == 1


class TokenRateLimit:
    """
    设置每秒向令牌桶添加令牌数量，请求时先获取令牌，获取成功才允许请求，否则限流

    处理：
    1. 请求前，先根据间隔时间，给令牌桶添加 rate * diff_seconds 具体数量的令牌
    2. 对令牌数量进行扣减，扣减成功则允许请求，否则限流
    """
    def __init__(self, rate, capacity):
        self._rate = rate
        self._capacity = capacity
        self._lock = threading.Lock()

        self._tokens = capacity
        self._last_time = time.monotonic()

    def apply(self) -> bool:
        with self._lock:
            self._refill()
            if self._tokens > 0:
                self._tokens -= 1
                return True
            return False

    def _refill(self):
        # 保证时间单调性
        now = time.monotonic()
        tokens = int((now - self._last_time) * self._rate)
        if tokens > 0:
            self._tokens = min(self._capacity, self._tokens + tokens)
            self._last_time = now


def test_ratelimit(limiter_cls):
    limiter = limiter_cls(2, 3)
    assert limiter.apply()
    assert limiter.apply()
    assert limiter.apply()
    assert not limiter.apply()
    time.sleep(1)
    assert limiter.apply()
    assert limiter.apply()
    assert not limiter.apply()
    assert not limiter.apply()


if __name__ == '__main__':
    test_ratelimit(TokenRateLimit)
    test_ratelimit(RedisTokenRatelimit)
