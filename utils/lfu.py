# -*- coding: utf-8 -*-
from collections import OrderedDict


class Node:
    def __init__(self, key, val, freq=1):
        self.key = key
        self.val = val
        self.freq = freq


class LFUCache:
    """460. LFU 缓存
    实现 LFUCache 类：

    LFUCache(int capacity) - 用数据结构的容量 capacity 初始化对象
        int get(int key) - 如果键 key 存在于缓存中，则获取键的值，否则返回 -1 。
        void put(int key, int value) - 如果键 key 已存在，则变更其值；
                                     如果键不存在，请插入键值对。

    当缓存达到其容量 capacity 时，则应该在插入新项之前，移除最不经常使用的项。

    在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除 最久未使用 的键。
    为了确定最不常使用的键，可以为缓存中的每个键维护一个 使用计数器 。使用计数最小的键是最久未使用的键。
    当一个键首次插入到缓存中时，它的使用计数器被设置为 1 (由于 put 操作)。

    对缓存中的键执行 get 或 put 操作，使用计数器的值将会递增。
    函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
    """

    def __init__(self, capacity: int):
        self.map = {}  # type:dict[int, Node]
        self.freq_to_keys = {}
        self.min_freq = 1
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        node = self.map.get(key)
        if not node:
            return -1

        self.add_freq(node)
        return node.val

    def add_freq(self, node):
        # 从原本的 FV 移除
        self.freq_to_keys[node.freq].pop(node.key)
        if not self.freq_to_keys[node.freq]:
            # 最小频次的key空了，需要加1
            if node.freq == self.min_freq:
                self.min_freq = node.freq + 1
            self.freq_to_keys.pop(node.freq)

        # 加入新的 FV
        node.freq += 1
        self.freq_to_keys.setdefault(node.freq, OrderedDict())
        self.freq_to_keys[node.freq][node.key] = 1

    def remove_min(self):
        """移除最小频率的节点
        - 从列表移除，不需要更新 min_freq，put 会重置 min_freq
        """
        keys = self.freq_to_keys.get(self.min_freq)
        if not keys:
            return

        key, _ = keys.popitem(last=False)
        self.map.pop(key)
        if not keys:
            self.freq_to_keys.pop(self.min_freq)
        self.size -= 1

    def put(self, key: int, value: int) -> None:
        """添加节点"""
        node = self.map.get(key)
        if node:
            node.val = value
            self.add_freq(node)
            return

        # 新增 node，需要检查是否超过容量，移除掉最小频率的值
        if self.size + 1 > self.capacity:
            self.remove_min()

        self.min_freq = 1
        self.freq_to_keys.setdefault(self.min_freq, OrderedDict())
        self.freq_to_keys[self.min_freq][key] = 1
        self.map[key] = Node(key, value)
        self.size += 1


if __name__ == "__main__":
    lfu = LFUCache(2)
    lfu.put(1, 1)  # cache=[1,_], cnt(1)=1
    lfu.put(2, 2)  # cache=[2,1], cnt(2)=1, cnt(1)=1
    assert lfu.get(1) == 1  # 返回 1
    assert len(lfu.map.keys()) == 2
    assert len(lfu.freq_to_keys.keys()) == 2
    # cache=[1,2], cnt(2)=1, cnt(1)=2
    lfu.put(3, 3)  # 去除键 2 ，因为 cnt(2)=1 ，使用计数最小
    assert len(lfu.map.keys()) == 2
    assert len(lfu.freq_to_keys.keys()) == 2
    # cache=[3,1], cnt(3)=1, cnt(1)=2
    assert lfu.get(2) == -1  # 返回 -1（未找到）
    assert lfu.get(3) == 3  # 返回 3
    # cache=[3,1], cnt(3)=2, cnt(1)=2
    lfu.put(4, 4)  # 去除键 1 ，1 和 3 的 cnt 相同，但 1 最久未使用
    # cache=[4,3], cnt(4)=1, cnt(3)=2
    assert lfu.get(1) == -1  # 返回 -1（未找到）
    assert lfu.get(3) == 3  # 返回 3
    # cache=[3,4], cnt(4)=1, cnt(3)=3
    assert lfu.get(4) == 4  # 返回 4
    # cache=[3,4], cnt(4)=2, cnt(3)=3
    print("OK")
