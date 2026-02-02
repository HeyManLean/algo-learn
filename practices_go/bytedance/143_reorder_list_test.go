package bytedance

import (
	"reflect"
	"testing"
)

// 辅助函数：将切片转换为链表
func sliceToList(nums []int) *ListNode {
	if len(nums) == 0 {
		return nil
	}
	head := &ListNode{Val: nums[0]}
	curr := head
	for i := 1; i < len(nums); i++ {
		curr.Next = &ListNode{Val: nums[i]}
		curr = curr.Next
	}
	return head
}

// 辅助函数：将链表转换为切片
func listToSlice3(head *ListNode) []int {
	var result []int
	for head != nil {
		result = append(result, head.Val)
		head = head.Next
	}
	return result
}

func TestReorderList(t *testing.T) {
	tests := []struct {
		name     string
		input    []int
		expected []int
	}{
		{
			name:     "示例1: 4个节点",
			input:    []int{1, 2, 3, 4},
			expected: []int{1, 4, 2, 3},
		},
		{
			name:     "示例2: 5个节点",
			input:    []int{1, 2, 3, 4, 5},
			expected: []int{1, 5, 2, 4, 3},
		},
		{
			name:     "单个节点",
			input:    []int{1},
			expected: []int{1},
		},
		{
			name:     "两个节点",
			input:    []int{1, 2},
			expected: []int{1, 2},
		},
		{
			name:     "三个节点",
			input:    []int{1, 2, 3},
			expected: []int{1, 3, 2},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			head := sliceToList(tt.input)
			reorderList(head)
			result := listToSlice3(head)
			if !reflect.DeepEqual(result, tt.expected) {
				t.Errorf("reorderList() = %v, want %v", result, tt.expected)
			}
		})
	}
}
