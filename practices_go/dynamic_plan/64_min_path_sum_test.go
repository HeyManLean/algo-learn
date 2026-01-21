package dynamicplan

import "testing"

func TestMinPathSum(t *testing.T) {
	tests := []struct {
		name   string
		grid   [][]int
		expect int
	}{
		{
			name: "示例1: [[1,3,1],[1,5,1],[4,2,1]]",
			grid: [][]int{
				{1, 3, 1},
				{1, 5, 1},
				{4, 2, 1},
			},
			expect: 7,
		},
		{
			name: "示例2: [[1,2,3],[4,5,6]]",
			grid: [][]int{
				{1, 2, 3},
				{4, 5, 6},
			},
			expect: 12,
		},
		{
			name:   "边界情况: 1x1网格",
			grid:   [][]int{{5}},
			expect: 5,
		},
		{
			name: "边界情况: 单行网格",
			grid: [][]int{
				{1, 2, 3, 4, 5},
			},
			expect: 15,
		},
		{
			name: "边界情况: 单列网格",
			grid: [][]int{
				{1},
				{2},
				{3},
				{4},
			},
			expect: 10,
		},
		{
			name: "边界情况: 2x2网格",
			grid: [][]int{
				{1, 2},
				{3, 4},
			},
			expect: 7,
		},
		{
			name: "复杂情况: 3x3网格",
			grid: [][]int{
				{1, 2, 3},
				{4, 5, 6},
				{7, 8, 9},
			},
			expect: 21,
		},
		{
			name: "复杂情况: 包含0的网格",
			grid: [][]int{
				{1, 0, 1},
				{0, 1, 0},
				{1, 0, 1},
			},
			expect: 3,
		},
		{
			name: "复杂情况: 较大网格",
			grid: [][]int{
				{1, 4, 8, 6, 2},
				{2, 5, 3, 7, 4},
				{3, 6, 2, 1, 5},
			},
			expect: 17,
		},
		{
			name: "边界情况: 所有元素相同",
			grid: [][]int{
				{5, 5, 5},
				{5, 5, 5},
			},
			expect: 20,
		},
		{
			name: "复杂情况: 需要选择最优路径",
			grid: [][]int{
				{1, 2, 5},
				{3, 2, 1},
			},
			expect: 6,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := minPathSum(tt.grid)
			if result != tt.expect {
				t.Errorf("minPathSum(%v) = %d, want %d",
					tt.grid, result, tt.expect)
			}
		})
	}
}
