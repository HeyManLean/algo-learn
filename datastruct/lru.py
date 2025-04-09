# -*- coding: utf-8 -*-


class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev  # type:Node
        self.next = next  # type:Node


class LRUCache:
    """146. LRU 缓存
    请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。

    实现 LRUCache 类：
    LRUCache(int capacity)          以 正整数 作为容量 capacity 初始化 LRU 缓存
    - int get(int key)              如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
    - void put(int key, int value)  如果关键字 key 已经存在，则变更其数据值 value ；
                                    如果不存在，则向缓存中插入该组 key-value 。
                                    如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。

    函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
    """

    def __init__(self, capacity: int):
        # 维护一个 hash map 和一个双向链表
        # 1. hash map 通过key索引到链表节点，访问可以做到 O(1)
        # 2. 访问该节点时，将节点移到 head 节点，将前后两节点直连，保证访问时间顺序
        # 3. 容量满时，将尾部节点移除，并将key从hash map移除
        self.map = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        node = self.map.get(key)
        if not node:
            return -1

        self.move_first(node)
        return node.val

    def move_first(self, node: Node):
        """将刚访问的节点移到头部"""
        if node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev

        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove_last(self):
        """检查是否超过容量，超过则移除尾部节点"""
        if self.size <= self.capacity:
            return False

        # 移出尾部节点
        remove_node = self.tail.prev
        self.map.pop(remove_node.key)
        self.tail.prev = remove_node.prev
        remove_node.prev.next = self.tail
        self.size -= 1

    def put(self, key: int, value: int) -> None:
        node = self.map.get(key)
        if node:
            node.val = value
        else:
            node = Node(key, value)
            self.map[key] = node
            self.size += 1

        self.move_first(node)
        self.remove_last()


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)  # 缓存是 {1=1}
    cache.put(2, 2)  # 缓存是 {1=1, 2=2}

    assert cache.head.next.val == 2  # 访问过 2

    assert cache.get(1) == 1  # 返回 1
    assert cache.head.next.val == 1  # 访问过 1

    cache.put(3, 3)  # 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}

    assert cache.size == 2
    assert not cache.map.get(2)
    assert cache.map.get(1) and cache.map.get(1).val == 1
    assert cache.map.get(3) and cache.map.get(3).val == 3

    assert cache.get(2) == -1  # 返回 -1 (未找到)

    cache.put(4, 4)  # 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
    assert cache.size == 2
    assert not cache.map.get(1)
    assert cache.map.get(3) and cache.map.get(3).val == 3
    assert cache.map.get(4) and cache.map.get(4).val == 4

    assert cache.get(1) == -1  # 返回 -1 (未找到)
    assert cache.get(3) == 3  # 返回 3
    assert cache.get(4) == 4  # 返回 4

    print("OK")
