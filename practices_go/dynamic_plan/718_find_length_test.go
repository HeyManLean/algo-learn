package dynamicplan

import "testing"

func TestFindLength(t *testing.T) {
	tests := []struct {
		name   string
		nums1  []int
		nums2  []int
		expect int
	}{
		{
			name:   "示例1: [1,2,3,2,1] 和 [3,2,1,4,7]",
			nums1:  []int{1, 2, 3, 2, 1},
			nums2:  []int{3, 2, 1, 4, 7},
			expect: 3,
		},
		{
			name:   "示例2: 全0数组",
			nums1:  []int{0, 0, 0, 0, 0},
			nums2:  []int{0, 0, 0, 0, 0},
			expect: 5,
		},
		{
			name:   "无公共子数组",
			nums1:  []int{1, 2, 3},
			nums2:  []int{4, 5, 6},
			expect: 0,
		},
		{
			name:   "单个元素相同",
			nums1:  []int{1, 2, 3},
			nums2:  []int{2, 4, 5},
			expect: 1,
		},
		{
			name:   "单个元素不同",
			nums1:  []int{1},
			nums2:  []int{2},
			expect: 0,
		},
		{
			name:   "单个元素相同",
			nums1:  []int{1},
			nums2:  []int{1},
			expect: 1,
		},
		{
			name:   "完全相同的数组",
			nums1:  []int{1, 2, 3, 4, 5},
			nums2:  []int{1, 2, 3, 4, 5},
			expect: 5,
		},
		{
			name:   "部分匹配在中间",
			nums1:  []int{0, 1, 1, 0, 0},
			nums2:  []int{1, 1, 0, 0, 1},
			expect: 4,
		},
		{
			name:   "多个相同子数组，取最长",
			nums1:  []int{1, 2, 3, 2, 1},
			nums2:  []int{3, 2, 1, 4, 7},
			expect: 3,
		},
		{
			name:   "边界情况: 空数组1",
			nums1:  []int{},
			nums2:  []int{1, 2, 3},
			expect: 0,
		},
		{
			name:   "边界情况: 空数组2",
			nums1:  []int{1, 2, 3},
			nums2:  []int{},
			expect: 0,
		},
		{
			name:   "边界情况: 两个空数组",
			nums1:  []int{},
			nums2:  []int{},
			expect: 0,
		},
		{
			name:   "子数组在开头",
			nums1:  []int{1, 2, 3, 4},
			nums2:  []int{1, 2, 3, 5, 6},
			expect: 3,
		},
		{
			name:   "子数组在结尾",
			nums1:  []int{5, 6, 1, 2, 3},
			nums2:  []int{4, 5, 1, 2, 3},
			expect: 3,
		},
		{
			name:   "重复元素",
			nums1:  []int{1, 1, 1, 1},
			nums2:  []int{1, 1, 1, 1},
			expect: 4,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := findLength(tt.nums1, tt.nums2)
			if result != tt.expect {
				t.Errorf("findLength(%v, %v) = %d, want %d",
					tt.nums1, tt.nums2, result, tt.expect)
			}
		})
	}
}
