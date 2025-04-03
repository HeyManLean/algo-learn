# -*- coding: utf-8 -*-
import random
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class HashMap:
    """hash 数组是不紧凑的，如果随机取值时间复杂度是O(N)，使用一个紧凑数组存储"""
    def __init__(self, size=4):
        self.arr = [None] * size  # type:list[Node]
        self.capacity = size
        self.size = 0

    def hash_index(self, key):
        return hash(key) % self.capacity

    def get(self, key):
        node = self.get_node(key)
        if not node:
            return None
        return node.val

    def put(self, key, val):
        index = self.hash_index(key)
        node = self.arr[index]
        if node is None:
            self.arr[index] = Node(key, val)
            self.size += 1
            return

        prev_node = None
        while node:
            # 需要检查key是否重复
            if node.key == key:
                node.val = val
                return
            prev_node = node
            node = node.next

        prev_node.next = Node(key, val)
        self.size += 1
        if self.size >= self.capacity * 0.75:
            self.resize(self.capacity * 2)

    def resize(self, new_size):
        print('resize', self.capacity, new_size)
        arr = self.arr
        self.arr = [None] * new_size
        self.capacity = new_size
        self.size = 0

        for node in arr:
            while node:
                self.put(node.key, node.val)
                node = node.next


    def remove(self, key):
        index = self.hash_index(key)
        node = self.arr[index]
        if node is None:
            raise KeyError('key not found')

        prev_node = None
        while node:
            if node.key == key:
                break
            prev_node = node
            node = node.next

        if not node:
            return

        if prev_node:
            prev_node.next = node.next
        else:
            self.arr[index] = None

        self.size -= 1
        if self.size < self.capacity * 0.125:
            self.resize(max(self.capacity * 0.25, 1))

    def has_key(self, key):
        return bool(self.get_node(key))

    def keys(self):
        keys = []
        for node in self.arr:
            while node:
                keys.append(node.key)
                node = node.next
        return keys

    def get_node(self, key):
        index = self.hash_index(key)
        node = self.arr[index]
        while node:
            if node.key == key:
                return node
            node = node.next

        return None



class ArrayHashMap:
    """hashmap的节点是不紧凑的，如果需要随机返回一个key，时间复杂度是 O(N)

    新增一个 nodes 数组，紧凑存储节点，使用hashmap存储 key 到 nodes 的索引
    """
    def __init__(self):
        self.map = HashMap()
        self.nodes = []

    def get(self, key):
        node_index = self.map.get(key)
        if node_index is None:
            return None
        return self.nodes[node_index].val

    def put(self, key, val):
        node_index = self.map.get(key)
        if node_index is not None:
            self.nodes[node_index].val = val
            return
        
        node_index = len(self.nodes)
        self.nodes.append(Node(key, val))
        self.map.put(key, node_index)

    def remove(self, key):
        node_index = self.map.get(key)
        if node_index is None:
            return
        
        self.map.remove(key)

        self.nodes[node_index] = self.nodes[-1]
        self.nodes.pop()

    def random_key(self):
        return self.nodes[random.randint(0, len(self.nodes) - 1)].key

    def keys(self):
        return [node.key for node in self.nodes]


if __name__ == '__main__':
    map = HashMap()
    map.put("a", 1)
    map.put("b", 2)
    map.put("c", 3)
    map.put("d", 4)
    # map.put("e", 5)
    map.put("z", 5)

    print(map.keys())  # ['a', 'b', 'c', 'd', 'e']
    map.remove("c")
    print(map.keys())  # ['a', 'b', 'd', 'e']
    for c in 'abdz':
        print(c, map.hash_index(c), map.get(c))

    map = ArrayHashMap()
    map.put(1, 1)
    map.put(2, 2)
    map.put(3, 3)
    map.put(4, 4)
    map.put(5, 5)

    print(map.get(1))
    print(map.random_key())

    map.remove(4)
    print(map.random_key())
    print(map.random_key())
