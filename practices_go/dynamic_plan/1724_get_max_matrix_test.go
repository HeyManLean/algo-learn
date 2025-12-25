package dynamicplan

import (
	"reflect"
	"testing"
)

func TestGetMaxMatrix(t *testing.T) {
	cases := []struct {
		name     string
		matrix   [][]int
		expected []int
	}{
		{
			name: "注释示例",
			matrix: [][]int{
				{-1, 0},
				{0, -1},
			},
			expected: []int{0, 1, 0, 1},
		},
		{
			name: "单个元素",
			matrix: [][]int{
				{5},
			},
			expected: []int{0, 0, 0, 0},
		},
		{
			name: "全为正数",
			matrix: [][]int{
				{1, 2},
				{3, 4},
			},
			expected: []int{0, 0, 1, 1},
		},
		{
			name: "全为负数",
			matrix: [][]int{
				{-1, -2},
				{-3, -4},
			},
			expected: []int{0, 0, 0, 0},
		},
		{
			name: "包含0",
			matrix: [][]int{
				{0, 0},
				{0, 0},
			},
			expected: []int{0, 0, 0, 0},
		},
		{
			name: "单行矩阵",
			matrix: [][]int{
				{-1, 2, -1, 3},
			},
			expected: []int{0, 1, 0, 3},
		},
		{
			name: "单列矩阵",
			matrix: [][]int{
				{-1},
				{2},
				{-1},
			},
			expected: []int{1, 0, 1, 0},
		},
		{
			name: "混合正负数",
			matrix: [][]int{
				{1, -2, 3},
				{-4, 5, -6},
				{7, -8, 9},
			},
			expected: []int{2, 2, 2, 2},
		},
	}

	for _, tt := range cases {
		t.Run(tt.name, func(t *testing.T) {
			res := getMaxMatrix(tt.matrix)
			if !reflect.DeepEqual(res, tt.expected) {
				t.Errorf("getMaxMatrix(%v) = %v, expected %v", tt.matrix, res, tt.expected)
			}
		})
	}
}
