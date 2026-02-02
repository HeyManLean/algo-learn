package bytedance

import (
	"testing"
)

func TestMaxPathSum(t *testing.T) {
	tests := []struct {
		name     string
		root     *TreeNode
		expected int
	}{
		{
			name: "示例 1: 简单三节点",
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
				},
				Right: &TreeNode{
					Val: 3,
				},
			},
			expected: 6,
		},
		{
			name: "示例 2: 包含负数根节点",
			root: &TreeNode{
				Val: -10,
				Left: &TreeNode{
					Val: 9,
				},
				Right: &TreeNode{
					Val: 20,
					Left: &TreeNode{
						Val: 15,
					},
					Right: &TreeNode{
						Val: 7,
					},
				},
			},
			expected: 42,
		},
		{
			name: "单个节点",
			root: &TreeNode{
				Val: 1,
			},
			expected: 1,
		},
		{
			name: "单个负数节点",
			root: &TreeNode{
				Val: -3,
			},
			expected: -3,
		},
		{
			name: "全负数节点",
			root: &TreeNode{
				Val: -10,
				Left: &TreeNode{
					Val: -20,
				},
				Right: &TreeNode{
					Val: -30,
				},
			},
			expected: -10,
		},
		{
			name: "左子树最优路径",
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 4,
					Left: &TreeNode{
						Val: 3,
					},
					Right: &TreeNode{
						Val: 5,
					},
				},
				Right: &TreeNode{
					Val: -100,
				},
			},
			expected: 12, // 3 -> 4 -> 5
		},
		{
			name: "深层路径",
			root: &TreeNode{
				Val: 5,
				Left: &TreeNode{
					Val: 4,
					Left: &TreeNode{
						Val: 11,
						Left: &TreeNode{
							Val: 7,
						},
						Right: &TreeNode{
							Val: 2,
						},
					},
				},
				Right: &TreeNode{
					Val: 8,
					Left: &TreeNode{
						Val: 13,
					},
					Right: &TreeNode{
						Val: 4,
						Right: &TreeNode{
							Val: 1,
						},
					},
				},
			},
			expected: 48, // 7 -> 11 -> 4 -> 5 -> 8 -> 13
		},
		{
			name: "只选择部分子树",
			root: &TreeNode{
				Val: 2,
				Left: &TreeNode{
					Val: -1,
				},
				Right: &TreeNode{
					Val: -2,
				},
			},
			expected: 2,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := maxPathSum(tt.root)
			if result != tt.expected {
				t.Errorf("maxPathSum() = %v, expected %v", result, tt.expected)
			}
		})
	}
}
