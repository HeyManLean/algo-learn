package dynamicplan

import "testing"

func TestMinimumTotal(t *testing.T) {
	tests := []struct {
		name     string
		triangle [][]int
		want     int
	}{
		{
			name: "示例1",
			triangle: [][]int{
				{2},
				{3, 4},
				{6, 5, 7},
				{4, 1, 8, 3},
			},
			want: 11,
		},
		{
			name: "示例2",
			triangle: [][]int{
				{-10},
			},
			want: -10,
		},
		{
			name: "单行",
			triangle: [][]int{
				{5},
			},
			want: 5,
		},
		{
			name: "两行",
			triangle: [][]int{
				{1},
				{2, 3},
			},
			want: 3,
		},
		{
			name: "包含负数",
			triangle: [][]int{
				{-1},
				{2, 3},
				{1, -1, -3},
			},
			want: -1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := minimumTotal(tt.triangle); got != tt.want {
				t.Errorf("minimumTotal() = %v, want %v", got, tt.want)
			}
		})
	}
}
