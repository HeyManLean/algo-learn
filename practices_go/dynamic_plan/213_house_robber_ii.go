package dynamicplan

func rob(nums []int) int {
	/*
		213. 打家劫舍 II

		你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。
		同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

		给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，今晚能够偷窃到的最高金额。

		示例 1：
		输入：nums = [2,3,2]
		输出：3
		解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

		示例 2：
		输入：nums = [1,2,3,1]
		输出：4
		解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
		     偷窃到的最高金额 = 1 + 3 = 4 。

		示例 3：
		输入：nums = [1,2,3]
		输出：3

		1 <= nums.length <= 100
		0 <= nums[i] <= 1000
	*/
	n := len(nums)
	if n == 0 {
		return 0
	}
	if n == 1 {
		return nums[0]
	}

	// 两段线性取最大
	a := robLine(nums[:n-1]) // 不考虑最后一间
	b := robLine(nums[1:])   // 不考虑第一间
	if a > b {
		return a
	}
	return b
}

func robLine(nums []int) int {
	// dp[i] 表示前面i个房屋能偷到的最多钱，这里不一定要偷i
	if len(nums) == 0 {
		return 0
	}
	if len(nums) == 1 {
		return nums[0]
	}
	n := len(nums)
	dp := make([]int, n)

	var max = func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	dp[0] = nums[0]
	dp[1] = max(nums[1], nums[0])
	for i := 2; i < n; i++ {
		dp[i] = max(dp[i-2]+nums[i], dp[i-1])
	}
	return dp[n-1]
}
