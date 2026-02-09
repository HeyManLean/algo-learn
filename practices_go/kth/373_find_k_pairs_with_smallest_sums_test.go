package bytedance

import (
	"reflect"
	"testing"
)

func TestKSmallestPairs(t *testing.T) {
	tests := []struct {
		name  string
		nums1 []int
		nums2 []int
		k     int
		want  [][]int
	}{
		{
			name:  "示例1",
			nums1: []int{1, 7, 11},
			nums2: []int{2, 4, 6},
			k:     3,
			want:  [][]int{{1, 2}, {1, 4}, {1, 6}},
		},
		{
			name:  "示例2",
			nums1: []int{1, 1, 2},
			nums2: []int{1, 2, 3},
			k:     2,
			want:  [][]int{{1, 1}, {1, 1}},
		},
		{
			name:  "示例3",
			nums1: []int{1, 2},
			nums2: []int{3},
			k:     3,
			want:  [][]int{{1, 3}, {2, 3}},
		},
		{
			name:  "测试",
			nums1: []int{1, 2, 4, 5, 6},
			nums2: []int{3, 5, 7, 9},
			k:     3,
			want:  [][]int{{1, 3}, {2, 3}, {1, 5}},
		},
		{
			name:  "单个元素",
			nums1: []int{1},
			nums2: []int{1},
			k:     1,
			want:  [][]int{{1, 1}},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := kSmallestPairs(tt.nums1, tt.nums2, tt.k)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("kSmallestPairs() = %v, want %v", got, tt.want)
			}
		})
	}
}
