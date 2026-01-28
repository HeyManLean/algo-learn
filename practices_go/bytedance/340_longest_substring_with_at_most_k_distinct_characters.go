package bytedance

func lengthOfLongestSubstringKDistinct(s string, k int) int {
	/*
		340. 至多包含 K 个不同字符的最长子串

		给定一个字符串 s 和一个整数 k，返回 至多包含 k 个不同字符的最长子串 的长度。

		子串必须是连续的。

		示例 1:
		输入: s = "eceba", k = 2
		输出: 3
		解释: 子串 "ece" 长度为 3。

		示例 2:
		输入: s = "aa", k = 1
		输出: 2
		解释: 子串 "aa" 长度为 2。

		提示:
		1 <= s.length <= 5 * 10^4
		0 <= k <= 50
	*/
	if k == 0 {
		return 0
	}
	// 滑动窗口
	// 使用map维护当前在窗口的字符及个数，如果map长度大于k，则左边收缩
	counter := make(map[byte]int)
	left := 0

	res := 0

	var max = func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	n := len(s)
	for right := 0; right < n; right++ {
		counter[s[right]] += 1

		for len(counter) > k {
			counter[s[left]] -= 1
			if counter[s[left]] == 0 {
				delete(counter, s[left])
			}
			left++
		}
		res = max(res, right-left+1)
	}
	return res
}
