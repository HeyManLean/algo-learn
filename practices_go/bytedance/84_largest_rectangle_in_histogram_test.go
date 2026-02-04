package bytedance

import "testing"

func Test_largestRectangleArea(t *testing.T) {
	tests := []struct {
		name    string
		heights []int
		want    int
	}{
		{
			name:    "示例1",
			heights: []int{2, 1, 5, 6, 2, 3},
			want:    10,
		},
		{
			name:    "示例x",
			heights: []int{2, 1, 2},
			want:    3,
		},
		{
			name:    "示例y",
			heights: []int{0, 1, 0, 2, 0, 3, 0},
			want:    3,
		},
		{
			name:    "示例2",
			heights: []int{2, 4},
			want:    4,
		},
		{
			name:    "单个柱子",
			heights: []int{5},
			want:    5,
		},
		{
			name:    "递增序列",
			heights: []int{1, 2, 3, 4, 5},
			want:    9,
		},
		{
			name:    "递减序列",
			heights: []int{5, 4, 3, 2, 1},
			want:    9,
		},
		{
			name:    "全部相同高度",
			heights: []int{3, 3, 3, 3},
			want:    12,
		},
		{
			name:    "包含0高度",
			heights: []int{2, 0, 2},
			want:    2,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := largestRectangleArea(tt.heights); got != tt.want {
				t.Errorf("largestRectangleArea() = %v, want %v", got, tt.want)
			}
		})
	}
}
