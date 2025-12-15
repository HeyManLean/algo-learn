package dynamicplan

import (
	"testing"
)

func TestMaximalRectangle(t *testing.T) {
	cases := []struct {
		name     string
		matrix   [][]byte
		expected int
	}{
		{
			name: "示例1",
			matrix: [][]byte{
				{'1', '0', '1', '0', '0'},
				{'1', '0', '1', '1', '1'},
				{'1', '1', '1', '1', '1'},
				{'1', '0', '0', '1', '0'},
			},
			expected: 6,
		},
		{
			name: "示例2-全0",
			matrix: [][]byte{
				{'0'},
			},
			expected: 0,
		},
		{
			name: "示例3-单个1",
			matrix: [][]byte{
				{'1'},
			},
			expected: 1,
		},
		{
			name: "全1矩阵",
			matrix: [][]byte{
				{'1', '1', '1'},
				{'1', '1', '1'},
				{'1', '1', '1'},
			},
			expected: 9,
		},
		{
			name: "单行全1",
			matrix: [][]byte{
				{'1', '1', '1', '1', '1'},
			},
			expected: 5,
		},
		{
			name: "单列全1",
			matrix: [][]byte{
				{'1'},
				{'1'},
				{'1'},
			},
			expected: 3,
		},
		{
			name: "空矩阵",
			matrix: [][]byte{
				{},
			},
			expected: 0,
		},
		{
			name: "L形矩形",
			matrix: [][]byte{
				{'1', '1', '1'},
				{'1', '0', '0'},
				{'1', '0', '0'},
			},
			expected: 3,
		},
		{
			name: "多个小矩形",
			matrix: [][]byte{
				{'1', '0', '1', '0'},
				{'1', '0', '1', '0'},
				{'1', '0', '1', '0'},
			},
			expected: 3,
		},
		{
			name: "最大矩形在中间",
			matrix: [][]byte{
				{'0', '0', '0', '0'},
				{'0', '1', '1', '1'},
				{'0', '1', '1', '1'},
				{'0', '0', '0', '0'},
			},
			expected: 6,
		},
		{
			name: "最大矩形在右下角",
			matrix: [][]byte{
				{'0', '0', '0'},
				{'0', '0', '0'},
				{'0', '1', '1'},
			},
			expected: 2,
		},
		{
			name: "最大矩形在左上角",
			matrix: [][]byte{
				{'1', '1', '0'},
				{'1', '1', '0'},
				{'0', '0', '0'},
			},
			expected: 4,
		},
	}

	for _, tt := range cases {
		t.Run(tt.name, func(t *testing.T) {
			result := maximalRectangle(tt.matrix)
			if result != tt.expected {
				t.Errorf("maximalRectangle() = %v, want %v", result, tt.expected)
			}
		})
	}
}
