package bytedance

func firstMissingPositive(nums []int) int {
	/*
		41. 缺失的第一个正数

		给你一个未排序的整数数组 nums，请你找出其中没有出现的最小的正整数。

		请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。


		输入: nums = [1,2,0]
		输出: 3
		解释: 范围 [1,2] 中的数字都在数组中。

		输入: nums = [3,4,-1,1]
		输出: 2
		解释: 1 在数组中，但 2 没有。

		输入: nums = [7,8,9,11,12]
		输出: 1
		解释: 最小的正数 1 没有出现。

		1 <= nums.length <= 10^5
		-2^31 <= nums[i] <= 2^31 - 1
	*/
	// 原地交换，保证 i 位置的数值就是 i，数值大于1，则0位置放1
	// 第二次遍历，找出第一个位置跟数值不相符的，返回该位置索引

	n := len(nums)
	for i := 0; i < n; i++ {
		// 将索引为 nums[i]-1的值交换为 nums[i]
		for nums[i] >= 1 && nums[i] <= n && nums[nums[i]-1] != nums[i] {
			j := nums[i] - 1
			nums[i], nums[j] = nums[j], nums[i]
		}
	}
	for i := 0; i < n; i++ {
		if nums[i] != i+1 {
			return i + 1
		}
	}
	return n + 1
}
