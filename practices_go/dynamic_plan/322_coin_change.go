package dynamicplan

import (
	"math"
)

func coinChange(coins []int, amount int) int {
	/*
		322. 零钱兑换

		给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
		计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

		你可以认为每种硬币的数量是无限的。

		输入：coins = [1, 2, 5], amount = 11
		输出：3
		解释：11 = 5 + 5 + 1

		输入：coins = [2], amount = 3
		输出：-1

		输入：coins = [1], amount = 0
		输出：0

		输入：coins = [1, 16, 17], acount=32
		输出：2  // 16+16

		提示：
		1 <= coins.length <= 12
		1 <= coins[i] <= 231 - 1
		0 <= amount <= 104
	*/
	// dp[i] 表示 金额为 i 时最少得硬币数
	// dp[i] = min(dp[i-coin[c]] for c in coins)
	if amount == 0 {
		return 0
	}
	var min = func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}
	dp := make([]int, amount+1)
	for i := range dp {
		dp[i] = math.MaxInt
		for _, c := range coins {
			if c == i {
				dp[i] = 1
				continue
			}
			if c > i {
				continue
			}
			if dp[i-c] != math.MaxInt {
				dp[i] = min(dp[i], dp[i-c]+1)
			}

		}
	}
	if dp[amount] != math.MaxInt {
		return dp[amount]
	}
	return -1
}
