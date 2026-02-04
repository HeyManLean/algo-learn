package bytedance

import (
	"testing"
)

func TestMaximumGap(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		want int
	}{
		{
			name: "示例1",
			nums: []int{3, 6, 9, 1},
			want: 3,
		},
		{
			name: "示例2-少于2个元素",
			nums: []int{10},
			want: 0,
		},
		{
			name: "空数组",
			nums: []int{},
			want: 0,
		},
		{
			name: "两元素",
			nums: []int{1, 5},
			want: 4,
		},
		{
			name: "两元素相等",
			nums: []int{2, 2},
			want: 0,
		},
		{
			name: "升序相邻差1",
			nums: []int{1, 2, 3, 4},
			want: 1,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maximumGap(tt.nums); got != tt.want {
				t.Errorf("maximumGap() = %v, want %v", got, tt.want)
			}
		})
	}
}
