package dynamicplan

import "testing"

func TestSuperEggDrop(t *testing.T) {
	tests := []struct {
		name     string
		k        int
		n        int
		expected int
	}{
		{
			name:     "示例1: k=1, n=2",
			k:        1,
			n:        2,
			expected: 2,
		},
		{
			name:     "示例2: k=2, n=6",
			k:        2,
			n:        6,
			expected: 3,
		},
		{
			name:     "示例3: k=3, n=14",
			k:        3,
			n:        14,
			expected: 4,
		},
		{
			name:     "边界情况: k=1, n=1",
			k:        1,
			n:        1,
			expected: 1,
		},
		{
			name:     "边界情况: k=1, n=3",
			k:        1,
			n:        3,
			expected: 3,
		},
		{
			name:     "边界情况: k=2, n=1",
			k:        2,
			n:        1,
			expected: 1,
		},
		{
			name:     "边界情况: k=2, n=2",
			k:        2,
			n:        2,
			expected: 2,
		},
		{
			name:     "边界情况: k=2, n=3",
			k:        2,
			n:        3,
			expected: 2,
		},
		{
			name:     "测试用例: k=2, n=10",
			k:        2,
			n:        10,
			expected: 4,
		},
		{
			name:     "测试用例: k=3, n=1",
			k:        3,
			n:        1,
			expected: 1,
		},
		{
			name:     "测试用例: k=3, n=2",
			k:        3,
			n:        2,
			expected: 2,
		},
		{
			name:     "测试用例: k=4, n=10",
			k:        4,
			n:        10,
			expected: 4,
		},
		{
			name:     "测试用例: k=2, n=100",
			k:        2,
			n:        100,
			expected: 14,
		},
		{
			name:     "测试用例: k=5, n=1",
			k:        5,
			n:        1,
			expected: 1,
		},
		{
			name:     "测试用例: k=5, n=2",
			k:        5,
			n:        2,
			expected: 2,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := superEggDrop(tt.k, tt.n)
			if result != tt.expected {
				t.Errorf("superEggDrop(%d, %d) = %d, want %d", tt.k, tt.n, result, tt.expected)
			}
		})
	}
}
