package bytedance

import (
	"testing"
)

func TestFirstMissingPositive(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		expected int
	}{
		{
			name:     "示例 1",
			nums:     []int{1, 2, 0},
			expected: 3,
		},
		{
			name:     "示例 2",
			nums:     []int{3, 4, -1, 1},
			expected: 2,
		},
		{
			name:     "示例 3",
			nums:     []int{7, 8, 9, 11, 12},
			expected: 1,
		},
		{
			name:     "单个元素为1",
			nums:     []int{1},
			expected: 2,
		},
		{
			name:     "单个元素为2",
			nums:     []int{2},
			expected: 1,
		},
		{
			name:     "连续正数",
			nums:     []int{1, 2, 3, 4, 5},
			expected: 6,
		},
		{
			name:     "包含负数",
			nums:     []int{-1, -2, -3},
			expected: 1,
		},
		{
			name:     "空数组",
			nums:     []int{},
			expected: 1,
		},
		{
			name:     "乱序数组",
			nums:     []int{2, 1, 4, 3, 6, 5},
			expected: 7,
		},
		{
			name:     "包含重复元素",
			nums:     []int{1, 1, 2, 2, 3},
			expected: 4,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := firstMissingPositive(tt.nums)
			if result != tt.expected {
				t.Errorf("firstMissingPositive(%v) = %d, expected %d", tt.nums, result, tt.expected)
			}
		})
	}
}
