package dynamicplan

import "testing"

func TestLongestCommonSubsequence(t *testing.T) {
	tests := []struct {
		name   string
		text1  string
		text2  string
		expect int
	}{
		{
			name:   "示例1: abcde 和 ace",
			text1:  "abcde",
			text2:  "ace",
			expect: 3,
		},
		{
			name:   "示例2: 相同字符串",
			text1:  "abc",
			text2:  "abc",
			expect: 3,
		},
		{
			name:   "示例3: 无公共子序列",
			text1:  "abc",
			text2:  "def",
			expect: 0,
		},
		{
			name:   "边界情况: 空字符串1",
			text1:  "",
			text2:  "abc",
			expect: 0,
		},
		{
			name:   "边界情况: 空字符串2",
			text1:  "abc",
			text2:  "",
			expect: 0,
		},
		{
			name:   "边界情况: 两个空字符串",
			text1:  "",
			text2:  "",
			expect: 0,
		},
		{
			name:   "单字符相同",
			text1:  "a",
			text2:  "a",
			expect: 1,
		},
		{
			name:   "单字符不同",
			text1:  "a",
			text2:  "b",
			expect: 0,
		},
		{
			name:   "复杂情况1",
			text1:  "abcdefgh",
			text2:  "aceg",
			expect: 4,
		},
		{
			name:   "复杂情况2",
			text1:  "oxcpqrsvwf",
			text2:  "shmtulqrypy",
			expect: 2,
		},
		{
			name:   "部分匹配",
			text1:  "abcde",
			text2:  "bcd",
			expect: 3,
		},
		{
			name:   "重复字符",
			text1:  "aabbcc",
			text2:  "abc",
			expect: 3,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := longestCommonSubsequence(tt.text1, tt.text2)
			if result != tt.expect {
				t.Errorf("longestCommonSubsequence(%q, %q) = %d, want %d",
					tt.text1, tt.text2, result, tt.expect)
			}
		})
	}
}
