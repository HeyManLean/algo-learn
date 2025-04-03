# -*- coding: utf-8 -*-

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    # 虚拟头尾节点
    def __init__(self):
        self.head = Node(None)  # type:Node
        self.tail = Node(None)  # type:Node

        self.head.next = self.tail
        self.tail.prev = self.head

        self.count = 0

    # ***** 增 *****

    def add_last(self, element):
        node = Node(element)

        prev = self.tail.prev
        node.prev = prev
        prev.next = node

        node.next = self.tail
        self.tail.prev = node

        self.count += 1

    def add_first(self, element):
        node = Node(element)

        next_node = self.head.next
        node.next = next_node
        next_node.prev = node

        node.prev = self.head
        self.head.next = node

        self.count += 1

    def add(self, index, element):
        if index > self.size():
            raise ValueError("index error")
        prev = self.head
        for _ in range(index):
            prev = prev.next

        node = Node(element)
        next_node = prev.next
        node.next = next_node
        next_node.prev = node

        node.prev = prev
        prev.next = node

        self.count += 1

    # ***** 删 *****

    def remove_first(self):
        first = self.get_first()
        if not first:
            raise ValueError("empty list")

        next_node = first.next

        next_node.prev = self.head
        self.head.next = next_node

        first.next = None
        first.prev = None

        self.count -= 1

    def remove_last(self):
        last = self.get_last()
        if not last:
            raise ValueError("empty list")
        
        prev = last.prev
        prev.next = self.tail
        self.tail.prev = prev

        last.prev = None
        last.next = None

        self.count -= 1

    def remove(self, index):
        if index >= self.size():
            raise ValueError("index error")

        prev = self.head
        for _ in range(index):
            prev = prev.next

        node = prev.next
        next_node = prev.next.next
        prev.next = next_node
        next_node.prev = prev

        node.prev = None
        node.next = None

        self.count -= 1

    # ***** 查 *****

    def get(self, index):
        if index >= self.size():
            raise ValueError("index error")
        
        node = self.head
        for _ in range(index + 1):
            node = node.next

        return node.val

    def get_first(self):
        if self.is_empty():
            return None
        return self.head.next

    def get_last(self):
        if self.is_empty():
            return None
        return self.tail.prev

    # ***** 改 *****

    def set(self, index, val):
        node = self.get_node(index)
        node.val = val

    # ***** 其他工具函数 *****
    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def get_node(self, index):
        if index >= self.size():
            raise ValueError("index error")
        
        node = self.head
        for _ in range(index + 1):
            node = node.next

        return node

    def display(self):
        print(self.size())
        node = self.head
        for _ in range(self.count):
            node = node.next
            print(node.val)


if __name__ == "__main__":
    list = DoublyLinkedList()
    list.add_last(1)
    list.add_last(2)
    list.add_last(3)
    list.add_first(0)
    list.add(2, 100)
    list.remove(1)

    list.display()
    # size = 5
    # 0 <-> 1 <-> 100 <-> 2 <-> 3 <-> null