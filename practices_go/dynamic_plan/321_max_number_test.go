package dynamicplan

import (
	"reflect"
	"testing"
)

func TestMaxNumber(t *testing.T) {
	cases := []struct {
		name     string
		nums1    []int
		nums2    []int
		k        int
		expected []int
	}{
		// 题目示例
		{
			name:     "示例1: nums1=[3,4,6,5], nums2=[9,1,2,5,8,3], k=5",
			nums1:    []int{3, 4, 6, 5},
			nums2:    []int{9, 1, 2, 5, 8, 3},
			k:        5,
			expected: []int{9, 8, 6, 5, 3},
		},
		{
			name:     "示例2: nums1=[6,7], nums2=[6,0,4], k=5",
			nums1:    []int{6, 7},
			nums2:    []int{6, 0, 4},
			k:        5,
			expected: []int{6, 7, 6, 0, 4},
		},
		{
			name:     "示例3: nums1=[3,9], nums2=[8,9], k=3",
			nums1:    []int{3, 9},
			nums2:    []int{8, 9},
			k:        3,
			expected: []int{9, 8, 9},
		},
		{
			name:     "示例4",
			nums1:    []int{8, 6, 9},
			nums2:    []int{1, 7, 5},
			k:        3,
			expected: []int{9, 7, 5},
		},
		// 边界情况
		{
			name:     "k等于1",
			nums1:    []int{3, 4, 6, 5},
			nums2:    []int{9, 1, 2, 5, 8, 3},
			k:        1,
			expected: []int{9},
		},
		{
			name:     "k等于两个数组长度之和",
			nums1:    []int{6, 7},
			nums2:    []int{6, 0, 4},
			k:        5,
			expected: []int{6, 7, 6, 0, 4},
		},
		{
			name:     "只从nums1取数",
			nums1:    []int{9, 8, 7},
			nums2:    []int{1, 2, 3},
			k:        3,
			expected: []int{9, 8, 7},
		},
		{
			name:     "只从nums2取数",
			nums1:    []int{1, 2, 3},
			nums2:    []int{9, 8, 7},
			k:        3,
			expected: []int{9, 8, 7},
		},
		// 复杂情况
		{
			name:     "需要穿插合并",
			nums1:    []int{2, 5, 6, 4, 4, 0},
			nums2:    []int{7, 3, 8, 0, 6, 5, 7, 6, 2},
			k:        15,
			expected: []int{7, 3, 8, 2, 5, 6, 4, 4, 0, 6, 5, 7, 6, 2, 0},
		},
		{
			name:     "相同数字需要比较后续",
			nums1:    []int{6, 7},
			nums2:    []int{6, 0, 4},
			k:        3,
			expected: []int{6, 7, 6},
		},
		{
			name:     "包含0的情况",
			nums1:    []int{0, 1, 2},
			nums2:    []int{0, 3, 4},
			k:        4,
			expected: []int{3, 4, 0, 1},
		},
		{
			name:     "单元素数组",
			nums1:    []int{9},
			nums2:    []int{8},
			k:        2,
			expected: []int{9, 8},
		},
		{
			name:     "单元素数组k=1",
			nums1:    []int{9},
			nums2:    []int{8},
			k:        1,
			expected: []int{9},
		},
	}

	for _, tt := range cases {
		t.Run(tt.name, func(t *testing.T) {
			res := maxNumber(tt.nums1, tt.nums2, tt.k)
			if !reflect.DeepEqual(res, tt.expected) {
				t.Errorf("maxNumber(%v, %v, %d) = %v, expected %v",
					tt.nums1, tt.nums2, tt.k, res, tt.expected)
			}
		})
	}
}

func TestMaxSequence(t *testing.T) {
	cases := []struct {
		name     string
		nums     []int
		k        int
		expected []int
	}{
		{
			name:     "基本测试",
			nums:     []int{3, 4, 6, 5},
			k:        2,
			expected: []int{6, 5},
		},
		{
			name:     "基本测试",
			nums:     []int{8, 6, 9},
			k:        1,
			expected: []int{9},
		},
		{
			name:     "k等于数组长度",
			nums:     []int{3, 4, 6, 5},
			k:        4,
			expected: []int{3, 4, 6, 5},
		},
		{
			name:     "k等于0",
			nums:     []int{3, 4, 6, 5},
			k:        0,
			expected: []int{},
		},
		{
			name:     "单调递减",
			nums:     []int{9, 8, 7, 6},
			k:        2,
			expected: []int{9, 8},
		},
		{
			name:     "需要删除中间元素",
			nums:     []int{2, 5, 6, 4, 4, 0},
			k:        3,
			expected: []int{6, 4, 4},
		},
	}

	for _, tt := range cases {
		t.Run(tt.name, func(t *testing.T) {
			res := maxSequence(tt.nums, tt.k)
			if !reflect.DeepEqual(res, tt.expected) {
				t.Errorf("maxSequence(%v, %d) = %v, expected %v",
					tt.nums, tt.k, res, tt.expected)
			}
		})
	}
}

func TestMerge(t *testing.T) {
	cases := []struct {
		name     string
		nums1    []int
		nums2    []int
		expected []int
	}{
		{
			name:     "基本合并",
			nums1:    []int{3, 4, 6},
			nums2:    []int{9, 1, 2},
			expected: []int{9, 3, 4, 6, 1, 2},
		},
		{
			name:     "nums1为空",
			nums1:    []int{},
			nums2:    []int{9, 1, 2},
			expected: []int{9, 1, 2},
		},
		{
			name:     "nums2为空",
			nums1:    []int{3, 4, 6},
			nums2:    []int{},
			expected: []int{3, 4, 6},
		},
		{
			name:     "相同数字比较后续",
			nums1:    []int{6, 7},
			nums2:    []int{6, 0, 4},
			expected: []int{6, 7, 6, 0, 4},
		},
	}

	for _, tt := range cases {
		t.Run(tt.name, func(t *testing.T) {
			res := merge(tt.nums1, tt.nums2)
			if !reflect.DeepEqual(res, tt.expected) {
				t.Errorf("merge(%v, %v) = %v, expected %v",
					tt.nums1, tt.nums2, res, tt.expected)
			}
		})
	}
}
