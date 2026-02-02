package bytedance

func reverseBetween(head *ListNode, left int, right int) *ListNode {
	/*
		92. 反转链表 II

		给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。
		请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。


		输入：head = [1,2,3,4,5], left = 2, right = 4
		输出：[1,4,3,2,5]

		输入：head = [5], left = 1, right = 1
		输出：[5]


		链表中节点数目为 n
		1 <= n <= 500
		-500 <= Node.val <= 500
		1 <= left <= right <= n

		进阶： 你可以使用一趟扫描完成反转吗？
	*/

	var suc *ListNode
	var reverseN func(head *ListNode, n int) *ListNode
	reverseN = func(head *ListNode, n int) *ListNode {
		if n == 1 {
			suc = head.Next
			return head
		}
		// 先反转 n-1 在将head反转
		last := reverseN(head.Next, n-1)
		head.Next.Next = head
		head.Next = suc
		return last
	}
	start := head
	pre := head
	for i := 0; i < left-1; i++ {
		pre = start
		start = start.Next
	}

	last := reverseN(start, right-left+1)
	if left == 1 {
		return last
	}

	pre.Next = last
	return head
}
