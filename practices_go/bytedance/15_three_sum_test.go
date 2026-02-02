package bytedance

import (
	"reflect"
	"sort"
	"testing"
)

// sortTriplets 对结果排序以便与预期比较（题目不要求顺序）
func sortTriplets(res [][]int) {
	sort.Slice(res, func(i, j int) bool {
		a, b := res[i], res[j]
		if a[0] != b[0] {
			return a[0] < b[0]
		}
		if a[1] != b[1] {
			return a[1] < b[1]
		}
		return a[2] < b[2]
	})
}

func TestThreeSum(t *testing.T) {
	tests := []struct {
		name string
		nums []int
		want [][]int
	}{
		{
			name: "示例1",
			nums: []int{-1, 0, 1, 2, -1, -4},
			want: [][]int{{-1, -1, 2}, {-1, 0, 1}},
		},
		{
			name: "示例2",
			nums: []int{0, 1, 1},
			want: [][]int{},
		},
		{
			name: "示例3",
			nums: []int{0, 0, 0},
			want: [][]int{{0, 0, 0}},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := threeSum(tt.nums)
			sortTriplets(got)
			sortTriplets(tt.want)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("threeSum() = %v, want %v", got, tt.want)
			}
		})
	}
}
