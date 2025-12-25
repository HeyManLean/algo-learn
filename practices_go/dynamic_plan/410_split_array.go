package dynamicplan

import (
	"math"
)

func splitArray(nums []int, k int) int {
	/*
		410. 分割数组的最大值

		给定一个非负整数数组 nums 和一个整数 k ，
		你需要将这个数组分成 k 个非空的连续子数组，使得这 k 个子数组各自和的最大值 最小。
		返回分割后最小的和的最大值。

		子数组 是数组中连续的部份。

		输入：nums = [7,2,5,10,8], k = 2
		输出：18
		解释：
		一共有四种方法将 nums 分割为 2 个子数组。
		其中最好的方式是将其分为 [7,2,5] 和 [10,8] 。
		因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
		示例 2：

		输入：nums = [1,2,3,4,5], k = 2
		输出：9

		输入：nums = [1,4,4], k = 3
		输出：4

		len(nums) >= k >= 1
	*/
	// 决策树，切在哪个位置，还剩几个数组
	// 状态：剩余 x<=k 个子数组

	// 每个子数组的和最小的情况是，每个子数组和都等于平均值
	// 最后一个子数组，和大于平均值的位置和不大于平均值的位置，取两者最小值即可
	// 先计算前缀和 preSum
	// dp[k][i] =

	// preSum[i]: 前i个数的和，[0...i-1]
	n := len(nums)
	preSum := make([]int, n+1)
	for i, num := range nums {
		preSum[i+1] = preSum[i] + num

	}

	dp := make([][]int, n+1)
	for i := range dp {
		dp[i] = make([]int, k+1)
		for j := range dp[i] {
			dp[i][j] = math.MaxInt32
		}
	}

	// 边界条件
	dp[0][0] = 0

	for i := 1; i <= n; i++ {
		for j := 1; j <= minV(i, k); j++ {
			for x := 0; x < i; x++ {
				dp[i][j] = minV(dp[i][j], maxV(dp[x][j-1], preSum[i]-preSum[x]))
			}
		}
	}

	return dp[n][k]
}

func minV(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func maxV(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func splitArrayV2(nums []int, m int) int {
	n := len(nums)
	f := make([][]int, n+1)
	sub := make([]int, n+1)
	for i := 0; i < len(f); i++ {
		f[i] = make([]int, m+1)
		for j := 0; j < len(f[i]); j++ {
			f[i][j] = math.MaxInt32
		}
	}
	for i := 0; i < n; i++ {
		sub[i+1] = sub[i] + nums[i]
	}
	f[0][0] = 0
	for i := 1; i <= n; i++ {
		for j := 1; j <= min(i, m); j++ {
			for k := 0; k < i; k++ {
				f[i][j] = min(f[i][j], max(f[k][j-1], sub[i]-sub[k]))
			}
		}
	}
	return f[n][m]
}
