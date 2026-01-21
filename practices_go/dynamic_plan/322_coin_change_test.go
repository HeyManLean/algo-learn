package dynamicplan

import "testing"

func TestCoinChange(t *testing.T) {
	tests := []struct {
		name   string
		coins  []int
		amount int
		expect int
	}{
		{
			name:   "示例1: coins=[1,2,5], amount=11",
			coins:  []int{1, 2, 5},
			amount: 11,
			expect: 3,
		},
		{
			name:   "示例2: coins=[2], amount=3",
			coins:  []int{2},
			amount: 3,
			expect: -1,
		},
		{
			name:   "示例3: coins=[1], amount=0",
			coins:  []int{1},
			amount: 0,
			expect: 0,
		},
		{
			name:   "示例4: coins=[1,16,17], amount=32",
			coins:  []int{1, 16, 17},
			amount: 32,
			expect: 2,
		},
		{
			name:   "边界情况: 单个硬币正好等于金额",
			coins:  []int{5},
			amount: 5,
			expect: 1,
		},
		{
			name:   "边界情况: 多个相同硬币",
			coins:  []int{1},
			amount: 5,
			expect: 5,
		},
		{
			name:   "边界情况: 无法凑成金额",
			coins:  []int{3, 5},
			amount: 4,
			expect: -1,
		},
		{
			name:   "复杂情况: 多种硬币组合",
			coins:  []int{1, 3, 4},
			amount: 6,
			expect: 2,
		},
		{
			name:   "复杂情况: 大金额",
			coins:  []int{1, 2, 5},
			amount: 100,
			expect: 20,
		},
		{
			name:   "边界情况: 金额为1",
			coins:  []int{1, 2, 5},
			amount: 1,
			expect: 1,
		},
		{
			name:   "边界情况: 硬币面额大于金额",
			coins:  []int{10, 20},
			amount: 5,
			expect: -1,
		},
		{
			name:   "复杂情况: 需要选择最优组合",
			coins:  []int{186, 419, 83, 408},
			amount: 6249,
			expect: 20,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := coinChange(tt.coins, tt.amount)
			if result != tt.expect {
				t.Errorf("coinChange(%v, %d) = %d, want %d",
					tt.coins, tt.amount, result, tt.expect)
			}
		})
	}
}
