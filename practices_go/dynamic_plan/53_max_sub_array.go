package dynamicplan

func maxSubArray(nums []int) int {
	/*
		53. 最大子数组和

		给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

		子数组是数组中的一个连续部分。

		输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
		输出：6
		解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

		输入：nums = [1]
		输出：1
		示例 3：

		输入：nums = [5,4,-1,7,8]
		输出：23

		1 <= nums.length <= 105
		-104 <= nums[i] <= 104

		进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。
	*/
	// dp[i] 表示包含当前元素的最大和连续子数组的和
	// 处理i时，dp[i] = max(dp[i-1] + nums[i], nums[i])
	if len(nums) == 0 {
		return 0
	}
	n := len(nums)
	dp := make([]int, n)
	dp[0] = nums[0]

	var max = func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}
	res := dp[0]

	for i := 1; i < n; i++ {
		dp[i] = max(dp[i-1]+nums[i], nums[i])
		res = max(res, dp[i])
	}
	return res
}
