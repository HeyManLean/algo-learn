package dynamicplan

import (
	"testing"
)

func TestIsMatchV2(t *testing.T) {
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
			name:     "示例2: s=aa, p=*",
			s:        "aa",
			p:        "*",
			expected: true,
		},
		{
			name:     "示例3: s=cb, p=?a",
			s:        "cb",
			p:        "?a",
			expected: false,
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
		{
			name:     "字符串比模式长",
			s:        "aa",
			p:        "a",
			expected: false,
		},
		{
			name:     "模式比字符串长",
			s:        "a",
			p:        "ab",
			expected: false,
		},
		// 问号匹配
		{
			name:     "问号匹配单个字符",
			s:        "a",
			p:        "?",
			expected: true,
		},
		{
			name:     "问号匹配多个字符",
			s:        "ab",
			p:        "??",
			expected: true,
		},
		{
			name:     "问号在中间",
			s:        "abc",
			p:        "a?c",
			expected: true,
		},
		{
			name:     "问号在开头",
			s:        "abc",
			p:        "?bc",
			expected: true,
		},
		{
			name:     "问号在结尾",
			s:        "abc",
			p:        "ab?",
			expected: true,
		},
		{
			name:     "多个问号",
			s:        "abcd",
			p:        "a??d",
			expected: true,
		},
		// 星号匹配
		{
			name:     "星号匹配空字符串",
			s:        "",
			p:        "*",
			expected: true,
		},
		{
			name:     "星号匹配任意字符串",
			s:        "abc",
			p:        "*",
			expected: true,
		},
		{
			name:     "星号匹配长字符串",
			s:        "abcdefghijklmnopqrstuvwxyz",
			p:        "*",
			expected: true,
		},
		{
			name:     "星号在开头",
			s:        "abc",
			p:        "*c",
			expected: true,
		},
		{
			name:     "星号在中间",
			s:        "abc",
			p:        "a*c",
			expected: true,
		},
		{
			name:     "星号在结尾",
			s:        "abc",
			p:        "a*",
			expected: true,
		},
		{
			name:     "星号匹配多个字符",
			s:        "abcd",
			p:        "a*d",
			expected: true,
		},
		{
			name:     "星号匹配单个字符",
			s:        "abc",
			p:        "a*c",
			expected: true,
		},
		{
			name:     "星号匹配0个字符",
			s:        "ac",
			p:        "a*c",
			expected: true,
		},
		{
			name:     "多个星号",
			s:        "abc",
			p:        "*b*",
			expected: true,
		},
		{
			name:     "连续星号",
			s:        "abc",
			p:        "a**c",
			expected: true,
		},
		// 问号和星号组合
		{
			name:     "问号和星号组合1",
			s:        "abc",
			p:        "a?*",
			expected: true,
		},
		{
			name:     "问号和星号组合2",
			s:        "abc",
			p:        "*?c",
			expected: true,
		},
		{
			name:     "问号和星号组合3",
			s:        "abcd",
			p:        "a?*d",
			expected: true,
		},
		{
			name:     "问号和星号组合4",
			s:        "abc",
			p:        "?*c",
			expected: true,
		},
		// 复杂情况
		{
			name:     "复杂情况1: 多个问号和星号",
			s:        "abcd",
			p:        "a?*?d",
			expected: true,
		},
		{
			name:     "复杂情况2: 星号后跟问号",
			s:        "abc",
			p:        "*?",
			expected: true,
		},
		{
			name:     "复杂情况3: 问号后跟星号",
			s:        "abc",
			p:        "?*",
			expected: true,
		},
		{
			name:     "复杂情况4: 长字符串匹配",
			s:        "abcdefghijklmnopqrstuvwxyz",
			p:        "a*z",
			expected: true,
		},
		{
			name:     "复杂情况5: 中间匹配",
			s:        "abcdefghijklmnopqrstuvwxyz",
			p:        "a?c*xyz",
			expected: true,
		},
		// 不匹配的情况
		{
			name:     "字符不匹配",
			s:        "abc",
			p:        "abd",
			expected: false,
		},
		{
			name:     "问号位置不匹配",
			s:        "abc",
			p:        "a?d",
			expected: false,
		},
		{
			name:     "星号后字符不匹配",
			s:        "abc",
			p:        "a*d",
			expected: false,
		},
		{
			name:     "模式太短",
			s:        "abc",
			p:        "ab",
			expected: false,
		},
		{
			name:     "模式太长",
			s:        "ab",
			p:        "abc",
			expected: false,
		},
		// 边界情况
		{
			name:     "空字符串匹配空模式",
			s:        "",
			p:        "",
			expected: true,
		},
		{
			name:     "空字符串匹配星号",
			s:        "",
			p:        "*",
			expected: true,
		},
		{
			name:     "空字符串匹配多个星号",
			s:        "",
			p:        "***",
			expected: true,
		},
		{
			name:     "空字符串不匹配问号",
			s:        "",
			p:        "?",
			expected: false,
		},
		{
			name:     "空字符串不匹配字符",
			s:        "",
			p:        "a",
			expected: false,
		},
		{
			name:     "单个字符匹配问号",
			s:        "a",
			p:        "?",
			expected: true,
		},
		{
			name:     "单个字符匹配星号",
			s:        "a",
			p:        "*",
			expected: true,
		},
		{
			name:     "星号匹配整个字符串",
			s:        "hello",
			p:        "*",
			expected: true,
		},
		{
			name:     "问号匹配整个字符串",
			s:        "hello",
			p:        "?????",
			expected: true,
		},
		{
			name:     "问号数量不匹配",
			s:        "hello",
			p:        "????",
			expected: false,
		},
		{
			name:     "星号和问号混合1",
			s:        "abc",
			p:        "a*?",
			expected: true,
		},
		{
			name:     "星号和问号混合2",
			s:        "abc",
			p:        "*?c",
			expected: true,
		},
		{
			name:     "星号和问号混合3",
			s:        "abcd",
			p:        "a*?d",
			expected: true,
		},
	}

	for _, tt := range cases {
		t.Run(tt.name, func(t *testing.T) {
			if res := isMatchV2(tt.s, tt.p); res != tt.expected {
				t.Errorf("isMatchV2(%q, %q) = %v, expected %v", tt.s, tt.p, res, tt.expected)
			}
		})
	}
}
