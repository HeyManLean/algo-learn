package bytedance

import (
	"testing"
)

func TestKInversePairs(t *testing.T) {
	tests := []struct {
		name     string
		n        int
		k        int
		expected int
	}{
		{
			name:     "示例1: n=3, k=0",
			n:        3,
			k:        0,
			expected: 1,
		},
		{
			name:     "示例2: n=3, k=1",
			n:        3,
			k:        1,
			expected: 2,
		},
		{
			name:     "边界测试: n=1, k=0",
			n:        1,
			k:        0,
			expected: 1,
		},
		{
			name:     "边界测试: n=1, k=1",
			n:        1,
			k:        1,
			expected: 0,
		},
		{
			name:     "测试: n=2, k=0",
			n:        2,
			k:        0,
			expected: 1,
		},
		{
			name:     "测试: n=2, k=1",
			n:        2,
			k:        1,
			expected: 1,
		},
		{
			name:     "测试: n=4, k=0",
			n:        4,
			k:        0,
			expected: 1,
		},
		{
			name:     "测试: n=4, k=1",
			n:        4,
			k:        1,
			expected: 3,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := kInversePairs(tt.n, tt.k)
			if result != tt.expected {
				t.Errorf("kInversePairs(%d, %d) = %d, expected %d", tt.n, tt.k, result, tt.expected)
			}
		})
	}
}
