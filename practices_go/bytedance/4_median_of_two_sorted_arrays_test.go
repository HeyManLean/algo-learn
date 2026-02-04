package bytedance

import (
	"testing"
)

func TestFindMedianSortedArrays(t *testing.T) {
	tests := []struct {
		name   string
		nums1  []int
		nums2  []int
		expect float64
	}{
		{
			name:   "示例1：奇数总长度",
			nums1:  []int{1, 3},
			nums2:  []int{2},
			expect: 2.00000,
		},
		{
			name:   "示例2：偶数总长度",
			nums1:  []int{1, 2},
			nums2:  []int{3, 4},
			expect: 2.50000,
		},
		{
			name:   "nums1 为空",
			nums1:  []int{},
			nums2:  []int{1},
			expect: 1.00000,
		},
		{
			name:   "nums2 为空",
			nums1:  []int{2},
			nums2:  []int{},
			expect: 2.00000,
		},
		{
			name:   "单元素 each",
			nums1:  []int{2},
			nums2:  []int{3},
			expect: 2.50000,
		},
		{
			name:   "无重叠",
			nums1:  []int{1, 2},
			nums2:  []int{3, 4, 5},
			expect: 3.00000,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := findMedianSortedArrays(tt.nums1, tt.nums2)
			if got != tt.expect {
				t.Errorf("findMedianSortedArrays() = %v, want %v", got, tt.expect)
			}
		})
	}
}
