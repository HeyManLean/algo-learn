package dynamicplan

func numDistinct(s string, t string) int {
	/*
		115. 不同的子序列
		给你两个字符串 s 和 t ，统计并返回在 s 的 子序列 中 t 出现的个数。

		输入：s = "rabbbit", t = "rabbit"
		输出：3

		输入：s = "babgbag", t = "bag"
		输出：5
	*/
	// 决策树:字符相等，选择匹配 s 当前字符，或者不匹配当前字符
	// 状态转移：当前字符相等 t[i] == s[j], 则 dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
	// 边界条件：t的第一个字符，如果在 s 内，累加个数
	m := len(t)
	n := len(s)

	dp := make([][]int, m+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
	}

	// hits := 0
	for j := 0; j < n+1; j++ {
		dp[0][j] = 1
	}

	for i := 1; i < m+1; i++ {
		for j := 1; j < n+1; j++ {
			if t[i-1] == s[j-1] {
				dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
			} else {
				dp[i][j] = dp[i][j-1]
			}
		}
	}

	return dp[m][n]

}

func numDistinctV2(s, t string) int {
	m, n := len(t), len(s)
	dp := make([][]int, m+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
	}

	// base case
	for j := 0; j <= n; j++ {
		dp[0][j] = 1
	}

	for i := 1; i <= m; i++ {
		for j := 1; j <= n; j++ {
			if t[i-1] == s[j-1] {
				dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
			} else {
				dp[i][j] = dp[i][j-1]
			}
		}
	}
	return dp[m][n]
}
