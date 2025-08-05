package practicesgo

import (
	"container/heap"
	"strconv"
	"testing"
)

type ReversedIntHeap struct {
	Nums []int
}

func (h *ReversedIntHeap) Len() int {
	return len(h.Nums)
}
func (h *ReversedIntHeap) Less(i, j int) bool {
	return h.Nums[i] > h.Nums[j]
}
func (h *ReversedIntHeap) Swap(i, j int) {
	h.Nums[i], h.Nums[j] = h.Nums[j], h.Nums[i]
}
func (h *ReversedIntHeap) Push(x any) {
	v := x.(int)
	h.Nums = append(h.Nums, v)
}
func (h *ReversedIntHeap) Pop() any {
	v := h.Nums[len(h.Nums)-1]
	h.Nums = h.Nums[:len(h.Nums)-1]
	return v
}

func findKthLargest(nums []int, k int) int {
	/*
		https://leetcode.cn/problems/kth-largest-element-in-an-array/description/
		215. 数组中的第K个最大元素

		给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
		你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

		输入: [3,2,1,5,6,4], k = 2
		输出: 5

		输入: [3,2,3,1,2,4,5,5,6], k = 4
		输出: 4

	*/
	hq := &ReversedIntHeap{
		Nums: nums,
	}
	heap.Init(hq)
	for i := 0; i < k-1; i++ {
		heap.Pop(hq)
	}
	v := heap.Pop(hq)
	return v.(int)
}

func TestFindKthLargest(t *testing.T) {
	cases := []struct {
		Nums     []int
		K        int
		Expected int
	}{
		{[]int{3, 2, 1, 5, 6, 4}, 2, 5},
		{[]int{3, 2, 3, 1, 2, 4, 5, 5, 6}, 4, 4},
	}
	for i, c := range cases {
		t.Run("test"+strconv.Itoa(i), func(t *testing.T) {
			if res := findKthLargest(c.Nums, c.K); res != c.Expected {
				t.Fatalf("case: %v expected: %d, but got %d", c, c.Expected, res)
			}
		})
	}
}
