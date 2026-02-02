package bytedance

// type ListNode struct {
// 	Val  int
// 	Next *ListNode
// }

func reorderList(head *ListNode) {
	/*
		143. 重排链表

		给定一个单链表 L 的头节点 head ，单链表 L 表示为：
		L0 → L1 → … → Ln - 1 → Ln

		请将其重新排列后变为：
		L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

		不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。


		输入：head = [1,2,3,4]
		输出：[1,4,2,3]

		输入：head = [1,2,3,4,5]
		输出：[1,5,2,4,3]


		链表的长度范围为 [1, 5 * 10^4]
		1 <= node.val <= 1000
	*/
	if head == nil || head.Next == nil {
		return
	}
	// 快慢指针到达中点，反转后一半指针
	// 左右指针，往中间靠拢
	slow, fast := head, head
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}
	// A->B->C->D
	// A<->B  C->D
	// 从slow中点反转后面链表
	next := slow.Next
	slow.Next = nil
	for next != nil {
		temp := next.Next
		next.Next = slow
		slow = next
		next = temp
	}
	// slow 到达终点
	left, right := head, slow
	for left != right && left != nil && right != nil {
		leftNext := left.Next
		rightNext := right.Next

		left.Next = right
		right.Next = leftNext

		left = leftNext
		right = rightNext
	}
	if left != nil {
		left.Next = nil
	}
}
