# coding=utf-8


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverse_linkedlist(self, head: ListNode) -> ListNode:
        """Reverse a LinkedList (easy)

        ```js
        反转链表
        反转一个单链表。

        示例:

        输入: 1->2->3->4->5->NULL
        输出: 5->4->3->2->1->NULL
        进阶:
        你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
        ```
        """
        if not (head and head.next):
            return head

        previous_node = None
        next_node = head.next

        while head.next:
            next_node = head.next
            head.next = previous_node
            previous_node = head
            head = next_node

        head.next = previous_node

        return head
