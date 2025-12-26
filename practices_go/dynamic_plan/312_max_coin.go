package dynamicplan

func maxCoins(nums []int) int {
	/*
		312. 戳气球
		有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
		现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。
		这里的 i - 1 和 i + 1 代表和 i 相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。

		求所能获得硬币的最大数量。

		输入：nums = [3,1,5,8]
		输出：167
		nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
		coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

		输入：nums = [1,5]
		输出：10
	*/
	// 假设在 (i, j) 区间中，k位置是最后一个戳破的，那么最大数量是 (i,k) 最大值 + (k,j) 最大值 + nums[i-1] * nums[k] + nums[j-1] (两侧)
	// 开区间

	// 状态: dp[i][j] 表示 (i, j) 区间的最大硬币数量
	// 遍历 i-j 之间位置，假设是最后一个戳破，最大硬币数更新到 dp[i][j]
	// dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
	// 两侧插入 1， 避免越界且方便计算，dp[0][n] 就是结果值

	n := len(nums)

	newNums := []int{1}
	newNums = append(newNums, nums...)
	newNums = append(newNums, 1)

	dp := make([][]int, n+2)
	for i := range dp {
		dp[i] = make([]int, n+2)
	}

	// 要先更新 dp[k][j] 和 dp[i][k]，才能算出 dp[i][j]
	// 先计算按照短的长度，从 2 到 n
	for length := 2; length <= n+1; length++ {
		for i := 0; i+length <= n+1; i++ {
			j := i + length
			for k := i + 1; k < j; k++ {
				dp[i][j] = max(dp[i][j], dp[i][k]+dp[k][j]+newNums[i]*newNums[k]*newNums[j])
			}
		}
	}
	return dp[0][n+1]
}

func maxC(x, y int) int {
	if x > y {
		return x
	}
	return y
}
