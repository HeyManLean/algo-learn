package dynamicplan

import (
	"testing"
)

func longestValidParenthesesBest(s string) int {
	/*

		在此方法中，我们利用两个计数器 left 和 right 。首先，我们从左到右遍历字符串，
		对于遇到的每个 ‘(’，我们增加 left 计数器，对于遇到的每个 ‘)’ ，我们增加 right 计数器。
		每当 left 计数器与 right 计数器相等时，我们计算当前有效字符串的长度，并且记录目前为止找到的最长子字符串。
		当 right 计数器比 left 计数器大时，我们将 left 和 right 计数器同时变回 0。

		这样的做法贪心地考虑了以当前字符下标结尾的有效括号长度，每次当右括号数量多于左括号数量的时候之前的字符我们都扔掉不再考虑，
		重新从下一个字符开始计算，但这样会漏掉一种情况，就是遍历的时候左括号的数量始终大于右括号的数量，即 (() ，
		这种时候最长有效括号是求不出来的。

		解决的方法也很简单，我们只需要从右往左遍历用类似的方法计算即可，只是这个时候判断条件反了过来：

		当 left 计数器比 right 计数器大时，我们将 left 和 right 计数器同时变回 0
		当 left 计数器与 right 计数器相等时，我们计算当前有效字符串的长度，并且记录目前为止找到的最长子字符串
	*/
	left, right, maxLength := 0, 0, 0
	for i := 0; i < len(s); i++ {
		if s[i] == '(' {
			left++
		} else {
			right++
		}
		if left == right {
			maxLength = max(maxLength, 2*right)
		} else if right > left {
			left, right = 0, 0
		}
	}
	left, right = 0, 0
	for i := len(s) - 1; i >= 0; i-- {
		if s[i] == '(' {
			left++
		} else {
			right++
		}
		if left == right {
			maxLength = max(maxLength, 2*left)
		} else if left > right {
			left, right = 0, 0
		}
	}
	return maxLength
}

func longestValidParenthesesStack(s string) int {
	maxAns := 0
	stack := []int{}
	stack = append(stack, -1)
	for i := 0; i < len(s); i++ {
		if s[i] == '(' {
			stack = append(stack, i)
		} else {
			stack = stack[:len(stack)-1]
			if len(stack) == 0 {
				stack = append(stack, i)
			} else {
				maxAns = max(maxAns, i-stack[len(stack)-1])
			}
		}
	}
	return maxAns
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func longestValidParentheses(s string) int {
	/*
		32. 最长有效括号

		给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号 子串 的长度。
		左右括号匹配，即每个左括号都有对应的右括号将其闭合的字符串是格式正确的，比如 "(()())"。

		输入：s = "(()"
		输出：2

		输入：s = ")()())"
		输出：4

		输入：s = ""
		输出：0
	*/
	// 最长、子串：动态规划
	// i 位置和 i - 1 位置的关系，i 的数值依赖 i - 1 数值得出
	// dp[i] 表示包含 i 字符的子串长度
	// 如果字符为 ( ，则 dp[i] 为 0， 我们只考虑 ) 的情况
	// 如果 i-1 为 ( 则，...() ，否则 ...))
	n := len(s)
	dp := make([]int, n)
	result := 0

	for i := 1; i < n; i++ {
		if s[i] != ')' {
			continue
		}

		// 前一个字符为 (
		if s[i-1] == '(' {
			if i-2 >= 0 {
				dp[i] = dp[i-2] + 2
			} else {
				dp[i] = 2
			}
		} else {
			// 前一个字符为 )
			// 如果扣掉前一个字符的最长子串，再往前一个字符为 (, 则可以加 2，否则为0

			// (...)((...))
			if i-dp[i-1]-1 >= 0 && s[i-dp[i-1]-1] == '(' {
				// 往前一个字符前面还有字符，需要加上前面的子串
				if i-dp[i-1]-2 >= 0 {
					dp[i] = dp[i-dp[i-1]-2] + dp[i-1] + 2
				} else {
					dp[i] = dp[i-1] + 2
				}
			}
		}
		if dp[i] > result {
			result = dp[i]
		}
	}
	return result
}

func Test(t *testing.T) {
	cases := []struct {
		name     string
		s        string
		expected int
	}{
		{
			name:     "1",
			s:        "(()",
			expected: 2,
		},
		{
			name:     "2",
			s:        ")()())",
			expected: 4,
		},
		{
			name:     "3",
			s:        "",
			expected: 0,
		},
		{
			name:     "4",
			s:        "()(())",
			expected: 6,
		},
		{
			name:     "5",
			s:        ")))(((",
			expected: 0,
		},
	}
	for _, tt := range cases {
		t.Run(tt.name, func(t *testing.T) {
			if res := longestValidParenthesesBest(tt.s); res != tt.expected {
				t.Errorf("error, expected %d, got %d", tt.expected, res)
			}
		})
	}
}
