package bytedance

import (
	"testing"
)

func TestGetPermutation(t *testing.T) {
	tests := []struct {
		name     string
		n        int
		k        int
		expected string
	}{
		{
			name:     "示例 1: n=3, k=3",
			n:        3,
			k:        3,
			expected: "213",
		},
		{
			name:     "示例 2: n=4, k=9",
			n:        4,
			k:        9,
			expected: "2314",
		},
		{
			name:     "示例 3: n=3, k=1",
			n:        3,
			k:        1,
			expected: "123",
		},
		{
			name:     "边界测试: n=1, k=1",
			n:        1,
			k:        1,
			expected: "1",
		},
		{
			name:     "边界测试: n=2, k=2",
			n:        2,
			k:        2,
			expected: "21",
		},
		{
			name:     "最大测试: n=9, k=1",
			n:        9,
			k:        1,
			expected: "123456789",
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := getPermutation(tt.n, tt.k)
			if result != tt.expected {
				t.Errorf("getPermutation(%d, %d) = %v, want %v", tt.n, tt.k, result, tt.expected)
			}
		})
	}
}
