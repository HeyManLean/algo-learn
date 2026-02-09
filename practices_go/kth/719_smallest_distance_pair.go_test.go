package bytedance

import (
	"testing"
)

func TestSmallestDistancePair(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		k        int
		expected int
	}{
		{
			name:     "示例 1",
			nums:     []int{1, 3, 1},
			k:        1,
			expected: 0,
		},
		{
			name:     "示例 2",
			nums:     []int{1, 1, 1},
			k:        2,
			expected: 0,
		},
		{
			name:     "示例 3",
			nums:     []int{1, 6, 1},
			k:        3,
			expected: 5,
		},
		{
			name:     "测试用例 4",
			nums:     []int{1, 3, 1, 5},
			k:        1,
			expected: 0,
		},
		{
			name:     "测试用例 5",
			nums:     []int{1, 3, 1, 5},
			k:        2,
			expected: 2,
		},
		{
			name:     "测试用例 6 - 较大数组",
			nums:     []int{9, 10, 7, 10, 6, 1, 5, 4, 9, 8},
			k:        18,
			expected: 2,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := smallestDistancePair(tt.nums, tt.k)
			if result != tt.expected {
				t.Errorf("smallestDistancePair(%v, %d) = %d, expected %d",
					tt.nums, tt.k, result, tt.expected)
			}
		})
	}
}
