package dynamicplan

import (
	"testing"
)

func TestNumDistinct(t *testing.T) {
	cases := []struct {
		name     string
		s        string
		t        string
		expected int
	}{
		{
			name:     "示例1",
			s:        "rabbbit",
			t:        "rabbit",
			expected: 3,
		},
		{
			name:     "示例2",
			s:        "babgbag",
			t:        "bag",
			expected: 5,
		},
		{
			name:     "完全匹配",
			s:        "abc",
			t:        "abc",
			expected: 1,
		},
		{
			name:     "单个字符匹配",
			s:        "aaa",
			t:        "a",
			expected: 3,
		},
		{
			name:     "无匹配",
			s:        "abc",
			t:        "def",
			expected: 0,
		},
		{
			name:     "s比t短",
			s:        "ab",
			t:        "abc",
			expected: 0,
		},
		{
			name:     "多个重复字符",
			s:        "aaaa",
			t:        "aa",
			expected: 6,
		},
		{
			name:     "复杂情况1",
			s:        "ddd",
			t:        "dd",
			expected: 3,
		},
		{
			name:     "复杂情况2",
			s:        "aabb",
			t:        "ab",
			expected: 4,
		},
		{
			name:     "复杂情况3",
			s:        "aabbaa",
			t:        "aba",
			expected: 8,
		},
	}

	for _, tt := range cases {
		t.Run(tt.name, func(t *testing.T) {
			if res := numDistinct(tt.s, tt.t); res != tt.expected {
				t.Errorf("numDistinct(%q, %q) = %d, expected %d", tt.s, tt.t, res, tt.expected)
			}
		})
	}
}
