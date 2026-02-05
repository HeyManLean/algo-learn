package bytedance

func longestIncreasingPath(matrix [][]int) int {
	/*
		329. 矩阵中的最长递增路径

		给定一个 m x n 的整数矩阵，找出其中最长递增路径的长度。
		对于每个单元格，你可以往上、下、左、右四个方向移动。不能在对角线方向上移动或移动到边界外。

		输入: matrix = [
			[9,9,4],
			[6,6,8],
			[2,1,1]
		]
		输出: 4
		解释: 最长递增路径为 [1, 2, 6, 9]。

		输入: matrix = [[3,4,5],[3,2,6],[2,2,1]]
		输出: 4
		解释: 最长递增路径是 [3, 4, 5, 6]。

		输入: matrix = [[1]]
		输出: 1

		m == matrix.length
		n == matrix[i].length
		1 <= m, n <= 200
		0 <= matrix[i][j] <= 2^31 - 1
	*/
	m := len(matrix)
	n := len(matrix[0])

	dp := make([][]int, m)
	for i := range dp {
		dp[i] = make([]int, n)
	}

	var max = func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	// dfs+dp
	var dfs func(i, j int) int
	dfs = func(i, j int) int {
		if i < 0 || i >= m || j < 0 || j >= n {
			return 0
		}
		if dp[i][j] > 0 {
			return dp[i][j]
		}
		// 找出四周比当前位置小，继续dfs
		dp[i][j] = 1
		if i > 0 && matrix[i][j] > matrix[i-1][j] {
			dp[i][j] = max(dp[i][j], 1+dfs(i-1, j))
		}
		if j > 0 && matrix[i][j] > matrix[i][j-1] {
			dp[i][j] = max(dp[i][j], 1+dfs(i, j-1))
		}
		if i < m-1 && matrix[i][j] > matrix[i+1][j] {
			dp[i][j] = max(dp[i][j], 1+dfs(i+1, j))
		}
		if j < n-1 && matrix[i][j] > matrix[i][j+1] {
			dp[i][j] = max(dp[i][j], 1+dfs(i, j+1))
		}
		return dp[i][j]
	}

	res := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			res = max(res, dfs(i, j))
		}
	}

	return res
}
