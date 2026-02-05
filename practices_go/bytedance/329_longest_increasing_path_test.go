package bytedance

import "testing"

func Test_longestIncreasingPath(t *testing.T) {
	tests := []struct {
		name   string
		matrix [][]int
		want   int
	}{
		{
			name:   "示例1: [[9,9,4],[6,6,8],[2,1,1]]",
			matrix: [][]int{{9, 9, 4}, {6, 6, 8}, {2, 1, 1}},
			want:   4,
		},
		{
			name:   "示例2: [[3,4,5],[3,2,6],[2,2,1]]",
			matrix: [][]int{{3, 4, 5}, {3, 2, 6}, {2, 2, 1}},
			want:   4,
		},
		{
			name:   "示例3: 单元素 [[1]]",
			matrix: [][]int{{1}},
			want:   1,
		},

		{
			name: "测试用例",
			matrix: [][]int{
				{7, 8, 9},
				{9, 7, 6},
				{7, 2, 3},
			},
			want: 6,
		},
		{
			name:   "单行递增",
			matrix: [][]int{{1, 2, 3, 4, 5}},
			want:   5,
		},
		{
			name:   "单行递减",
			matrix: [][]int{{5, 4, 3, 2, 1}},
			want:   5,
		},
		{
			name:   "单列递增",
			matrix: [][]int{{1}, {2}, {3}, {4}},
			want:   4,
		},
		{
			name:   "全部相同",
			matrix: [][]int{{2, 2}, {2, 2}},
			want:   1,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := longestIncreasingPath(tt.matrix); got != tt.want {
				t.Errorf("longestIncreasingPath() = %v, want %v", got, tt.want)
			}
		})
	}
}
