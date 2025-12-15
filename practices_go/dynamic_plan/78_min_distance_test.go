package dynamicplan

import (
	"fmt"
	"testing"
)

func minDistance(word1 string, word2 string) int {
	/*
		72. 编辑距离
		给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。

		你可以对一个单词进行如下三种操作：
		插入一个字符
		删除一个字符
		替换一个字符

		输入：word1 = "horse", word2 = "ros"
		输出：3
		解释：
		horse -> rorse (将 'h' 替换为 'r')
		rorse -> rose (删除 'r')
		rose -> ros (删除 'e')

		输入：word1 = "intention", word2 = "execution"
		输出：5
		解释：
		intention -> inention (删除 't')
		inention -> enention (将 'i' 替换为 'e')
		enention -> exention (将 'n' 替换为 'x')
		exention -> exection (将 'n' 替换为 'c')
		exection -> execution (插入 'u')
	*/

	// w1, w2 执行两个单词最左侧，对比所在位置差异，
	// 如果相同则一起前进，否则分别考虑删除、替换、插入
	// 计算当前选择后的操作数+后续的操作数的最小值返回
	m := len(word1)
	n := len(word2)

	// dp[i][j] 表示 word1 前 i 个字符 和 word2 前 j 个字符 的最小操作数
	dp := make([][]int, m+1)
	for i := 0; i < m+1; i++ {
		dp[i] = make([]int, n+1)
		dp[i][0] = i
	}

	for j := 1; j < n+1; j++ {
		dp[0][j] = j
	}

	for i := 1; i < m+1; i++ {
		for j := 1; j < n+1; j++ {
			if word1[i-1] == word2[j-1] {
				dp[i][j] = dp[i-1][j-1]
			} else {
				// 替换 word1 i-1, 跟 word2 j-1 一样
				dp[i][j] = 1 + dp[i-1][j-1]
				// 删除 word1 i-1
				dp[i][j] = min(dp[i][j], 1+dp[i-1][j])
				// 添加 word1 i-1
				dp[i][j] = min(dp[i][j], 1+dp[i][j-1])
			}
		}
	}
	return dp[m][n]
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func TestMinDistance(t *testing.T) {
	res := minDistance("horse", "ros")
	if res != 3 {
		fmt.Println(res)
		t.Errorf("error, res=%d, expected=3", res)
	}
}
