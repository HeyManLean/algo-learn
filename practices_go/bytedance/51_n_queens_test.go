package bytedance

import (
	"reflect"
	"testing"
)

func Test_solveNQueens(t *testing.T) {
	tests := []struct {
		name string
		n    int
		want [][]string
	}{
		{
			name: "示例1: n=4 有两个解",
			n:    4,
			want: [][]string{
				{".Q..", "...Q", "Q...", "..Q."},
				{"..Q.", "Q...", "...Q", ".Q.."},
			},
		},
		{
			name: "示例2: n=1 只有一个解",
			n:    1,
			want: [][]string{{"Q"}},
		},
		{
			name: "n=2 无解",
			n:    2,
			want: [][]string{},
		},
		{
			name: "n=3 无解",
			n:    3,
			want: [][]string{},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := solveNQueens(tt.n)
			// 结果顺序可能不同，需要比较集合
			if !matchNQueensResult(got, tt.want) {
				t.Errorf("solveNQueens(%d) = %v, want %v", tt.n, got, tt.want)
			}
		})
	}
}

// matchNQueensResult 比较两个解集是否等价（解的集合相同，顺序可不同）
func matchNQueensResult(got, want [][]string) bool {
	if len(got) != len(want) {
		return false
	}
	used := make([]bool, len(want))
	for _, g := range got {
		found := false
		for j, w := range want {
			if used[j] {
				continue
			}
			if reflect.DeepEqual(g, w) {
				used[j] = true
				found = true
				break
			}
		}
		if !found {
			return false
		}
	}
	return true
}
