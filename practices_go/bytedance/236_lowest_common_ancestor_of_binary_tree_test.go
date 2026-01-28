package bytedance

import "testing"

func TestLowestCommonAncestor(t *testing.T) {
	tests := []struct {
		name     string
		root     *TreeNode
		p        *TreeNode
		q        *TreeNode
		expected *TreeNode
	}{
		{
			name: "示例 1",
			root: &TreeNode{
				Val: 3,
				Left: &TreeNode{
					Val: 5,
					Left: &TreeNode{
						Val: 6,
					},
					Right: &TreeNode{
						Val: 2,
						Left: &TreeNode{
							Val: 7,
						},
						Right: &TreeNode{
							Val: 4,
						},
					},
				},
				Right: &TreeNode{
					Val: 1,
					Left: &TreeNode{
						Val: 0,
					},
					Right: &TreeNode{
						Val: 8,
					},
				},
			},
			p:        &TreeNode{Val: 5},
			q:        &TreeNode{Val: 1},
			expected: &TreeNode{Val: 3},
		},
		{
			name: "示例 2",
			root: &TreeNode{
				Val: 3,
				Left: &TreeNode{
					Val: 5,
					Left: &TreeNode{
						Val: 6,
					},
					Right: &TreeNode{
						Val: 2,
						Left: &TreeNode{
							Val: 7,
						},
						Right: &TreeNode{
							Val: 4,
						},
					},
				},
				Right: &TreeNode{
					Val: 1,
					Left: &TreeNode{
						Val: 0,
					},
					Right: &TreeNode{
						Val: 8,
					},
				},
			},
			p:        &TreeNode{Val: 5},
			q:        &TreeNode{Val: 4},
			expected: &TreeNode{Val: 5},
		},
		{
			name: "示例 3",
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
				},
			},
			p:        &TreeNode{Val: 1},
			q:        &TreeNode{Val: 2},
			expected: &TreeNode{Val: 1},
		},
		{
			name: "节点是另一个节点的祖先",
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
					Left: &TreeNode{
						Val: 3,
					},
				},
			},
			p:        &TreeNode{Val: 2},
			q:        &TreeNode{Val: 3},
			expected: &TreeNode{Val: 2},
		},
		{
			name: "两个节点在不同子树",
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
				},
				Right: &TreeNode{
					Val: 3,
				},
			},
			p:        &TreeNode{Val: 2},
			q:        &TreeNode{Val: 3},
			expected: &TreeNode{Val: 1},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			// 需要先找到实际的 p 和 q 节点指针
			var pNode, qNode *TreeNode
			var findNodes func(node *TreeNode)
			findNodes = func(node *TreeNode) {
				if node == nil {
					return
				}
				if node.Val == tt.p.Val {
					pNode = node
				}
				if node.Val == tt.q.Val {
					qNode = node
				}
				findNodes(node.Left)
				findNodes(node.Right)
			}
			findNodes(tt.root)

			result := lowestCommonAncestor(tt.root, pNode, qNode)
			if result == nil {
				t.Errorf("lowestCommonAncestor() = nil, expected %d", tt.expected.Val)
				return
			}
			if result.Val != tt.expected.Val {
				t.Errorf("lowestCommonAncestor() = %d, expected %d", result.Val, tt.expected.Val)
			}
		})
	}
}
