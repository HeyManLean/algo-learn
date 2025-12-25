package dynamicplan

import (
	"testing"
)

func TestSplitArray(t *testing.T) {
	cases := []struct {
		name     string
		nums     []int
		k        int
		expected int
	}{
		{
			name:     "示例1",
			nums:     []int{7, 2, 5, 10, 8},
			k:        2,
			expected: 18,
		},
		{
			name:     "示例2",
			nums:     []int{1, 2, 3, 4, 5},
			k:        2,
			expected: 9,
		},
		{
			name:     "示例3",
			nums:     []int{1, 4, 4},
			k:        3,
			expected: 4,
		},
		{
			name:     "k=1，整个数组",
			nums:     []int{7, 2, 5, 10, 8},
			k:        1,
			expected: 32,
		},
		{
			name:     "k等于数组长度，每个元素一个子数组",
			nums:     []int{1, 2, 3, 4, 5},
			k:        5,
			expected: 5,
		},
		{
			name:     "单个元素",
			nums:     []int{1},
			k:        1,
			expected: 1,
		},
		{
			name:     "两个元素k=2",
			nums:     []int{1, 2},
			k:        2,
			expected: 2,
		},
		{
			name:     "所有元素相同",
			nums:     []int{3, 3, 3, 3},
			k:        2,
			expected: 6,
		},
		{
			name:     "包含0",
			nums:     []int{1, 0, 2, 3, 0, 4},
			k:        2,
			expected: 6,
		},
	}

	for _, tt := range cases {
		t.Run(tt.name, func(t *testing.T) {
			if res := splitArray(tt.nums, tt.k); res != tt.expected {
				t.Errorf("splitArray(%v, %d) = %d, expected %d", tt.nums, tt.k, res, tt.expected)
			}
		})
	}
}

func TestSplitArrayV2(t *testing.T) {
	cases := []struct {
		name     string
		nums     []int
		m        int
		expected int
	}{
		{
			name:     "示例1",
			nums:     []int{7, 2, 5, 10, 8},
			m:        2,
			expected: 18,
		},
		{
			name:     "示例2",
			nums:     []int{1, 2, 3, 4, 5},
			m:        2,
			expected: 9,
		},
		{
			name:     "示例3",
			nums:     []int{1, 4, 4},
			m:        3,
			expected: 4,
		},
		{
			name:     "m=1，整个数组",
			nums:     []int{7, 2, 5, 10, 8},
			m:        1,
			expected: 32,
		},
		{
			name:     "m等于数组长度，每个元素一个子数组",
			nums:     []int{1, 2, 3, 4, 5},
			m:        5,
			expected: 5,
		},
		{
			name:     "单个元素",
			nums:     []int{1},
			m:        1,
			expected: 1,
		},
		{
			name:     "两个元素m=2",
			nums:     []int{1, 2},
			m:        2,
			expected: 2,
		},
		{
			name:     "所有元素相同",
			nums:     []int{3, 3, 3, 3},
			m:        2,
			expected: 6,
		},
		{
			name:     "递增序列",
			nums:     []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
			m:        3,
			expected: 20,
		},
		{
			name:     "递减序列",
			nums:     []int{10, 9, 8, 7, 6, 5, 4, 3, 2, 1},
			m:        3,
			expected: 20,
		},
		{
			name:     "包含0",
			nums:     []int{1, 0, 2, 3, 0, 4},
			m:        2,
			expected: 6,
		},
		{
			name:     "较大值在中间",
			nums:     []int{1, 2, 3, 10, 1, 2, 3},
			m:        2,
			expected: 12,
		},
	}

	for _, tt := range cases {
		t.Run(tt.name, func(t *testing.T) {
			if res := splitArrayV2(tt.nums, tt.m); res != tt.expected {
				t.Errorf("splitArrayV2(%v, %d) = %d, expected %d", tt.nums, tt.m, res, tt.expected)
			}
		})
	}
}
