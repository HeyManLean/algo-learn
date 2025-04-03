# -*- coding: utf-8 -*-

"""
二叉堆，父节点权值都小于等于（或大于等于）左右子节权值

二叉堆是完全二叉树，左边优先紧凑排列，可以退化为使用数组实现

1. 父节点索引：(子节点索引 - 1) // 2
2. 左子节点索引：父节点索引 * 2 + 1
3. 右子节点索引：父节点索引 * 2 + 2

主要应用:
优先级队列
堆排序


"""

class HeapNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

        self.parent = None  # 需要上浮时，借助父节点交换


class MinPriorityQueue:
    # 创建一个容量为 capacity 的最小优先级队列
    def __init__(self, capacity: int):
        self.heap = [None] * capacity
        self.size = 0

    # 返回队列中的元素个数
    def size(self) -> int:
        pass

    # 向队列中插入一个元素
    def push(self, x: int):
        if self.is_full():
            raise ValueError('queue full')

        last = self.size
        self.heap[last] = x
        self.size += 1
        self.swim(last)

    # 返回队列中的最小元素（堆顶元素）
    def peek(self) -> int:
        return self.heap[0]

    # 删除并返回队列中的最小元素（堆顶元素）
    def pop(self) -> int:
        if self.is_empty():
            raise ValueError('queue empty')
        
        val = self.heap[0]

        self.heap[0] = self.heap[self.size - 1]
        # self.heap[self.size - 1] = None  # 可以不用删除
        self.size -= 1

        self.sink(0)
        return val

    def swim(self, node):
        """向上上浮，跟父节点交换"""
        parent = self.parent(node)
        if parent < 0:
            return

        # 当前节点小于父节点，跟父节点交换
        if self.heap[node] < self.heap[parent]:
            self.swap(node, parent)
            return self.swim(parent)

    def sink(self, node):
        """向下下沉，跟子节点交换"""
        left = self.left(node)
        if left >= self.size:
            return

        min_node = left
        right = self.right(node)
        if right < self.size and self.heap[left] > self.heap[right]:
            min_node = right

        if self.heap[min_node] < self.heap[node]:
            self.swap(min_node, node)
            self.sink(min_node)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def parent(self, node):
        return (node - 1) // 2
    
    def left(self, node):
        return node * 2 + 1
    
    def right(self, node):
        return node * 2 + 2
    
    def is_full(self):
        return len(self.heap) == self.size
    
    def is_empty(self):
        return self.size == 0


if __name__ == '__main__':
    pq = MinPriorityQueue(10)
    pq.push(3)
    pq.push(4)
    pq.push(1)
    pq.push(2)

    assert pq.peek() == 1

    assert pq.pop() == 1
    assert pq.pop() == 2
    assert pq.pop() == 3
    assert pq.pop() == 4

    print("OK")
