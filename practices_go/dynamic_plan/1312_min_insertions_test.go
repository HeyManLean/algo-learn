package dynamicplan

import (
	"testing"
)

func TestMinInsertions(t *testing.T) {
	cases := []struct {
		name     string
		s        string
		expected int
	}{
		{
			name:     "示例1-已经是回文串",
			s:        "zzazz",
			expected: 0,
		},
		{
			name:     "示例2",
			s:        "mbadm",
			expected: 2,
		},
		{
			name:     "示例3",
			s:        "leetcode",
			expected: 5,
		},
		{
			name:     "单个字符",
			s:        "a",
			expected: 0,
		},
		{
			name:     "两个相同字符",
			s:        "aa",
			expected: 0,
		},
		{
			name:     "两个不同字符",
			s:        "ab",
			expected: 1,
		},
		{
			name:     "三个字符-回文",
			s:        "aba",
			expected: 0,
		},
		{
			name:     "三个字符-非回文",
			s:        "abc",
			expected: 2,
		},
		{
			name:     "四个字符-回文",
			s:        "abba",
			expected: 0,
		},
		{
			name:     "四个字符-非回文",
			s:        "abcd",
			expected: 3,
		},
		{
			name:     "重复字符",
			s:        "aaa",
			expected: 0,
		},
		{
			name:     "交替字符",
			s:        "abab",
			expected: 1,
		},
	}

	for _, tt := range cases {
		t.Run(tt.name, func(t *testing.T) {
			if res := minInsertions(tt.s); res != tt.expected {
				t.Errorf("minInsertions(%q) = %d, expected %d", tt.s, res, tt.expected)
			}
		})
	}
}
