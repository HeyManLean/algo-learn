package bytedance

import (
	"testing"
)

func TestLongestConsecutive(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		expected int
	}{
		{
			name:     "示例 1",
			nums:     []int{100, 4, 200, 1, 3, 2},
			expected: 4,
		},
		{
			name:     "示例 2",
			nums:     []int{0, 3, 7, 2, 5, 8, 4, 6, 0, 1},
			expected: 9,
		},
		{
			name:     "空数组",
			nums:     []int{},
			expected: 0,
		},
		{
			name:     "单个元素",
			nums:     []int{1},
			expected: 1,
		},
		{
			name:     "无连续序列",
			nums:     []int{10, 20, 30, 40},
			expected: 1,
		},
		{
			name:     "全部连续",
			nums:     []int{1, 2, 3, 4, 5},
			expected: 5,
		},
		{
			name:     "包含重复元素",
			nums:     []int{1, 2, 0, 1},
			expected: 3,
		},
		{
			name:     "包含负数",
			nums:     []int{-1, 0, 1, 2},
			expected: 4,
		},
		{
			name:     "乱序且有间隔",
			nums:     []int{9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6},
			expected: 7,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := longestConsecutive(tt.nums)
			if result != tt.expected {
				t.Errorf("longestConsecutive(%v) = %d, expected %d", tt.nums, result, tt.expected)
			}
		})
	}
}
