# coding=utf-8


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverse_between(self, head: ListNode, m: int, n: int) -> ListNode:
        """Reverse a Sub-list (medium)

        ```js
        反转链表 II
        反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

        说明:
        1 ≤ m ≤ n ≤ 链表长度。

        示例:

        输入: 1->2->3->4->5->NULL, m = 2, n = 4
        输出: 1->4->3->2->5->NULL
        ```
        """
        if not (head and head.next) or m == n:
            return head

        start = head
        pre_start = None

        for _ in range(1, m):
            pre_start = start
            start = start.next

        prev = start
        cur = start.next

        while m < n:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

            m += 1

        start.next = cur

        if pre_start:
            pre_start.next = prev
            return head
        else:
            return prev


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]

    m = 1
    n = 2

    prev = None
    head = None

    for num in nums:
        node = ListNode(num)
        if prev:
            prev.next = node
        else:
            head = node

        prev = node

    head = Solution().reverse_between(head, m, n)

    while head:
        print(head.val)
        head = head.next
