package bytedance

import (
	"container/heap"
)

type MaxHeap struct {
	list []int
}

func (h *MaxHeap) Len() int {
	return len(h.list)
}

func (h *MaxHeap) Less(i, j int) bool {
	return h.list[i] > h.list[j]
}

func (h *MaxHeap) Swap(i, j int) {
	h.list[i], h.list[j] = h.list[j], h.list[i]
}

func (h *MaxHeap) Push(x any) {
	h.list = append(h.list, x.(int))
}

func (h *MaxHeap) Pop() any {
	res := h.list[len(h.list)-1]
	h.list = h.list[:len(h.list)-1]
	return res
}

func findKthLargest(nums []int, k int) int {
	/*
		215. 数组中的第K个最大元素

		给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

		请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

		输入：nums = [3,2,1,5,6,4], k = 2
		输出：5

		输入：nums = [3,2,3,1,2,4,5,5,6], k = 4
		输出：4

		1 <= k <= nums.length <= 10^5
		-10^4 <= nums[i] <= 10^4
	*/
	h := &MaxHeap{}
	for _, num := range nums {
		heap.Push(h, num)
	}

	res := 0
	for i := 0; i < k; i++ {
		res = heap.Pop(h).(int)
	}
	return res
}
