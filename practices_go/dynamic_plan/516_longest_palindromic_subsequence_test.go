package dynamicplan

import "testing"

func Test_longestPalindromeSubseq(t *testing.T) {
	tests := []struct {
		name string
		s    string
		want int
	}{
		{
			name: "示例1: bbbab",
			s:    "bbbab",
			want: 4,
		},
		{
			name: "示例2: cbbd",
			s:    "cbbd",
			want: 2,
		},
		{
			name: "单个字符",
			s:    "a",
			want: 1,
		},
		{
			name: "两个相同字符",
			s:    "aa",
			want: 2,
		},
		{
			name: "两个不同字符",
			s:    "ab",
			want: 1,
		},
		{
			name: "完全回文",
			s:    "racecar",
			want: 7,
		},
		{
			name: "无重复字符",
			s:    "abcdef",
			want: 1,
		},
		{
			name: "部分回文",
			s:    "aabaa",
			want: 5,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := longestPalindromeSubseq(tt.s); got != tt.want {
				t.Errorf("longestPalindromeSubseq() = %v, want %v", got, tt.want)
			}
		})
	}
}
