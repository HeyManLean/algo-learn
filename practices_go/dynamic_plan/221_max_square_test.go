package dynamicplan

import "testing"

func TestMaximalSquare(t *testing.T) {
	tests := []struct {
		name   string
		matrix [][]byte
		want   int
	}{
		{
			name: "示例1",
			matrix: [][]byte{
				{'1', '0', '1', '0', '0'},
				{'1', '0', '1', '1', '1'},
				{'1', '1', '1', '1', '1'},
				{'1', '0', '0', '1', '0'},
			},
			want: 4,
		},
		{
			name: "示例2",
			matrix: [][]byte{
				{'0', '1'},
				{'1', '0'},
			},
			want: 1,
		},
		{
			name: "示例3",
			matrix: [][]byte{
				{'0'},
			},
			want: 0,
		},
		{
			name: "全为1的矩阵",
			matrix: [][]byte{
				{'1', '1', '1'},
				{'1', '1', '1'},
				{'1', '1', '1'},
			},
			want: 9,
		},
		{
			name: "全为0的矩阵",
			matrix: [][]byte{
				{'0', '0', '0'},
				{'0', '0', '0'},
				{'0', '0', '0'},
			},
			want: 0,
		},
		{
			name: "单行矩阵",
			matrix: [][]byte{
				{'1', '1', '1', '0', '1'},
			},
			want: 1,
		},
		{
			name: "单列矩阵",
			matrix: [][]byte{
				{'1'},
				{'1'},
				{'0'},
				{'1'},
			},
			want: 1,
		},
		{
			name: "2x2全1",
			matrix: [][]byte{
				{'1', '1'},
				{'1', '1'},
			},
			want: 4,
		},
		{
			name: "复杂情况",
			matrix: [][]byte{
				{'1', '0', '1', '1', '1'},
				{'1', '0', '1', '1', '1'},
				{'1', '1', '1', '1', '1'},
				{'1', '0', '0', '1', '0'},
			},
			want: 9,
		},
		{
			name: "只有单个1",
			matrix: [][]byte{
				{'0', '0', '0'},
				{'0', '1', '0'},
				{'0', '0', '0'},
			},
			want: 1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maximalSquare(tt.matrix); got != tt.want {
				t.Errorf("maximalSquare() = %v, want %v", got, tt.want)
			}
		})
	}
}
