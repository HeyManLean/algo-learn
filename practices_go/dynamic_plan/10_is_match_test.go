package dynamicplan

import (
	"testing"
)

func TestIsMatch(t *testing.T) {
	cases := []struct {
		name     string
		s        string
		p        string
		expected bool
	}{
		// 题目示例
		{
			name:     "示例1: s=aa, p=a",
			s:        "aa",
			p:        "a",
			expected: false,
		},
		{
			name:     "示例2: s=aa, p=a*",
			s:        "aa",
			p:        "a*",
			expected: true,
		},
		{
			name:     "示例3: s=ab, p=.*",
			s:        "ab",
			p:        ".*",
			expected: true,
		},
		// 基本匹配情况
		{
			name:     "单个字符匹配",
			s:        "a",
			p:        "a",
			expected: true,
		},
		{
			name:     "单个字符不匹配",
			s:        "a",
			p:        "b",
			expected: false,
		},
		{
			name:     "完全匹配",
			s:        "abc",
			p:        "abc",
			expected: true,
		},
		// 点号匹配
		{
			name:     "点号匹配单个字符",
			s:        "a",
			p:        ".",
			expected: true,
		},
		{
			name:     "点号匹配多个字符",
			s:        "ab",
			p:        "..",
			expected: true,
		},
		{
			name:     "点号在中间",
			s:        "abc",
			p:        "a.c",
			expected: true,
		},
		// 星号匹配
		{
			name:     "星号匹配0次",
			s:        "a",
			p:        "ab*",
			expected: true,
		},
		{
			name:     "星号匹配1次",
			s:        "ab",
			p:        "ab*",
			expected: true,
		},
		{
			name:     "星号匹配多次",
			s:        "abbb",
			p:        "ab*",
			expected: true,
		},
		{
			name:     "星号匹配0次的情况",
			s:        "a",
			p:        "aa*",
			expected: true,
		},
		{
			name:     "多个星号组合",
			s:        "aaa",
			p:        "a*a",
			expected: true,
		},
		// 点星组合
		{
			name:     "点星匹配任意字符",
			s:        "abc",
			p:        ".*",
			expected: true,
		},
		{
			name:     "点星匹配长字符串",
			s:        "abcdefgh",
			p:        ".*",
			expected: true,
		},
		{
			name:     "点号和星号匹配",
			s:        "abc",
			p:        ".*c",
			expected: true,
		},
		{
			name:     "点号和星号不匹配",
			s:        "ab",
			p:        ".*c",
			expected: false,
		},
		{
			name:     "多个点星",
			s:        "abcd",
			p:        "a.*b.*d",
			expected: true,
		},
		// 复杂情况
		{
			name:     "复杂情况1: s=aab, p=c*a*b",
			s:        "aab",
			p:        "c*a*b",
			expected: true,
		},
		{
			name:     "复杂情况2: s=mississippi, p=mis*is*p*.",
			s:        "mississippi",
			p:        "mis*is*p*.",
			expected: false,
		},
		{
			name:     "复杂情况3: s=mississippi, p=mis*is*ip*.",
			s:        "mississippi",
			p:        "mis*is*ip*.",
			expected: true,
		},
		{
			name:     "复杂情况4: 多个星号",
			s:        "a",
			p:        "a*b*c*",
			expected: true,
		},
		// 边界情况
		{
			name:     "模式比字符串长",
			s:        "a",
			p:        "ab",
			expected: false,
		},
		{
			name:     "字符串比模式长",
			s:        "aa",
			p:        "a",
			expected: false,
		},
		{
			name:     "星号匹配但字符不匹配",
			s:        "ab",
			p:        ".*c",
			expected: false,
		},
	}

	for _, tt := range cases {
		t.Run(tt.name, func(t *testing.T) {
			if res := isMatch(tt.s, tt.p); res != tt.expected {
				t.Errorf("isMatch(%q, %q) = %v, expected %v", tt.s, tt.p, res, tt.expected)
			}
		})
	}
}
