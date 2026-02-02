package bytedance

import (
	"reflect"
	"testing"
)

func TestRightSideView(t *testing.T) {
	tests := []struct {
		name     string
		root     *TreeNode
		expected []int
	}{
		{
			name: "示例 1",
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
					Right: &TreeNode{
						Val: 5,
					},
				},
				Right: &TreeNode{
					Val: 3,
					Right: &TreeNode{
						Val: 4,
					},
				},
			},
			expected: []int{1, 3, 4},
		},
		{
			name: "示例 2",
			root: &TreeNode{
				Val: 1,
				Right: &TreeNode{
					Val: 3,
				},
			},
			expected: []int{1, 3},
		},
		{
			name:     "示例 3 - 空树",
			root:     nil,
			expected: []int{},
		},
		{
			name: "单个节点",
			root: &TreeNode{
				Val: 1,
			},
			expected: []int{1},
		},
		{
			name: "只有左子树",
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
					Left: &TreeNode{
						Val: 3,
					},
				},
			},
			expected: []int{1, 2, 3},
		},
		{
			name: "左子树更深",
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
					Left: &TreeNode{
						Val: 4,
					},
				},
				Right: &TreeNode{
					Val: 3,
				},
			},
			expected: []int{1, 3, 4},
		},
		{
			name: "完全二叉树",
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
					Left: &TreeNode{
						Val: 4,
					},
					Right: &TreeNode{
						Val: 5,
					},
				},
				Right: &TreeNode{
					Val: 3,
					Left: &TreeNode{
						Val: 6,
					},
					Right: &TreeNode{
						Val: 7,
					},
				},
			},
			expected: []int{1, 3, 7},
		},
		{
			name: "左右交替更深",
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
					Right: &TreeNode{
						Val: 5,
						Left: &TreeNode{
							Val: 6,
						},
					},
				},
				Right: &TreeNode{
					Val: 3,
					Right: &TreeNode{
						Val: 4,
					},
				},
			},
			expected: []int{1, 3, 4, 6},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := rightSideView(tt.root)
			if result == nil {
				result = []int{}
			}
			if !reflect.DeepEqual(result, tt.expected) {
				t.Errorf("rightSideView() = %v, expected %v", result, tt.expected)
			}
		})
	}
}
