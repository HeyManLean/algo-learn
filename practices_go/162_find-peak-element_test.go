package practicesgo

import (
	"fmt"
	"testing"
)

func findPeakElement(nums []int) int {
	/*
		162. 寻找峰值
		峰值元素是指其值严格大于左右相邻值的元素。
		给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
		你可以假设 nums[-1] = nums[n] = -∞ 。
		你必须实现时间复杂度为 O(log n) 的算法来解决此问题。

		对于所有有效的 i 都有 nums[i] != nums[i + 1]
	*/
	// 简述：寻找比左右位置的值大的位置
	// 二分法，判断中点是否峰值，如果中点右边偏大，往右边遍历，否则往左边遍历
	left := 0
	right := len(nums) - 1

	for left < right {
		mid := (right + left) / 2
		if nums[mid] < nums[mid+1] {
			left = mid + 1
		} else {
			right = mid
		}
	}
	return left
}

func TestFindPeakElement(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		want int
	}{
		{
			name: "2",
			nums: []int{1, 2, 1, 3, 5, 6, 4},
			want: 5,
		},
		{
			name: "3",
			nums: []int{6, 5, 4, 3, 2, 3, 2},
			want: 0,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			fmt.Println(tt.nums)
			if got := findPeakElement(tt.nums); got != tt.want {
				t.Errorf("findPeakElement(%v) = %v, want %v", tt.nums, got, tt.want)
			}
			// 	t.Errorf("findPeakElement() = %v, want %v", got, tt.expected)
			// }
		})
	}
}
