package dynamicplan

import (
	"testing"
)

func TestMaxCoins(t *testing.T) {
	cases := []struct {
		name     string
		nums     []int
		expected int
	}{
		{
			name:     "示例1 - 题目给出的标准答案",
			nums:     []int{3, 1, 5, 8},
			expected: 167,
		},
		{
			name:     "示例2 - 题目给出的标准答案",
			nums:     []int{1, 5},
			expected: 10,
		},
		{
			name:     "单个元素",
			nums:     []int{5},
			expected: 5,
		},
		{
			name:     "两个元素",
			nums:     []int{3, 1},
			expected: 6,
		},
		{
			name:     "三个元素",
			nums:     []int{1, 2, 3},
			expected: 12,
		},
		{
			name:     "全为1",
			nums:     []int{1, 1, 1},
			expected: 3,
		},
		{
			name:     "空数组",
			nums:     []int{},
			expected: 0,
		},
		{
			name:     "包含0的元素",
			nums:     []int{0, 1, 2},
			expected: 4,
		},
	}

	for _, tt := range cases {
		t.Run(tt.name, func(t *testing.T) {
			if res := maxCoins(tt.nums); res != tt.expected {
				t.Errorf("maxCoins(%v) = %d, expected %d", tt.nums, res, tt.expected)
			}
		})
	}
}
