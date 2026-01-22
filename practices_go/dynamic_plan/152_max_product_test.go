package dynamicplan

import "testing"

func TestMaxProduct(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		want int
	}{
		{
			name: "示例1: [2,3,-2,4]",
			nums: []int{2, 3, -2, 4},
			want: 6,
		},
		{
			name: "示例1: [-1,0,-2,2]",
			nums: []int{-1, 0, -2, 2},
			want: 2,
		},

		{
			name: "示例2: [-2,0,-1]",
			nums: []int{-2, 0, -1},
			want: 0,
		},
		{
			name: "单个正数",
			nums: []int{5},
			want: 5,
		},
		{
			name: "单个负数",
			nums: []int{-3},
			want: -3,
		},
		{
			name: "全为正数",
			nums: []int{1, 2, 3, 4},
			want: 24,
		},
		{
			name: "两个负数相乘",
			nums: []int{-2, -3},
			want: 6,
		},
		{
			name: "包含0的数组",
			nums: []int{0, 2},
			want: 2,
		},
		{
			name: "多个负数",
			nums: []int{-2, 3, -4},
			want: 24,
		},
		{
			name: "负数在中间",
			nums: []int{2, -5, -2, -4, 3},
			want: 24,
		},
		{
			name: "全为负数偶数个",
			nums: []int{-1, -2, -3, -4},
			want: 24,
		},
		{
			name: "全为负数奇数个",
			nums: []int{-1, -2, -3},
			want: 6,
		},
		{
			name: "包含多个0",
			nums: []int{-2, 0, -1, 0, 3, 4},
			want: 12,
		},
		{
			name: "单个0",
			nums: []int{0},
			want: 0,
		},
		{
			name: "复杂情况",
			nums: []int{2, -1, 1, 1},
			want: 2,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maxProduct(tt.nums); got != tt.want {
				t.Errorf("maxProduct() = %v, want %v", got, tt.want)
			}
		})
	}
}
