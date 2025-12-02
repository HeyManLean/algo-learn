package practicesgo

import (
	"fmt"
	"testing"
)

func findMin(nums []int) int {
	/*
		153. 寻找旋转排序数组中的最小值

		已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
		若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
		若旋转 7 次，则可以得到 [0,1,2,4,5,6,7]
		注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。

		给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。

		你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。

		输入：nums = [3,4,5,1,2]
		输出：1

		输入：nums = [4,5,6,7,0,1,2]
		输出：0

		输入：nums = [11,13,15,17]
		输出：11
	*/
	// 简述：找出一个旋转过的有序集合的最小的元素
	// 双指针+二分法：如果左端比中间小，中间比右端大，则遍历右侧元素，否则遍历左侧元素
	n := len(nums)
	left := 0
	right := n - 1
	for left < right {
		mid := (left + right) / 2
		if nums[left] < nums[right] {
			return nums[left]
		}
		if nums[left] <= nums[mid] && nums[mid] > nums[right] {
			left = mid + 1
		} else {
			right = mid
		}
	}
	return nums[left]
}

func TestFindMin(t *testing.T) {
	tests := []struct {
		nums []int
		want int
	}{
		{[]int{3, 4, 5, 1, 2}, 1},
		{[]int{4, 5, 6, 7, 0, 1, 2}, 0},
		{[]int{11, 13, 15, 17}, 11},
		{[]int{1}, 1},
		{[]int{2, 1}, 1},
	}
	for _, test := range tests {
		t.Run(fmt.Sprintf("test %d", test.nums), func(t *testing.T) {
			got := findMin(test.nums)
			if got != test.want {
				t.Errorf("findMin(%v) = %d, want %d", test.nums, got, test.want)
			}
		})
	}
}
