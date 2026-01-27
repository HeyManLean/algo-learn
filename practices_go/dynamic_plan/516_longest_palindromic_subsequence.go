package dynamicplan

func longestPalindromeSubseq(s string) int {
	/*
		516. 最长回文子序列

		给你一个字符串 s，找到其中最长的回文子序列，并返回该序列的长度。

		子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。

		注意：这是子序列而不是子字符串。子字符串要求连续，而子序列不需要连续。

		示例 1：
		输入: s = "bbbab"
		输出: 4
		解释: 一个可能的最长回文子序列为 "bbbb"

		示例 2：
		输入: s = "cbbd"
		输出: 2
		解释: 一个可能的最长回文子序列为 "bb"

		1 <= s.length <= 1000
		s 仅由小写英文字母组成
	*/
	// 如果子串长度为3时，判断首尾是否相等，相等，则为长度为1的子串+2
	// 如果子串长度为4时，首尾相等，则为长度为2的子串+2，否则等于长度为3的最长数值

	// dp[i][j] = dp[i+1][j-1] + 2 if s[i] == s[j] else max(dp[i+1][j], dp[i][j-1])
	// 按照长度

	n := len(s)
	if n <= 1 {
		return n
	}
	dp := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, n)
		dp[i][i] = 1
	}

	var max = func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	for length := 2; length <= n; length++ {
		for i := 0; i+length <= n; i++ {
			j := i + length - 1
			if s[i] == s[j] {
				dp[i][j] = dp[i+1][j-1] + 2
			} else {
				dp[i][j] = max(dp[i+1][j], dp[i][j-1])
			}
		}
	}

	return dp[0][n-1]
}
