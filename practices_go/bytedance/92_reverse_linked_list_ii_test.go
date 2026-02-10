package bytedance

import (
	"reflect"
	"testing"
)

func listToSlice(head *ListNode) []int {
	var result []int
	for head != nil {
		result = append(result, head.Val)
		head = head.Next
	}
	return result
}

func TestReverseBetween(t *testing.T) {
	tests := []struct {
		name  string
		head  []int
		left  int
		right int
		want  []int
	}{
		{
			name:  "示例1: 反转中间部分",
			head:  []int{1, 2, 3, 4, 5},
			left:  2,
			right: 4,
			want:  []int{1, 4, 3, 2, 5},
		},
		{
			name:  "示例2: 单节点",
			head:  []int{5},
			left:  1,
			right: 1,
			want:  []int{5},
		},
		{
			name:  "反转整个链表",
			head:  []int{1, 2, 3, 4, 5},
			left:  1,
			right: 5,
			want:  []int{5, 4, 3, 2, 1},
		},
		{
			name:  "反转前两个节点",
			head:  []int{1, 2, 3},
			left:  1,
			right: 2,
			want:  []int{2, 1, 3},
		},
		{
			name:  "反转最后两个节点",
			head:  []int{1, 2, 3},
			left:  2,
			right: 3,
			want:  []int{1, 3, 2},
		},
		{
			name:  "两个节点反转",
			head:  []int{3, 5},
			left:  1,
			right: 2,
			want:  []int{5, 3},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			head := sliceToList(tt.head)
			got := reverseBetween(head, tt.left, tt.right)
			gotSlice := listToSlice(got)
			if !reflect.DeepEqual(gotSlice, tt.want) {
				t.Errorf("reverseBetween() = %v, want %v", gotSlice, tt.want)
			}
		})
	}
}
