package practicesgo

import (
	"testing"
)

func lengthOfLongestSubstring(s string) int {
	/*https://leetcode.cn/problems/longest-substring-without-repeating-characters/

	无重复字符的最长子串：给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。

	输入: s = "abcabcbb"，输出: 3
	输入: s = "bbbbb"，输出: 1
	输入: s = "pwwkew"，输出: 3
	*/
	var (
		counter = make(map[byte]int)
		res     int
		slow    int
		fast    int
		n       int = len(s)
	)
	for fast < n {
		if _, ok := counter[s[fast]]; !ok {
			counter[s[fast]] = 0
		}
		counter[s[fast]] += 1

		for counter[s[fast]] > 1 {
			counter[s[slow]] -= 1
			slow += 1
		}

		fast += 1
		if fast-slow+1 > res {
			res = fast - slow
		}
	}

	return res

}

func TestLengthOfLongestSubstring(t *testing.T) {
	cases := []struct {
		S        string
		Expected int
	}{
		{"abcabcbb", 3},
		{"bbbbb", 1},
		{"pwwkew", 3},
	}
	for _, c := range cases {
		t.Run(c.S, func(t *testing.T) {
			if res := lengthOfLongestSubstring(c.S); res != c.Expected {
				t.Fatalf("str: %s expected: %d, but got %d", c.S, c.Expected, res)
			}
		})
	}
}
