package bytedance

import "testing"

func TestPredictTheWinner(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		expected bool
	}{
		{
			name:     "示例 1",
			nums:     []int{1, 5, 2},
			expected: false,
		},
		{
			name:     "示例 2",
			nums:     []int{1, 5, 233, 7},
			expected: true,
		},
		{
			name:     "单个元素",
			nums:     []int{1},
			expected: true,
		},
		{
			name:     "两个元素相等",
			nums:     []int{1, 1},
			expected: true,
		},
		{
			name:     "两个元素不等",
			nums:     []int{1, 2},
			expected: true,
		},
		{
			name:     "三个元素玩家1胜",
			nums:     []int{1, 3, 1},
			expected: true,
		},
		{
			name:     "四个元素",
			nums:     []int{1, 2, 3, 4},
			expected: true,
		},
		{
			name:     "对称数组",
			nums:     []int{1, 2, 2, 1},
			expected: true,
		},
		{
			name:     "玩家1必输",
			nums:     []int{2, 4, 55, 6, 8},
			expected: false,
		},
		{
			name:     "全零",
			nums:     []int{0, 0, 0, 0},
			expected: true,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := PredictTheWinner(tt.nums)
			if result != tt.expected {
				t.Errorf("PredictTheWinner(%v) = %v, expected %v", tt.nums, result, tt.expected)
			}
		})
	}
}
