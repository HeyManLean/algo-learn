package dynamicplan

import "testing"

func editDistance(s1 string, s2 string) int {
	/*
		输入两个字符串 s1 和 s2，返回将 转换为 所需的最少编辑步数。
		你可以在一个字符串中进行三种编辑操作：插入一个字符、删除一个字符、将字符替换为任意一个字符。
	*/
	// 动态规划判断：
	// 决策树？是
	// 求最值：是
	// 状态关联：是，前面位置最值 + 当前决策数，算出最值

	// 状态，dp
	// dp[i][j]  i 表示s1处理的长度，j 表示s2处理的长度， val是最小步数
	m := len(s1)
	n := len(s2)

	dp := make([][]int, m+1)
	for i := 0; i < m+1; i++ {
		dp[i] = make([]int, n+1)
	}

	// 边界条件
	// i=0 情况下，最小操作数为 j(插入)
	// j=0 情况下，最小操作数为 i(删除)

	for i := 1; i < m+1; i++ {
		dp[i][0] = i
	}
	for j := 1; j < n+1; j++ {
		dp[0][j] = j
	}

	for i := 1; i < m+1; i++ {
		for j := 1; j < n+1; j++ {
			// 状态转移
			// 如果当前字符相等，则不需要操作数，dp[i][j] = dp[i - 1][j - 1]
			if s1[i-1] == s2[j-1] {
				dp[i][j] = dp[i-1][j-1]
			} else {
				// 否则考虑删除 i：那只需要 i-1 和 j 的最小操作数 + 1
				dp[i][j] = dp[i-1][j] + 1
				// 考虑替换 i：需要 i-1 和 j-1 的最小操作数 + 1
				dp[i][j] = minInt(dp[i][j], dp[i-1][j-1]+1)

				// 考虑新增 i: 需要
				dp[i][j] = minInt(dp[i][j], dp[i][j-1]+1)
			}
		}
	}
	return dp[m][n]
}

func editDistanceV3(s1 string, s2 string) int {
	// 空间优化重写练习
	m := len(s1)
	n := len(s2)

	dp := make([]int, n+1)

	// 首行, s1 长度为0，操作数为 s2 的长度
	for j := 1; j < n+1; j++ {
		dp[j] = j
	}

	// dp[j] 表示 i 行处理完的j的结果，存储i行的结果，必须逐行处理

	for i := 1; i < m+1; i++ {
		leftUp := dp[0]

		// 边界条件
		dp[0] = i
		for j := 1; j < n+1; j++ {
			// 记录上一行的 j 位
			temp := dp[j]
			if s1[i-1] == s2[j-1] {
				// 字符相等不操作，等于左上角 dp[i-1,j-1]
				dp[j] = leftUp
			} else {
				dp[j] = minInt(leftUp, minInt(dp[j], dp[j-1])) + 1
			}
			leftUp = temp // 变成 i-1 j
		}
	}
	return dp[n]
}

func editDistanceV2(s1 string, s2 string) int {
	return editDistanceV3(s1, s2)
	// 空间优化
	m := len(s1)
	n := len(s2)
	dp := make([]int, n+1)

	// dp[i, j] 是有左上角、左边、上边来转换的，需要临时变量记录左上角的值

	// 第一行
	for j := 1; j < n+1; j++ {
		dp[j] = j
	}

	for i := 1; i < m+1; i++ {
		leftUp := dp[0] // 上一行  dp[i-1][0]
		dp[0] = i       // 当前行 dp[i][0]
		for j := 1; j < n+1; j++ {
			temp := dp[j] // 上一行 dp[i-1][j]
			if s1[i-1] == s2[j-1] {
				dp[j] = leftUp // dp[i-1,j-1]
			} else {
				// dp[i-1,j-1] dp[i-1,j] 是上一行数据
				// dp[j-1] = dp[i, j-1] 是当前行更新后的数据
				dp[j] = minInt(leftUp, minInt(dp[j], dp[j-1])) + 1
			}
			leftUp = temp // 左上角
		}
	}
	return dp[n]
}

func minInt(x int, y int) int {
	if x < y {
		return x
	}
	return y
}

func TestEditDistance(t *testing.T) {
	tests := []struct {
		name     string
		s1       string
		s2       string
		expected int
	}{
		{
			name:     "空字符串到空字符串",
			s1:       "",
			s2:       "",
			expected: 0,
		},
		{
			name:     "空字符串到非空字符串",
			s1:       "",
			s2:       "abc",
			expected: 3,
		},
		{
			name:     "非空字符串到空字符串",
			s1:       "abc",
			s2:       "",
			expected: 3,
		},
		{
			name:     "相同字符串",
			s1:       "abc",
			s2:       "abc",
			expected: 0,
		},
		{
			name:     "需要全部替换",
			s1:       "abc",
			s2:       "def",
			expected: 3,
		},
		{
			name:     "需要插入字符",
			s1:       "abc",
			s2:       "abcd",
			expected: 1,
		},
		{
			name:     "需要删除字符",
			s1:       "abcd",
			s2:       "abc",
			expected: 1,
		},
		{
			name:     "需要替换字符",
			s1:       "abc",
			s2:       "adc",
			expected: 1,
		},
		{
			name:     "混合操作 - 经典例子1",
			s1:       "horse",
			s2:       "ros",
			expected: 3,
		},
		{
			name:     "混合操作 - 经典例子2",
			s1:       "intention",
			s2:       "execution",
			expected: 5,
		},
		{
			name:     "单字符相同",
			s1:       "a",
			s2:       "a",
			expected: 0,
		},
		{
			name:     "单字符不同",
			s1:       "a",
			s2:       "b",
			expected: 1,
		},
		{
			name:     "需要多次插入",
			s1:       "a",
			s2:       "abcde",
			expected: 4,
		},
		{
			name:     "需要多次删除",
			s1:       "abcde",
			s2:       "a",
			expected: 4,
		},
		{
			name:     "部分匹配",
			s1:       "kitten",
			s2:       "sitting",
			expected: 3,
		},
		{
			name:     "包含重复字符",
			s1:       "aabbcc",
			s2:       "aabbdd",
			expected: 2,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := editDistance(tt.s1, tt.s2)
			if result != tt.expected {
				t.Errorf("editDistance(%q, %q) = %d, expected %d", tt.s1, tt.s2, result, tt.expected)
			}
		})
	}
	for _, tt := range tests {
		t.Run(tt.name+"v2", func(t *testing.T) {
			result := editDistanceV2(tt.s1, tt.s2)
			if result != tt.expected {
				t.Errorf("editDistanceV2(%q, %q) = %d, expected %d", tt.s1, tt.s2, result, tt.expected)
			}
		})
	}
}
