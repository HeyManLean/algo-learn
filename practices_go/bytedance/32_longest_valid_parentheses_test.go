package bytedance

import "testing"

func TestLongestValidParentheses(t *testing.T) {
	tests := []struct {
		name     string
		s        string
		expected int
	}{
		{
			name:     "示例 1",
			s:        "(()",
			expected: 2,
		},
		{
			name:     "示例 2",
			s:        ")()())",
			expected: 4,
		},
		{
			name:     "示例 3",
			s:        "",
			expected: 0,
		},
		{
			name:     "单个左括号",
			s:        "(",
			expected: 0,
		},
		{
			name:     "单个右括号",
			s:        ")",
			expected: 0,
		},
		{
			name:     "完全匹配",
			s:        "()()",
			expected: 4,
		},
		{
			name:     "嵌套括号",
			s:        "((()))",
			expected: 6,
		},
		{
			name:     "混合情况",
			s:        "()(()",
			expected: 2,
		},
		{
			name:     "连续匹配",
			s:        "()(())",
			expected: 6,
		},
		{
			name:     "开头不匹配",
			s:        "))()()",
			expected: 4,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := longestValidParentheses(tt.s)
			if result != tt.expected {
				t.Errorf("longestValidParentheses(%q) = %d, expected %d", tt.s, result, tt.expected)
			}
		})
	}
}
