package bytedance

// ListNode 链表节点定义
type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseKGroup(head *ListNode, k int) *ListNode {
	/*
		25. K 个一组翻转链表

		给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。

		k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

		你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。


		示例 1：
		输入：head = [1,2,3,4,5], k = 2
		输出：[2,1,4,3,5]

		示例 2：
		输入：head = [1,2,3,4,5], k = 3
		输出：[3,2,1,4,5]

		示例 3：
		输入：head = [1,2,3,4,5], k = 1
		输出：[1,2,3,4,5]


		提示：
		链表中节点的数目为 n
		1 <= k <= n <= 5000
		0 <= Node.val <= 1000


		进阶：你可以设计一个只用 O(1) 额外内存空间的算法解决此问题吗？
	*/

	// 检查是否够 k 个节点
	temp := head
	for i := 0; i < k; i++ {
		if temp == nil {
			return head
		}
		temp = temp.Next
	}

	// 每轮翻转 K 个节点，然后对 head.Next 下一组k个节点继续执行  reverseKGroup
	last := reverseN(head, k)
	head.Next = reverseKGroup(head.Next, k)
	return last
}

var suc *ListNode

func reverseN(head *ListNode, n int) *ListNode {
	/*
		翻转前n个节点，返回新的 head

		// 递归：先反正后面n-1节点，后将当前节点的next指针指向 n+1 位置节点
	*/
	if n == 1 {
		suc = head.Next
		return head
	}

	last := reverseN(head.Next, n-1)
	head.Next.Next = head
	head.Next = suc
	return last
}
