package bytedance

import (
	"reflect"
	"testing"
)

// 辅助函数：创建链表
func createList(vals []int) *ListNode {
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

// 辅助函数：链表转切片
func listToSlice(head *ListNode) []int {
	result := []int{}
	current := head
	for current != nil {
		result = append(result, current.Val)
		current = current.Next
	}
	return result
}

func TestReverseKGroup(t *testing.T) {
	tests := []struct {
		name string
		head []int
		k    int
		want []int
	}{
		{
			name: "示例1: k=2",
			head: []int{1, 2, 3, 4, 5},
			k:    2,
			want: []int{2, 1, 4, 3, 5},
		},
		{
			name: "示例2: k=3",
			head: []int{1, 2, 3, 4, 5},
			k:    3,
			want: []int{3, 2, 1, 4, 5},
		},
		{
			name: "示例3: k=1",
			head: []int{1, 2, 3, 4, 5},
			k:    1,
			want: []int{1, 2, 3, 4, 5},
		},
		{
			name: "k等于链表长度",
			head: []int{1, 2, 3, 4},
			k:    4,
			want: []int{4, 3, 2, 1},
		},
		{
			name: "空链表",
			head: []int{},
			k:    1,
			want: []int{},
		},
		{
			name: "单节点链表",
			head: []int{1},
			k:    1,
			want: []int{1},
		},
		{
			name: "k大于链表长度",
			head: []int{1, 2},
			k:    3,
			want: []int{1, 2},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			head := createList(tt.head)
			result := reverseKGroup(head, tt.k)
			got := listToSlice(result)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("reverseKGroup() = %v, want %v", got, tt.want)
			}
		})
	}
}
