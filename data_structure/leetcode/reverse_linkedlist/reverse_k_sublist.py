# coding=utf-8
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverse_k_group(self, head: ListNode, k: int) -> ListNode:
        """Reverse every K-element Sub-list (medium)

        ```js
        K 个一组翻转链表
        给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

        k 是一个正整数，它的值小于或等于链表的长度。

        如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

        

        示例：

        给你这个链表：1->2->3->4->5

        当 k = 2 时，应当返回: 2->1->4->3->5

        当 k = 3 时，应当返回: 3->2->1->4->5

        

        说明：

        你的算法只能使用常数的额外空间。
        你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
        ```
        """
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next

        for i in range(1, count + 1, k):
            if i + k - 1 > count:
                break

            head = self.reverse_between(head, i, i + k - 1)

        return head

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

    k = 2

    prev = None
    head = None

    for num in nums:
        node = ListNode(num)
        if prev:
            prev.next = node
        else:
            head = node

        prev = node

    print(head, head.next)
    head = Solution().reverse_k_group(head, k)
    print(head)

    while head:
        print(head.val, '==================')
        head = head.next
