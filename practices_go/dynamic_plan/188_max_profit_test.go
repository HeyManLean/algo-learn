package dynamicplan

import "testing"

func TestMaxProfit4(t *testing.T) {
	tests := []struct {
		name     string
		k        int
		prices   []int
		expected int
	}{
		{
			name:     "示例1: k=2, prices=[2,4,1]",
			k:        2,
			prices:   []int{2, 4, 1},
			expected: 2,
		},
		{
			name:     "示例2: k=2, prices=[3,2,6,5,0,3]",
			k:        2,
			prices:   []int{3, 2, 6, 5, 0, 3},
			expected: 7,
		},
		{
			name:     "边界情况: k=0",
			k:        0,
			prices:   []int{1, 2, 3},
			expected: 0,
		},
		{
			name:     "边界情况: 单元素数组",
			k:        1,
			prices:   []int{5},
			expected: 0,
		},
		{
			name:     "k=1的情况",
			k:        1,
			prices:   []int{7, 1, 5, 3, 6, 4},
			expected: 5,
		},
		{
			name:     "k=3的情况",
			k:        3,
			prices:   []int{3, 3, 5, 0, 0, 3, 1, 4},
			expected: 8,
		},
		{
			name:     "价格一直下跌",
			k:        2,
			prices:   []int{7, 6, 4, 3, 1},
			expected: 0,
		},
		{
			name:     "价格一直上涨",
			k:        2,
			prices:   []int{1, 2, 3, 4, 5},
			expected: 4,
		},
		{
			name:     "k大于等于交易次数",
			k:        10,
			prices:   []int{1, 2, 3, 4, 5},
			expected: 4,
		},
		{
			name:     "复杂情况: k=2",
			k:        2,
			prices:   []int{1, 2, 4, 2, 5, 7, 2, 4, 9, 0},
			expected: 13,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := maxProfit4(tt.k, tt.prices)
			if result != tt.expected {
				t.Errorf("maxProfit4(%d, %v) = %d, expected %d", tt.k, tt.prices, result, tt.expected)
			}
		})
	}
}

func BenchmarkMaxProfit4(b *testing.B) {
	prices := []int{3, 2, 6, 5, 0, 3, 1, 4, 2, 5, 7, 2, 4, 9, 0, 1, 2, 3, 4, 5}
	k := 5
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		maxProfit4(k, prices)
	}
}
