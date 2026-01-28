package bytedance

import "testing"

func TestMinWindow(t *testing.T) {
	tests := []struct {
		name     string
		s        string
		t        string
		expected string
	}{
		{
			name:     "示例 1 - 基本情况",
			s:        "ADOBECODEBANC",
			t:        "ABC",
			expected: "BANC",
		},
		{
			name:     "示例 2 - 单个字符",
			s:        "a",
			t:        "a",
			expected: "a",
		},
		{
			name:     "示例 3 - 无法覆盖",
			s:        "a",
			t:        "aa",
			expected: "",
		},
		{
			name:     "t 中有重复字符",
			s:        "aaaaaaaaaaaabbbbbcdd",
			t:        "abcdd",
			expected: "abbbbbcdd",
		},
		{
			name:     "整个字符串就是答案",
			s:        "abc",
			t:        "abc",
			expected: "abc",
		},
		{
			name:     "最小窗口在开头",
			s:        "ABCabc",
			t:        "ABC",
			expected: "ABC",
		},
		{
			name:     "最小窗口在结尾",
			s:        "abcABC",
			t:        "ABC",
			expected: "ABC",
		},
		{
			name:     "s 不包含 t",
			s:        "abc",
			t:        "xyz",
			expected: "",
		},
		{
			name:     "复杂情况 - 多个可能的窗口",
			s:        "ADOBECODEBANC",
			t:        "ABC",
			expected: "BANC",
		},
		{
			name:     "t 比 s 长",
			s:        "a",
			t:        "abc",
			expected: "",
		},
		{
			name:     "t 中字符全部相同",
			s:        "bbaac",
			t:        "aba",
			expected: "baa",
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := minWindow(tt.s, tt.t)
			if result != tt.expected {
				t.Errorf("minWindow(%q, %q) = %q, expected %q", tt.s, tt.t, result, tt.expected)
			}
		})
	}
}
