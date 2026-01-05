package dynamicplan

func minInsertions(s string) int {
	/*
		1312. 让字符串成为回文串的最少插入次数
		给你一个字符串 s ，每一次操作你都可以在字符串的任意位置插入任意字符。
		请你返回让 s 成为回文串的 最少操作次数 。
		「回文串」是正读和反读都相同的字符串。

		输入：s = "zzazz"
		输出：0
		解释：字符串 "zzazz" 已经是回文串了，所以不需要做任何插入操作。

		输入：s = "mbadm"
		输出：2
		解释：字符串可变为 "mbdadbm" 或者 "mdbabdm" 。

		输入：s = "leetcode"
		输出：5
		解释：插入 5 个字符后字符串变为 "leetcodocteel" 。


		提示：
		1 <= s.length <= 500
		s 中所有字符都是小写字母。
	*/
	// 对于第 i 个字符，如果字符跟第一个字符相等，可以插入，或者不插入
	// 则前 i 个字符的回文子串是：dp[0][i] = min(dp[1][i-1], 1 + dp[0][i-1])
	// 否则 dp[0][i] = dp[0][i-1]

	// 最后返回 dp[0][n]

	// 要求出 dp[1][i-1] 还需要求 dp[2][i-1]，长的依赖短的
	// 可以按照长度来做遍历

	var min = func(x, y int) int {
		if x <= y {
			return x
		}
		return y
	}

	n := len(s)
	dp := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, n)
	}

	for length := 2; length <= n; length++ {
		for i := 0; i+length-1 < n; i++ {
			j := i + length - 1

			// 字符相等
			if s[i] == s[j] {
				dp[i][j] = dp[i+1][j-1]
			} else {
				// 不相等，往左或往右边插入数字
				dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])
			}
		}
	}
	return dp[0][n-1]
}
