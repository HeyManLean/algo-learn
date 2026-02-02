package bytedance

import (
	"sort"
)

func fourSum(nums []int, target int) [][]int {
	/*
		18. 四数之和

		给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：

		a、b、c 和 d 互不相同
		nums[a] + nums[b] + nums[c] + nums[d] == target

		你可以按 任意顺序 返回答案 。

		输入：nums = [1,0,-1,0,-2,2], target = 0
		输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

		输入：nums = [2,2,2,2,2], target = 8
		输出：[[2,2,2,2]]

		1 <= nums.length <= 200
		-10^9 <= nums[i] <= 10^9
		-10^9 <= target <= 10^9
	*/
	var twoSum = func(nums []int, target int) [][]int {
		// sort.Ints(nums)  // 排序
		// 左右指针收缩
		n := len(nums)
		lo, hi := 0, n-1

		res := make([][]int, 0)

		for lo < hi {
			cur := nums[lo] + nums[hi]
			if cur < target {
				// 左边收缩
				lo++
			} else if cur > target {
				hi--
			} else {
				res = append(res, []int{nums[lo], nums[hi]})
				// 左边收缩，直到跟当前数字不同
				left := nums[lo]
				lo++
				for lo < n-1 && nums[lo] == left {
					lo++
				}
			}
		}
		return res
	}

	var threeSum = func(nums []int, target int) [][]int {
		// 暴力
		n := len(nums)
		res := make([][]int, 0)

		// sort.Ints(nums) // 排序

		i := 0
		for i < n-2 {
			twoSums := twoSum(nums[i+1:], target-nums[i])

			for _, twoSum := range twoSums {
				res = append(res, []int{nums[i], twoSum[0], twoSum[1]})
			}

			// 避免相同
			left := nums[i]
			i++
			for i < n-2 && nums[i] == left {
				i++
			}
		}
		return res
	}

	n := len(nums)
	res := make([][]int, 0)
	sort.Ints(nums)

	i := 0
	for i < n-3 {
		sums := threeSum(nums[i+1:], target-nums[i])

		for _, sum := range sums {
			res = append(res, []int{nums[i], sum[0], sum[1], sum[2]})
		}

		// 避免相同
		left := nums[i]
		i++
		for i < n-3 && nums[i] == left {
			i++
		}
	}
	return res
}
