package bytedance

import (
	"reflect"
	"sort"
	"testing"
)

// sortFourSumResult 对结果排序以便比较（题目不要求顺序）
func sortFourSumResult(res [][]int) {
	for i := range res {
		sort.Ints(res[i])
	}
	sort.Slice(res, func(i, j int) bool {
		for k := 0; k < 4; k++ {
			if res[i][k] != res[j][k] {
				return res[i][k] < res[j][k]
			}
		}
		return false
	})
}

func TestFourSum(t *testing.T) {
	tests := []struct {
		name   string
		nums   []int
		target int
		want   [][]int
	}{
		{
			name:   "示例1",
			nums:   []int{1, 0, -1, 0, -2, 2},
			target: 0,
			want:   [][]int{{-2, -1, 1, 2}, {-2, 0, 0, 2}, {-1, 0, 0, 1}},
		},
		{
			name:   "示例2",
			nums:   []int{2, 2, 2, 2, 2},
			target: 8,
			want:   [][]int{{2, 2, 2, 2}},
		},
		{
			name:   "空结果",
			nums:   []int{1, 2, 3, 4},
			target: 100,
			want:   [][]int{},
		},
		{
			name:   "单元素数组",
			nums:   []int{1},
			target: 4,
			want:   [][]int{},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := fourSum(tt.nums, tt.target)
			sortFourSumResult(got)
			sortFourSumResult(tt.want)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("fourSum() = %v, want %v", got, tt.want)
			}
		})
	}
}
