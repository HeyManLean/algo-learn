package bytedance

// ListNode 链表节点定义
// type ListNode struct {
// 	Val  int
// 	Next *ListNode
// }

import (
	"container/heap"
)

type ListNodeHeap struct {
	lists []*ListNode
}

func (h *ListNodeHeap) Push(x any) {
	h.lists = append(h.lists, x.(*ListNode))
}
func (h *ListNodeHeap) Pop() any {
	temp := h.lists[len(h.lists)-1]
	h.lists = h.lists[0 : len(h.lists)-1]
	return temp
}

func (h *ListNodeHeap) Len() int {
	return len(h.lists)
}

func (h *ListNodeHeap) Less(i, j int) bool {
	return h.lists[i].Val < h.lists[j].Val
}
func (h *ListNodeHeap) Swap(i, j int) {
	h.lists[i], h.lists[j] = h.lists[j], h.lists[i]
}

func mergeKLists(lists []*ListNode) *ListNode {
	/*
		23. 合并K个排序链表

		给你一个链表数组，每个链表都已经按升序排列。

		请你将所有链表合并到一个升序链表中，返回合并后的链表。


		输入: lists = [[1,4,5],[1,3,4],[2,6]]
		输出: [1,1,2,3,4,4,5,6]
		解释: 链表数组如下：
		  1->4->5,
		  1->3->4,
		  2->6
		将它们合并到一个有序链表中得到。
		1->1->2->3->4->4->5->6

		输入: lists = []
		输出: []

		输入: lists = [[]]
		输出: []

		k == lists.length
		0 <= k <= 10^4
		0 <= lists[i].length <= 500
		-10^4 <= lists[i][j] <= 10^4
		lists[i] 按 升序 排列
		lists[i].length 的总和不超过 10^4
	*/
	// 将链表放到最小堆里面，每次去最小的堆，并将链表下一个节点推进堆，以此类推
	h := &ListNodeHeap{}
	for _, list := range lists {
		if list == nil {
			continue
		}
		heap.Push(h, list)
	}

	dummy := &ListNode{}
	cur := dummy

	for h.Len() > 0 {
		temp := heap.Pop(h).(*ListNode)
		if temp.Next != nil {
			heap.Push(h, temp.Next)
		}

		cur.Next = temp
		cur = cur.Next
	}
	return dummy.Next
}
