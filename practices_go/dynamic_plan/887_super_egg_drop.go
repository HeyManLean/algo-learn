package dynamicplan

import (
	"math"
)

func superEggDropV3(k int, n int) int {
	// 空间优化
	dp := make([]int, k+1)
	// 首行为0

	for i := 1; i < n+1; i++ {
		// 依赖上一行数据，左上角和上方
		for j := k; j >= 1; j-- {
			dp[j] = 1 + dp[j-1] + dp[j]
		}
		if dp[k] >= n {
			return i
		}
	}
	return -1
}

func superEggDropV2(k int, n int) int {
	// 优化，调整状态为  i=操作数，j=鸡蛋数，值为能确定 f 的最大楼层数
	// 操作数 i <= n 最大楼层数

	// 最后取，值为 n， 鸡蛋数为 k 的，最小的 i
	dp := make([][]int, n+1)
	for i := 0; i < n+1; i++ {
		dp[i] = make([]int, k+1)
	}

	for i := 1; i < n+1; i++ {
		for j := 1; j < k+1; j++ {
			// 为什么是相加！
			// 输入：k = 1, n = 2
			// 输出：2
			// 解释：
			// 鸡蛋从 1 楼掉落。如果它碎了，肯定能得出 f = 0 。
			// 否则，鸡蛋从 2 楼掉落。如果它碎了，肯定能得出 f = 1 。
			// 如果它没碎，那么肯定能得出 f = 2 。
			dp[i][j] = 1 + dp[i-1][j-1] + dp[i-1][j]
		}
		if dp[i][k] >= n {
			return i
		}
	}

	return -1
}

func minOp(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func superEggDrop(k int, n int) int {
	return superEggDropV3(k, n)
	/*
		887. 鸡蛋掉落

		给你 k 枚相同的鸡蛋，并可以使用一栋从第 1 层到第 n 层共有 n 层楼的建筑。
		已知存在楼层 f ，满足 0 <= f <= n ，任何从 高于 f 的楼层落下的鸡蛋都会碎，从 f 楼层或比它低的楼层落下的鸡蛋都不会破。
		每次操作，你可以取一枚没有碎的鸡蛋并把它从任一楼层 x 扔下（满足 1 <= x <= n）。
		如果鸡蛋碎了，你就不能再次使用它。如果某枚鸡蛋扔下后没有摔碎，则可以在之后的操作中 重复使用 这枚鸡蛋。

		请你计算并返回要确定 f 确切的值 的 最小操作次数 是多少？

		输入：k = 1, n = 2
		输出：2
		解释：
		鸡蛋从 1 楼掉落。如果它碎了，肯定能得出 f = 0 。
		否则，鸡蛋从 2 楼掉落。如果它碎了，肯定能得出 f = 1 。
		如果它没碎，那么肯定能得出 f = 2 。
		因此，在最坏的情况下我们需要移动 2 次以确定 f 是多少。

		输入：k = 2, n = 6
		输出：3

		输入：k = 3, n = 14
		输出：4
	*/
	// 碎了或没碎是随机事件，如果要确定，应该取两者最大操作数的那个（最坏情况）
	// 选择是 x 为 1~n 层，取最小操作数的那一层作为 dp[i][j]

	dp := make([][]int, k+1)
	for i := 0; i < k+1; i++ {
		dp[i] = make([]int, n+1)
	}

	// 首行， 0 个鸡蛋，不用处理
	// 首列，0层楼，不用处理

	// 第二行、第二列
	// for i := 1; i <= k; i++ {
	// 	// dp[i][0] = 0
	// 	dp[i][1] = 1
	// }
	// // 1 个蛋 → 必须从 1 到 n 线性扫描 → n 次
	// for j := 1; j <= n; j++ {
	// 	dp[1][j] = j
	// }

	// 1个鸡蛋，j层，需要j个操作
	for j := 1; j < n+1; j++ {
		dp[1][j] = j
	}
	// 只有一层，只需要一个操作
	for i := 1; i < k+1; i++ {
		dp[i][1] = 1
	}

	// 让“最坏情况”最小的楼层 x
	for i := 2; i < k+1; i++ {
		for j := 2; j < n+1; j++ {
			minSteps := math.MaxInt

			for x := 1; x <= j; x++ {
				// 碎了或不碎
				steps := 1 + maxOp(dp[i-1][x-1], dp[i][j-x])
				if steps < minSteps {
					minSteps = steps
				}
			}
			dp[i][j] = minSteps
		}
	}
	return dp[k][n]
}

func maxOp(x int, y int) int {
	if x > y {
		return x
	}
	return y
}
