package dynamicplan

func isMatchV2(s string, p string) bool {
	/*
		44. 通配符匹配

		给你一个输入字符串 (s) 和一个字符模式 (p) ，请你实现一个支持 '?' 和 '*' 匹配规则的通配符匹配：
		'?' 可以匹配任何单个字符。
		'*' 可以匹配任意字符序列（包括空字符序列）。
		判定匹配成功的充要条件是：字符模式必须能够 完全匹配 输入字符串（而不是部分匹配）。

		输入：s = "aa", p = "a"
		输出：false
		解释："a" 无法匹配 "aa" 整个字符串。

		输入：s = "aa", p = "*"
		输出：true
		解释：'*' 可以匹配任意字符串。

		输入：s = "cb", p = "?a"
		输出：false
		解释：'?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。

		0 <= s.length, p.length <= 2000
		s 仅由小写英文字母组成
		p 仅由小写英文字母、'?' 或 '*' 组成
	*/
	// * 表示0或任意字符串, 如果 p[j-1] 为 *, 则 dp[i][j] = dp[i-1][j]  # s往前， 否则判断是否相等或等于?
	// ? 表示一个任意字符
	m := len(s)
	n := len(p)
	dp := make([][]bool, m+1)
	for i := range dp {
		dp[i] = make([]bool, n+1)
	}
	dp[0][0] = true
	// s为空时
	for j := 1; j <= n; j++ {
		if p[j-1] == '*' {
			dp[0][j] = dp[0][j-1]
		}
	}

	for i := 1; i <= m; i++ {
		for j := 1; j <= n; j++ {
			if p[j-1] == '*' {
				// 匹配0次 || 匹配一次或多次
				dp[i][j] = dp[i][j-1] || dp[i-1][j]
			} else if s[i-1] == p[j-1] || p[j-1] == '?' {
				dp[i][j] = dp[i-1][j-1]
			}
		}
	}
	return dp[m][n]
}
