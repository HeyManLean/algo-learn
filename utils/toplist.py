# -*- coding: utf-8 -*-

"""
积分排行榜实现

用户积分累加，优先按照用户的积分进行降序，积分相同达成时间最早优先
"""
import time
from redis import StrictRedis

LUA_SCRIPT = '''
local key = KEYS[1]
local uid = ARGV[1]
local score = tonumber(ARGV[2])
local now = tonumber(ARGV[3])

local current = redis.call("ZSCORE", key, uid) or 0
if current == 0 then
    redis.call("ZADD", key, score * 10000000000000 + 9999999999999 - now, uid)
    return score
else
    local base = math.floor(current / 10000000000000)
    redis.call("ZADD", key, (base + score) * 10000000000000 + 9999999999999 - now, uid)
    return base + score
end
'''


class TopList:
    def __init__(self):
        self.client = StrictRedis()
        self.script = self.client.register_script(LUA_SCRIPT)

    def add_score(self, uid, score):
        now = int(time.time() * 1000)
        self.script(["toplist"], [uid, score, now])

    def get_top(self, n=5):
        ret = []
        for uid, score in self.client.zrevrange("toplist", 0, n - 1, withscores=True):
            ret.append({
                'uid': int(uid),
                'score': score // 10000000000000,
                'value': int(score)
            })
        return ret

    def clean(self):
        self.client.delete("toplist")


top_list = TopList()
top_list.clean()
top_list.add_score(1, 20000)
top_list.add_score(111, 9999)
time.sleep(0.01)
top_list.add_score(99, 9999)
top_list.add_score(66, 8900000)
top_list.add_score(88, 1999)
top_list.add_score(87, 1999)
top_list.add_score(77, 1)

print(top_list.get_top())
