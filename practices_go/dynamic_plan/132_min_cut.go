package dynamicplan

func minCut(s string) int {
	/*
		132. 分割回文串 II
		给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文串。

		返回符合要求的 最少分割次数 。

		输入：s = "aab"
		输出：1
		解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。

		输入：s = "a"
		输出：0

		输入：s = "ab"
		输出：1

		1 <= s.length <= 2000
		s 仅由小写英文字母组成
	*/
	var min = func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}
	n := len(s)

	pal := make([][]bool, n) // pal[i][j] 记录某个区间s[i:j+1]是否是回文子串
	for i := range pal {
		pal[i] = make([]bool, n)
	}

	// 初始化，如果s[i] == s[j], 判断 pal[i+1][j-1]，那么先遍历 i+1, j-1
	for i := n - 1; i >= 0; i-- {
		for j := i; j < n; j++ {
			if s[i] == s[j] && (j-i <= 2 || pal[i+1][j-1]) {
				pal[i][j] = true
			}
		}
	}

	// dp[i] 表示前 i 个字符最小分割次数，默认为字符个数
	dp := make([]int, n)
	for i := range dp {
		dp[i] = i
	}

	// 如果 0:i 是回文子串则 dp[i] 分割为0
	// 否则遍历期间，找到最小分割 min(dp[i], dp[j] + 1), if s[j+1:i] 是回文子串
	for i := 0; i < n; i++ {
		if pal[0][i] {
			dp[i] = 0
			continue
		}
		for j := 0; j < i; j++ {
			if pal[j+1][i] {
				dp[i] = min(dp[i], 1+dp[j])
			}
		}
	}
	return dp[n-1]

}
