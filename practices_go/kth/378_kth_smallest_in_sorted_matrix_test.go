package bytedance

import "testing"

func TestKthSmallest(t *testing.T) {
	tests := []struct {
		name   string
		matrix [][]int
		k      int
		want   int
	}{
		{
			name: "示例1",
			matrix: [][]int{
				{1, 5, 9},
				{10, 11, 13},
				{12, 13, 15},
			},
			k:    8,
			want: 13,
		},
		{
			name:   "示例2",
			matrix: [][]int{{-5}},
			k:      1,
			want:   -5,
		},
		{
			name: "2x2矩阵",
			matrix: [][]int{
				{1, 2},
				{3, 4},
			},
			k:    2,
			want: 2,
		},
		{
			name: "包含重复元素",
			matrix: [][]int{
				{1, 2, 3},
				{4, 5, 5},
				{6, 7, 8},
			},
			k:    5,
			want: 5,
		},
		{
			name: "第一个元素",
			matrix: [][]int{
				{1, 5, 9},
				{10, 11, 13},
				{12, 13, 15},
			},
			k:    1,
			want: 1,
		},
		{
			name: "最后一个元素",
			matrix: [][]int{
				{1, 5, 9},
				{10, 11, 13},
				{12, 13, 15},
			},
			k:    9,
			want: 15,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := kthSmallest(tt.matrix, tt.k)
			if got != tt.want {
				t.Errorf("kthSmallest() = %v, want %v", got, tt.want)
			}
		})
	}
}
