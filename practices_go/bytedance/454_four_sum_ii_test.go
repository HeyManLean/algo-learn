package bytedance

import (
	"testing"
)

func TestFourSumCount(t *testing.T) {
	tests := []struct {
		name  string
		nums1 []int
		nums2 []int
		nums3 []int
		nums4 []int
		want  int
	}{
		{
			name:  "示例1",
			nums1: []int{1, 2},
			nums2: []int{-2, -1},
			nums3: []int{-1, 2},
			nums4: []int{0, 2},
			want:  2,
		},
		{
			name:  "示例2",
			nums1: []int{0},
			nums2: []int{0},
			nums3: []int{0},
			nums4: []int{0},
			want:  1,
		},
		{
			name:  "无满足元组",
			nums1: []int{1, 1},
			nums2: []int{1, 1},
			nums3: []int{1, 1},
			nums4: []int{1, 1},
			want:  0,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := fourSumCount(tt.nums1, tt.nums2, tt.nums3, tt.nums4); got != tt.want {
				t.Errorf("fourSumCount() = %v, want %v", got, tt.want)
			}
		})
	}
}
