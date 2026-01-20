package dynamicplan

import "testing"

func TestLengthOfLIS(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		expected int
	}{
		{
			name:     "示例1: [10,9,2,5,3,7,101,18]",
			nums:     []int{10, 9, 2, 5, 3, 7, 101, 18},
			expected: 4, // [2,3,7,101]
		},
		{
			name:     "示例2: [0,1,0,3,2,3]",
			nums:     []int{0, 1, 0, 3, 2, 3},
			expected: 4,
		},
		{
			name:     "示例3: 全相同元素 [7,7,7,7,7,7,7]",
			nums:     []int{7, 7, 7, 7, 7, 7, 7},
			expected: 1,
		},
		{
			name:     "单个元素",
			nums:     []int{5},
			expected: 1,
		},
		{
			name:     "严格递增序列",
			nums:     []int{1, 2, 3, 4, 5},
			expected: 5,
		},
		{
			name:     "严格递减序列",
			nums:     []int{5, 4, 3, 2, 1},
			expected: 1,
		},
		{
			name:     "两个元素递增",
			nums:     []int{1, 2},
			expected: 2,
		},
		{
			name:     "两个元素递减",
			nums:     []int{2, 1},
			expected: 1,
		},
		{
			name:     "含负数的序列",
			nums:     []int{-2, -1, 0, 1, 2},
			expected: 5,
		},
		{
			name:     "交替序列",
			nums:     []int{1, 3, 2, 4, 3, 5},
			expected: 4, // [1,2,3,5] or [1,2,4,5] or [1,3,4,5]
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := lengthOfLIS(tt.nums)
			if result != tt.expected {
				t.Errorf("lengthOfLIS(%v) = %d, want %d", tt.nums, result, tt.expected)
			}
		})
	}
}
