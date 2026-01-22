package dynamicplan

func maximalSquare(matrix [][]byte) int {
	/*
		221. 最大正方形

		在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。

		输入：matrix = [
			["1","0","1","0","0"],
			["1","0","1","1","1"],
			["1","1","1","1","1"],
			["1","0","0","1","0"]
		]
		输出：4

		输入：matrix = [["0","1"],["1","0"]]
		输出：1

		输入：matrix = [["0"]]
		输出：0

		提示：
		m == matrix.length
		n == matrix[i].length
		1 <= m, n <= 300
		matrix[i][j] 为 '0' 或 '1'
	*/
	// dp[i][j] 表示最大正方形的边长
	// dp[i][j] 如果 matric[i][j] == '1', 判断上边，左边、右边 边长最小值 + 1， 否则为 1
	m := len(matrix)
	n := len(matrix[0])

	var min = func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}
	var max = func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	dp := make([][]int, m)
	for i := range dp {
		dp[i] = make([]int, n)
	}

	res := 0

	// 首列
	for i := 0; i < m; i++ {
		if matrix[i][0] == '1' {
			dp[i][0] = 1
			res = 1
		}
	}
	for j := 1; j < n; j++ {
		if matrix[0][j] == '1' {
			dp[0][j] = 1
			res = 1
		}
	}
	for i := 1; i < m; i++ {
		for j := 1; j < n; j++ {
			if matrix[i][j] != '1' {
				continue
			}
			dp[i][j] = 1 + min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1]))
			res = max(res, dp[i][j]*dp[i][j])
		}
	}
	return res
}
