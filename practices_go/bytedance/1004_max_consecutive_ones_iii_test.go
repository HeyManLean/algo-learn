package bytedance

import "testing"

func Test_longestOnes(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		k    int
		want int
	}{
		{
			name: "示例1: [1,1,1,0,0,0,1,1,1,1,0] k=2",
			nums: []int{1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0},
			k:    2,
			want: 6,
		},
		{
			name: "示例2: [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1] k=3",
			nums: []int{0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1},
			k:    3,
			want: 10,
		},
		{
			name: "全1数组",
			nums: []int{1, 1, 1, 1, 1},
			k:    0,
			want: 5,
		},
		{
			name: "全0数组 k足够",
			nums: []int{0, 0, 0},
			k:    3,
			want: 3,
		},
		{
			name: "全0数组 k不足",
			nums: []int{0, 0, 0},
			k:    1,
			want: 1,
		},
		{
			name: "k为0 中间有0",
			nums: []int{1, 1, 0, 1, 1},
			k:    0,
			want: 2,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := longestOnes(tt.nums, tt.k); got != tt.want {
				t.Errorf("longestOnes(%v, %v) = %v, want %v", tt.nums, tt.k, got, tt.want)
			}
		})
	}
}
