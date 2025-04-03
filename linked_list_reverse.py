# -*- coding: utf-8 -*-


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverse(head: ListNode) -> ListNode:
    """递归反转整个链表"""
    if not head or not head.next:
        return head

    last = reverse(head.next)
    head.next.next = head
    head.next = None
    return last


sucessor = None

def reverse_n(head: ListNode, n: int) -> ListNode:
    """递归反转前面N个节点"""
    global sucessor
    if n == 1:
        sucessor = head.next  # 记录第N+1个节点
        return head

    last = reverse_n(head.next, n - 1)
    head.next.next = head
    head.next = sucessor  # 尾部指向第N+1个节点
    return last


def reverse_between(head: ListNode, m: int, n: int) -> ListNode:
    """反转指定区间（第m到第n个，索引从1开始）的链表节点"""
    # 调到第 M 个节点时，退化为反转前 n-m+1 个节点
    if m == 1:
        return reverse_n(head, n - m + 1)

    head.next = reverse_between(head.next, m - 1, n - 1)
    return head


def reverse_between_iter(head: ListNode, m: int, n: int) -> ListNode:
    """迭代反转指定区间（第m到第n个，索引从1开始）的链表节点"""
    if m == 1:
        return reverse_n_iter(head, n)

    # 前驱(m>1)
    head.next = reverse_between_iter(head.next, m - 1, n - 1)
    return head


def reverse_iter(head: ListNode) -> ListNode:
    """迭代反转整个链表"""
    if not head or not head.next:
        return head

    prev, cur, next_node = None, head, head.next

    while cur:
        cur.next = prev
        prev = cur
        cur = next_node

        if next_node:
            next_node = next_node.next

    return prev


def reverse_n_iter(head: ListNode, n: int) -> ListNode:
    """迭代反转前面N个节点"""
    if n == 1:
        return head

    prev, cur, next_node = None, head, head.next

    while n > 0:
        cur.next = prev
        prev = cur
        cur = next_node
        n -= 1

        if next_node:
            next_node = next_node.next

    head.next = cur

    return prev


class Solution(object):
    def reverseKGroup(self, head: ListNode, k: int):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return head

        # 找到下一个K组的起点
        successor = head
        for _ in range(k):
            if not successor:
                return head
            successor = successor.next


        last = self.reverseN(head, k)
        head.next = self.reverseKGroup(successor, k)

        return last

    suc = None
    def reverseN(self, head: ListNode, n: int):
        if not head or not head.next:
            return head
        
        if n == 1:
            self.suc = head.next
            return head

        last = self.reverseN(head.next, n - 1)
        head.next.next = head
        head.next = self.suc
        return last


def test_reverse(reverse_func, m=None, n=None):
    print(reverse_func.__name__)
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    if m is None:
        p = reverse_func(head)
    elif n is None:
        p = reverse_func(head, m)
    else:
        p = reverse_func(head, m, n)

    vals = []
    while p:
        vals.append(p.val)
        p = p.next

    arr = [1, 2, 3, 4, 5]
    if m is None:
        expected = arr[::-1]
    elif n is None:
        expected = arr[:m][::-1] + arr[m:]
    else:
        expected = arr[:m-1] + arr[m-1:n][::-1] + arr[n:]

    print(vals, expected)
    assert vals == expected


if __name__ == '__main__':
    test_reverse(reverse)
    test_reverse(reverse_iter)
    test_reverse(reverse_n, 3)
    test_reverse(reverse_n_iter, 3)
    test_reverse(reverse_between, 2, 4)
    test_reverse(reverse_between, 1, 3)
    test_reverse(reverse_between_iter, 2, 4)
    test_reverse(reverse_between_iter, 1, 3)
