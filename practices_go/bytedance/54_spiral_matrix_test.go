package bytedance

import (
	"reflect"
	"testing"
)

func Test_spiralOrder(t *testing.T) {
	tests := []struct {
		name   string
		matrix [][]int
		want   []int
	}{
		{
			name:   "示例1: 3x3矩阵",
			matrix: [][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}},
			want:   []int{1, 2, 3, 6, 9, 8, 7, 4, 5},
		},
		{
			name:   "示例2: 3x4矩阵",
			matrix: [][]int{{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}},
			want:   []int{1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7},
		},
		{
			name:   "单行矩阵",
			matrix: [][]int{{1, 2, 3}},
			want:   []int{1, 2, 3},
		},
		{
			name:   "单列矩阵",
			matrix: [][]int{{1}, {2}, {3}},
			want:   []int{1, 2, 3},
		},
		{
			name:   "单个元素",
			matrix: [][]int{{42}},
			want:   []int{42},
		},
		{
			name:   "2x2矩阵",
			matrix: [][]int{{1, 2}, {3, 4}},
			want:   []int{1, 2, 4, 3},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := spiralOrder(tt.matrix); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("spiralOrder() = %v, want %v", got, tt.want)
			}
		})
	}
}
