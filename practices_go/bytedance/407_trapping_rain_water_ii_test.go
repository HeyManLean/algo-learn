package bytedance

import "testing"

func TestTrapRainWater(t *testing.T) {
	tests := []struct {
		name      string
		heightMap [][]int
		want      int
	}{
		{
			name: "示例1",
			heightMap: [][]int{
				{1, 4, 3, 1, 3, 2},
				{3, 2, 1, 3, 2, 4},
				{2, 3, 3, 2, 3, 1},
			},
			want: 4,
		},
		{
			name: "示例2",
			heightMap: [][]int{
				{3, 3, 3, 3, 3},
				{3, 2, 2, 2, 3},
				{3, 2, 1, 2, 3},
				{3, 2, 2, 2, 3},
				{3, 3, 3, 3, 3},
			},
			want: 10,
		},
		{
			name: "单行",
			heightMap: [][]int{
				{1, 2, 3, 2, 1},
			},
			want: 0,
		},
		{
			name: "单列",
			heightMap: [][]int{
				{1},
				{2},
				{3},
				{2},
				{1},
			},
			want: 0,
		},
		{
			name: "全相同高度",
			heightMap: [][]int{
				{5, 5, 5},
				{5, 5, 5},
				{5, 5, 5},
			},
			want: 0,
		},
		{
			name: "边界高中间低",
			heightMap: [][]int{
				{5, 5, 5, 5},
				{5, 1, 1, 5},
				{5, 5, 5, 5},
			},
			want: 8,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := trapRainWater(tt.heightMap); got != tt.want {
				t.Errorf("trapRainWater() = %v, want %v", got, tt.want)
			}
		})
	}
}
