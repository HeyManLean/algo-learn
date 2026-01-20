package dynamicplan

func longestPalindrome(s string) string {
	/*
		5. 最长回文子串

		给你一个字符串 s，找到 s 中最长的 回文 子串。

		输入：s = "babad"
		输出："bab"
		解释："aba" 同样是符合题意的答案。

		输入：s = "cbbd"
		输出："bb"

		输入：s="abbcccba"
		输出："bcccb

		提示：
		1 <= s.length <= 1000
		s 仅由数字和英文字母组成
	*/
	if len(s) == 0 {
		return ""
	}
	// dp[i] 表示以 i 字符结尾的最长回文子串
	n := len(s)
	dp := make([]int, n)
	dp[0] = 1

	memo := make([][]bool, n)
	for i := range memo {
		memo[i] = make([]bool, n)
	}

	var isPalind = func(start, end int) bool {
		if memo[start][end] {
			return true
		}
		for start < end {
			if s[start] != s[end] {
				memo[start][end] = false
				return false
			}
			start++
			end--
		}
		memo[start][end] = true
		return true
	}

	// i - dp[i-1] - 1 的长度前一个字符如果跟 s[i] 相等, 则为 dp[i-1] + 2, 否则判断 i-dp[i-1] ~ i 是否回文
	res := string(s[0])
	for i := 1; i < n; i++ {
		for j := 0; j < i; j++ {
			if isPalind(j, i) {
				dp[i] = i - j + 1
			}
			if dp[i] > len(res) {
				res = s[j : i+1]
			}
		}
	}
	return res

}
