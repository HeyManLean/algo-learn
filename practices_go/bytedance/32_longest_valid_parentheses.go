package bytedance

func longestValidParentheses(s string) int {
	/*
		32. 最长有效括号

		给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

		示例 1：
		输入：s = "(()"
		输出：2
		解释：最长有效括号子串是 "()"

		示例 2：
		输入：s = ")()())"
		输出：4
		解释：最长有效括号子串是 "()()"

		示例 3：
		输入：s = ""
		输出：0

		0 <= s.length <= 3 * 10^4
		s[i] 为 '(' 或 ')'
	*/
	var max = func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	n := len(s)
	res := 0
	// 从左扫到右，遇到闭括号更多情况下，则重新数
	open, close := 0, 0
	for i := 0; i < n; i++ {
		if s[i] == '(' {
			open++
		} else {
			close++
		}
		if close > open {
			open, close = 0, 0
		} else if close == open {
			res = max(res, close*2)
		}
	}

	open, close = 0, 0
	for i := n - 1; i >= 0; i-- {
		if s[i] == '(' {
			open++
		} else {
			close++
		}
		if open > close {
			open, close = 0, 0
		} else if close == open {
			res = max(res, open*2)
		}
	}

	// 从右扫到左，遇到开括号更多的情况下，则重新数
	return res
}

func longestValidParenthesesStack(s string) int {
	// 栈方式，记录上一个开括号的位置索引，遇到闭括号，则移除栈顶，最长长度变为：当前索引-栈顶还没开括号索引
	// 如果栈为空，则将闭括号位置记录在栈顶，第一个认为是无效位置
	stack := []int{-1}
	res := 0

	var max = func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	for i, c := range s {
		if c == '(' {
			stack = append(stack, i)
			continue
		}
		stack = stack[:len(stack)-1] // 移除栈顶

		// 栈顶为空，表示没有开括号
		if len(stack) == 0 {
			stack = append(stack, i)
		} else {
			// 不为空
			res = max(res, i-stack[len(stack)-1])
		}
	}
	return res
}
