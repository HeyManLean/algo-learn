# coding=utf-8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list) -> ListNode:
        """Merge K Sorted Lists (medium)

        ```js
        合并K个升序链表
        给你一个链表数组，每个链表都已经按升序排列。

        请你将所有链表合并到一个升序链表中，返回合并后的链表。



        示例 1：

        输入：lists = [[1,4,5],[1,3,4],[2,6]]
        输出：[1,1,2,3,4,4,5,6]
        解释：链表数组如下：
        [
        1->4->5,
        1->3->4,
        2->6
        ]
        将它们合并到一个有序链表中得到。
        1->1->2->3->4->4->5->6
        示例 2：

        输入：lists = []
        输出：[]
        示例 3：

        输入：lists = [[]]
        输出：[]


        提示：

        k == lists.length
        0 <= k <= 10^4
        0 <= lists[i].length <= 500
        -10^4 <= lists[i][j] <= 10^4
        lists[i] 按 升序 排列
        lists[i].length 的总和不超过 10^4
        ```
        """
        if not lists:
            return None

        n = len(lists)

        head = lists[0]

        for i in range(1, n):
            head = self.merge_two_list(head, lists[i])

        return head

    def merge_two_list(self, left: ListNode, right: ListNode):
        if not (left or right):
            return None

        if not right:
            head = left
            left = left.next
        elif not left:
            head = right
            right = right.next
        elif left.val <= right.val:
            head = left
            left = head.next
        else:
            head = right
            right = head.next

        first = head

        while left and right:
            while left and right and left.val <= right.val:
                head.next = left
                head = head.next
                left = left.next

            while right and left and right.val < left.val:
                head.next = right
                head = head.next
                right = right.next

        while left:
            head.next = left
            head = head.next
            left = left.next

        while right:
            head.next = right
            head = head.next
            right = right.next

        return first
