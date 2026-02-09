package bytedance

import (
	"testing"
)

// 辅助函数：从切片创建链表
func createListFromSlice(vals []int) *ListNode {
	if len(vals) == 0 {
		return nil
	}
	head := &ListNode{Val: vals[0]}
	current := head
	for i := 1; i < len(vals); i++ {
		current.Next = &ListNode{Val: vals[i]}
		current = current.Next
	}
	return head
}

// 辅助函数：将链表转换为切片
func listToSlice2(head *ListNode) []int {
	var result []int
	for head != nil {
		result = append(result, head.Val)
		head = head.Next
	}
	return result
}

// 辅助函数：比较两个链表是否相等
func compareLists(l1, l2 *ListNode) bool {
	for l1 != nil && l2 != nil {
		if l1.Val != l2.Val {
			return false
		}
		l1 = l1.Next
		l2 = l2.Next
	}
	return l1 == nil && l2 == nil
}

func TestMergeKLists(t *testing.T) {
	tests := []struct {
		name     string
		lists    []*ListNode
		expected []int
	}{
		{
			name: "示例 1",
			lists: []*ListNode{
				createListFromSlice([]int{1, 4, 5}),
				createListFromSlice([]int{1, 3, 4}),
				createListFromSlice([]int{2, 6}),
			},
			expected: []int{1, 1, 2, 3, 4, 4, 5, 6},
		},
		{
			name:     "示例 2 - 空数组",
			lists:    []*ListNode{},
			expected: []int{},
		},
		{
			name: "示例 3 - 包含空链表",
			lists: []*ListNode{
				nil,
			},
			expected: []int{},
		},
		{
			name: "单个链表",
			lists: []*ListNode{
				createListFromSlice([]int{1, 2, 3}),
			},
			expected: []int{1, 2, 3},
		},
		{
			name: "两个链表",
			lists: []*ListNode{
				createListFromSlice([]int{1, 3, 5}),
				createListFromSlice([]int{2, 4, 6}),
			},
			expected: []int{1, 2, 3, 4, 5, 6},
		},
		{
			name: "多个链表，部分为空",
			lists: []*ListNode{
				createListFromSlice([]int{1, 2}),
				nil,
				createListFromSlice([]int{3, 4}),
			},
			expected: []int{1, 2, 3, 4},
		},
		{
			name: "所有链表都只有一个元素",
			lists: []*ListNode{
				createListFromSlice([]int{3}),
				createListFromSlice([]int{1}),
				createListFromSlice([]int{2}),
			},
			expected: []int{1, 2, 3},
		},
		{
			name: "包含重复元素",
			lists: []*ListNode{
				createListFromSlice([]int{1, 1, 2}),
				createListFromSlice([]int{1, 3, 3}),
			},
			expected: []int{1, 1, 1, 2, 3, 3},
		},
		{
			name: "负数元素",
			lists: []*ListNode{
				createListFromSlice([]int{-1, 0, 1}),
				createListFromSlice([]int{-2, 2}),
			},
			expected: []int{-2, -1, 0, 1, 2},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := mergeKLists(tt.lists)
			resultSlice := listToSlice2(result)
			expectedSlice := tt.expected

			if len(resultSlice) != len(expectedSlice) {
				t.Errorf("mergeKLists() length = %v, expected %v", resultSlice, expectedSlice)
				return
			}

			for i := 0; i < len(resultSlice); i++ {
				if resultSlice[i] != expectedSlice[i] {
					t.Errorf("mergeKLists() = %v, expected %v", resultSlice, expectedSlice)
					return
				}
			}
		})
	}
}
