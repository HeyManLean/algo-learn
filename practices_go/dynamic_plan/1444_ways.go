package dynamicplan

func ways(pizza []string, k int) int {
	/*
		1444. 切披萨的方案数

		给你一个 rows x cols 大小的矩形披萨和一个整数 k ，
		矩形包含两种字符： 'A' （表示苹果）和 '.' （表示空白格子）。你需要切披萨 k-1 次，得到 k 块披萨并送给别人。
		切披萨的每一刀，先要选择是向垂直还是水平方向切，再在矩形的边界上选一个切的位置，
		将披萨一分为二。如果垂直地切披萨，那么需要把左边的部分送给一个人，
		如果水平地切，那么需要把上面的部分送给一个人。在切完最后一刀后，需要把剩下来的一块送给最后一个人。

		请你返回确保每一块披萨包含 至少 一个苹果的切披萨方案数。
		由于答案可能是个很大的数字，请你返回它对 10^9 + 7 取余的结果。


		输入：pizza = [
			"A..",
			"AAA",
			"..."
		], k = 3
		输出：3
		解释：上图展示了三种切披萨的方案。注意每一块披萨都至少包含一个苹果。

		输入：pizza = [
			"A..",
			"AA.",
			"..."
		], k = 3
		输出：1

		输入：pizza = ["A..","A..","..."], k = 1
		输出：1

	*/
	// 需要方法判断某个区域是否有苹果
	// 先维护一个二维数组 postSum，表示该位置右下方的苹果数量
	// 求某个区域苹果数量：r1,c1,r2,c2 = postSum[r1][c1] - postSum[r2+1][c1] - postSum[r1][c2+1] + postSum[r2+1][c2+1]
	const mod = 1_000_000_007
	rows := len(pizza)
	cols := len(pizza[0])
	apples := make([][]int, rows+1)
	for r := range apples {
		apples[r] = make([]int, cols+1)
	}

	// dp: 状态 披萨数量、当前行、当前列，值为方案数量
	dp := make([][][]int, k+1)
	for i := range dp {
		dp[i] = make([][]int, rows)
		for r := range dp[i] {
			dp[i][r] = make([]int, cols)
		}
	}

	// 从右下角开始计算位置右下方的苹果数量
	for r := rows - 1; r >= 0; r-- {
		rowApples := 0
		for c := cols - 1; c >= 0; c-- {
			if pizza[r][c] == 'A' {
				rowApples += 1
			}
			// 右下角的苹果数，等于当前行右侧苹果数量 + 下一行同一列的右下角数量
			apples[r][c] = rowApples + apples[r+1][c]

			// 边界条件：k=1 的时候，如果区域有苹果，则方案为1，否则为0
			if apples[r][c] > 0 {
				dp[1][r][c] = 1
			}
		}
	}

	// 判断是否可以水平切、垂直切，将方案累加
	for remains := 2; remains < k+1; remains++ {
		for r := 0; r < rows; r++ {
			for c := 0; c < cols; c++ {
				// 水平切：每一行是否有苹果，则累加
				for nr := r + 1; nr < rows; nr++ {
					if apples[r][c] > apples[nr][c] {
						dp[remains][r][c] = (dp[remains][r][c] + dp[remains-1][nr][c]) % mod
					}
				}
				// 垂直切：对剩下的列，选择一列进行下一切(切完左右都有苹果），累加结果
				for nc := c; nc < cols; nc++ {
					if apples[r][c] > apples[r][nc] {
						dp[remains][r][c] = (dp[remains][r][c] + dp[remains-1][r][nc]) % mod
					}
				}
			}
		}
	}
	return dp[k][0][0]
}

func waysV2(pizza []string, k int) int {
	m := len(pizza)
	n := len(pizza[0])
	mod := 1_000_000_007
	apples := make([][]int, m+1)
	for i := range apples {
		apples[i] = make([]int, n+1)
	}
	dp := make([][][]int, k+1)
	for i := range dp {
		dp[i] = make([][]int, m+1)
		for j := range dp[i] {
			dp[i][j] = make([]int, n+1)
		}
	}

	// 预处理
	for i := m - 1; i >= 0; i-- {
		for j := n - 1; j >= 0; j-- {
			apples[i][j] = apples[i+1][j] + apples[i][j+1] - apples[i+1][j+1]
			if pizza[i][j] == 'A' {
				apples[i][j] += 1
			}
			if apples[i][j] > 0 {
				dp[1][i][j] = 1
			}
		}
	}

	for ki := 2; ki <= k; ki++ {
		for i := 0; i < m; i++ {
			for j := 0; j < n; j++ {
				// 水平方向切
				for i2 := i + 1; i2 < m; i2++ {
					if apples[i][j] > apples[i2][j] {
						dp[ki][i][j] = (dp[ki][i][j] + dp[ki-1][i2][j]) % mod
					}
				}
				// 垂直方向切
				for j2 := j + 1; j2 < n; j2++ {
					if apples[i][j] > apples[i][j2] {
						dp[ki][i][j] = (dp[ki][i][j] + dp[ki-1][i][j2]) % mod
					}
				}
			}
		}
	}
	return dp[k][0][0]
}
