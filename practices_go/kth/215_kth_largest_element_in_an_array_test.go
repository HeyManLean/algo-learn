package bytedance

import (
	"testing"
)

func TestFindKthLargest(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		k    int
		want int
	}{
		{
			name: "示例1",
			nums: []int{3, 2, 1, 5, 6, 4},
			k:    2,
			want: 5,
		},
		{
			name: "示例2",
			nums: []int{3, 2, 3, 1, 2, 4, 5, 5, 6},
			k:    4,
			want: 4,
		},
		{
			name: "单个元素",
			nums: []int{1},
			k:    1,
			want: 1,
		},
		{
			name: "取最大",
			nums: []int{2, 1},
			k:    1,
			want: 2,
		},
		{
			name: "取最小",
			nums: []int{2, 1},
			k:    2,
			want: 1,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := findKthLargest(tt.nums, tt.k); got != tt.want {
				t.Errorf("findKthLargest() = %v, want %v", got, tt.want)
			}
		})
	}
}
