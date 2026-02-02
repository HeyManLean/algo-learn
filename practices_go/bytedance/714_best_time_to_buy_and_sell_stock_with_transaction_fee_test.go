package bytedance

import (
	"testing"
)

func TestMaxProfit(t *testing.T) {
	tests := []struct {
		name   string
		prices []int
		fee    int
		want   int
	}{
		{
			name:   "示例1",
			prices: []int{1, 3, 2, 8, 4, 9},
			fee:    2,
			want:   8,
		},
		{
			name:   "示例2",
			prices: []int{1, 3, 7, 5, 10, 3},
			fee:    3,
			want:   6,
		},
		{
			name:   "单日无交易",
			prices: []int{1},
			fee:    0,
			want:   0,
		},
		{
			name:   "两日下跌",
			prices: []int{3, 1},
			fee:    1,
			want:   0,
		},
		{
			name:   "两日上涨",
			prices: []int{1, 4},
			fee:    2,
			want:   1,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maxProfit(tt.prices, tt.fee); got != tt.want {
				t.Errorf("maxProfit() = %v, want %v", got, tt.want)
			}
		})
	}
}
