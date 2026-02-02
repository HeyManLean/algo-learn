package bytedance

import (
	"sort"
)

func twoSum(nums []int, target int) [][]int {
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

func threeSum(nums []int) [][]int {
	/*
		15. 三数之和

		给你一个整数数组 nums ，判断是否存在三元组
		[nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。
		请你返回所有和为 0 且不重复的三元组。
		注意：答案中不可以包含重复的三元组。

		输入：nums = [-1,0,1,2,-1,-4]
		输出：[[-1,-1,2],[-1,0,1]]
		解释：nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
		nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
		不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。注意，输出的顺序和三元组的顺序并不重要。

		输入：nums = [0,1,1]
		输出：[]
		解释：唯一可能的三元组和不为 0 。

		输入：nums = [0,0,0]
		输出：[[0,0,0]]
		解释：唯一可能的三元组和为 0 。

		3 <= nums.length <= 3000
		-10^5 <= nums[i] <= 10^5
	*/
	// 暴力
	n := len(nums)
	res := make([][]int, 0)

	sort.Ints(nums) // 排序

	i := 0
	for i < n-2 {
		twoSums := twoSum(nums[i+1:], -nums[i])

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
