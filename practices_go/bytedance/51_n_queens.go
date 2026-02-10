package bytedance

import (
	"strings"
)

func solveNQueens(n int) [][]string {
	/*
		51. N 皇后

		按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
		n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
		给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
		每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

		示例 1：
		输入: n = 4
		输出: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
		解释: 如上图所示，4 皇后问题存在两个不同的解法。

		示例 2：
		输入: n = 1
		输出: [["Q"]]

		1 <= n <= 9
	*/
	var buildString = func(j int) string {
		b := &strings.Builder{}

		for t := 0; t < j; t++ {
			b.WriteByte('.')
		}
		b.WriteByte('Q')
		for t := j + 1; t < n; t++ {
			b.WriteByte('.')
		}
		return b.String()
	}

	// 回溯法
	col := make([]bool, n)
	ans := make([][]string, 0)
	tmp := make([]string, 0, n)
	var dfs func(i int) // 第i行，还剩k个
	dfs = func(i int) {
		if i == n {
			board := make([]string, n)
			copy(board, tmp)
			ans = append(ans, board)
			return
		}
		for j := 0; j < n; j++ {
			if col[j] {
				continue
			}
			// 左上和右上
			r := i - 1
			c := j - 1

			hasQ := false
			for r >= 0 && c >= 0 {
				if tmp[r][c] == 'Q' {
					hasQ = true
					break
				}
				r--
				c--
			}
			if hasQ {
				continue
			}

			r = i - 1
			c = j + 1
			hasQ = false
			for r >= 0 && c < n {
				if tmp[r][c] == 'Q' {
					hasQ = true
					break
				}
				r--
				c++
			}
			if hasQ {
				continue
			}

			col[j] = true
			tmp = append(tmp, buildString(j))
			dfs(i + 1)
			col[j] = false
			tmp = tmp[:len(tmp)-1]
		}
	}
	dfs(0)
	return ans
}
