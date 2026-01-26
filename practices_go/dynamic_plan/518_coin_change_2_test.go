package dynamicplan

import "testing"

func TestChange(t *testing.T) {
	tests := []struct {
		name   string
		amount int
		coins  []int
		want   int
	}{
		{
			name:   "示例 1",
			amount: 5,
			coins:  []int{1, 2, 5},
			want:   4,
		},
		{
			name:   "示例 2",
			amount: 3,
			coins:  []int{2},
			want:   0,
		},
		{
			name:   "示例 3",
			amount: 10,
			coins:  []int{10},
			want:   1,
		},
		{
			name:   "amount为0",
			amount: 0,
			coins:  []int{1, 2, 5},
			want:   1,
		},
		{
			name:   "多个硬币",
			amount: 6,
			coins:  []int{1, 2, 3},
			want:   7,
		},
		{
			name:   "无法凑成",
			amount: 7,
			coins:  []int{2, 4},
			want:   0,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := change(tt.amount, tt.coins); got != tt.want {
				t.Errorf("change() = %v, want %v", got, tt.want)
			}
		})
	}
}
