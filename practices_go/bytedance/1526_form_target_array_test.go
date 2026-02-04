package bytedance

import (
	"testing"
)

func TestMinNumberOperations(t *testing.T) {
	tests := []struct {
		name   string
		target []int
		want   int
	}{
		{
			name:   "示例1",
			target: []int{1, 2, 3, 2, 1},
			want:   3,
		},
		{
			name:   "示例2",
			target: []int{3, 1, 1, 2},
			want:   4,
		},
		{
			name:   "示例3",
			target: []int{3, 1, 5, 4, 2},
			want:   7,
		},
		{
			name:   "单元素",
			target: []int{5},
			want:   5,
		},
		{
			name:   "两元素递增",
			target: []int{1, 2},
			want:   2,
		},
		{
			name:   "两元素递减",
			target: []int{2, 1},
			want:   2,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := minNumberOperations(tt.target); got != tt.want {
				t.Errorf("minNumberOperations() = %v, want %v", got, tt.want)
			}
		})
	}
}
