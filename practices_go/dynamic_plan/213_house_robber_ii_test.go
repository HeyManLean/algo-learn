package dynamicplan

import "testing"

func TestRob(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		expected int
	}{
		{
			name:     "2, 2, 4, 3, 2, 5",
			nums:     []int{2, 2, 4, 3, 2, 5},
			expected: 10,
		},
		{
			name:     "示例 1",
			nums:     []int{2, 3, 2},
			expected: 3,
		},
		{
			name:     "示例 2",
			nums:     []int{1, 2, 3, 1},
			expected: 4,
		},
		{
			name:     "示例 3",
			nums:     []int{1, 2, 3},
			expected: 3,
		},
		{
			name:     "单个房屋",
			nums:     []int{5},
			expected: 5,
		},
		{
			name:     "两个房屋",
			nums:     []int{2, 3},
			expected: 3,
		},
		{
			name:     "四个房屋",
			nums:     []int{1, 3, 1, 3, 100},
			expected: 103,
		},
		{
			name:     "所有房屋金额相同",
			nums:     []int{2, 2, 2, 2},
			expected: 4,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := rob(tt.nums)
			if result != tt.expected {
				t.Errorf("rob(%v) = %d, expected %d", tt.nums, result, tt.expected)
			}
		})
	}
}
