package bytedance

import "testing"

func Test_countRangeSum(t *testing.T) {
	tests := []struct {
		name  string
		nums  []int
		lower int
		upper int
		want  int
	}{
		{
			name:  "示例1: [-2,5,-1], lower=-2, upper=2",
			nums:  []int{-2, 5, -1},
			lower: -2,
			upper: 2,
			want:  3,
		},
		{
			name:  "示例2: [0], lower=0, upper=0",
			nums:  []int{0},
			lower: 0,
			upper: 0,
			want:  1,
		},
		{
			name:  "单元素在范围内",
			nums:  []int{5},
			lower: 3,
			upper: 7,
			want:  1,
		},
		{
			name:  "单元素不在范围内",
			nums:  []int{5},
			lower: 10,
			upper: 20,
			want:  0,
		},
		{
			name:  "两元素",
			nums:  []int{1, 2},
			lower: 1,
			upper: 3,
			want:  3,
		},
		{
			name:  "全为负数",
			nums:  []int{-3, -2, -1},
			lower: -5,
			upper: -1,
			want:  5,
		},
		{
			name:  "全为正数",
			nums:  []int{1, 2, 3},
			lower: 2,
			upper: 5,
			want:  4,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := countRangeSum(tt.nums, tt.lower, tt.upper); got != tt.want {
				t.Errorf("countRangeSum() = %v, want %v", got, tt.want)
			}
		})
	}
}
