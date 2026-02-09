package bytedance

import "container/heap"

type KSNode struct {
	Left  int
	Right int
	Val   int
}

type KSNodeHeap struct {
	lists []*KSNode
}

func (h *KSNodeHeap) Push(x any) {
	h.lists = append(h.lists, x.(*KSNode))
}
func (h *KSNodeHeap) Pop() any {
	temp := h.lists[len(h.lists)-1]
	h.lists = h.lists[0 : len(h.lists)-1]
	return temp
}

func (h *KSNodeHeap) Len() int {
	return len(h.lists)
}

func (h *KSNodeHeap) Less(i, j int) bool {
	return h.lists[i].Val < h.lists[j].Val
}
func (h *KSNodeHeap) Swap(i, j int) {
	h.lists[i], h.lists[j] = h.lists[j], h.lists[i]
}

func kSmallestPairs(nums1 []int, nums2 []int, k int) [][]int {
	/*
		373. 查找和最小的 K 对数字

		给定两个以 非递减顺序排列 的整数数组 nums1 和 nums2 , 以及一个整数 k 。

		定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2 。

		请找到和最小的 k 个数对 (u1,v1),  (u2,v2)  ...  (uk,vk) 。

		示例 1:
		输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
		输出: [[1,2],[1,4],[1,6]]
		解释: 返回序列中的前 3 对数：
		     [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

		示例 2:
		输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
		输出: [[1,1],[1,1]]
		解释: 返回序列中的前 2 对数：
		     [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

		示例 3:
		输入: nums1 = [1,2], nums2 = [3], k = 3
		输出: [[1,3],[2,3]]
		解释: 也可能序列中所有的数对都被返回:[1,3],[2,3]

		提示:
		1 <= nums1.length, nums2.length <= 10^5
		-10^9 <= nums1[i], nums2[i] <= 10^9
		nums1 和 nums2 均为升序排列
		1 <= k <= 10^4
	*/
	// 最小的在 0,0 位置
	// 扔到最小堆，pop出来后，将下一个位置的值扔进来
	n := len(nums2)
	h := &KSNodeHeap{}

	for i, num := range nums1 {
		heap.Push(h, &KSNode{
			Left:  i,
			Right: 0,
			Val:   num + nums2[0],
		})
	}

	res := make([][]int, 0)

	for k > 0 && h.Len() != 0 {
		node := heap.Pop(h).(*KSNode)
		res = append(res, []int{nums1[node.Left], nums2[node.Right]})
		k--
		if node.Right < n-1 {
			heap.Push(h, &KSNode{
				Left:  node.Left,
				Right: node.Right + 1,
				Val:   nums1[node.Left] + nums2[node.Right+1],
			})
		}
	}
	return res
}
