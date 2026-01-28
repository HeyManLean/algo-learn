package bytedance

import "testing"

func TestLengthOfLongestSubstringKDistinct(t *testing.T) {
	tests := []struct {
		name     string
		s        string
		k        int
		expected int
	}{
		{
			name:     "示例 1",
			s:        "eceba",
			k:        2,
			expected: 3,
		},
		{
			name:     "示例 2",
			s:        "aa",
			k:        1,
			expected: 2,
		},
		{
			name:     "空字符串",
			s:        "",
			k:        1,
			expected: 0,
		},
		{
			name:     "k=0",
			s:        "abc",
			k:        0,
			expected: 0,
		},
		{
			name:     "全部相同字符",
			s:        "aaaa",
			k:        1,
			expected: 4,
		},
		{
			name:     "k大于不同字符数",
			s:        "abc",
			k:        5,
			expected: 3,
		},
		{
			name:     "复杂情况",
			s:        "aabbcc",
			k:        2,
			expected: 4,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := lengthOfLongestSubstringKDistinct(tt.s, tt.k)
			if result != tt.expected {
				t.Errorf("lengthOfLongestSubstringKDistinct(%s, %d) = %d, want %d",
					tt.s, tt.k, result, tt.expected)
			}
		})
	}
}
