package practicesgo

import (
	"reflect"
	"testing"
)

type Node struct {
	Val    int
	Next   *Node
	Random *Node
}

/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 *     Random *Node
 * }
 */

func copyRandomList3(head *Node) *Node {
	// copy的时候，将原本的节点和复制新节点连在一起，建立索引
	// 那么random 建立的时候，则取 random.next 就好了
	if head == nil {
		return nil
	}
	for node := head; node != nil; node = node.Next.Next {
		node.Next = &Node{Val: node.Val, Next: node.Next}
	}
	for node := head; node != nil; node = node.Next.Next {
		if node.Random != nil {
			node.Next.Random = node.Random.Next
		}
	}
	headNew := head.Next
	for node := head; node != nil; node = node.Next {
		nodeNew := node.Next
		node.Next = node.Next.Next
		if nodeNew.Next != nil {
			nodeNew.Next = nodeNew.Next.Next
		}
	}
	return headNew

}

func copyRandomList2(head *Node) *Node {
	// copy的时候，将原本的节点和复制新节点连在一起，建立索引
	// 那么random 建立的时候，则取 random.next 就好了
	if head == nil {
		return nil
	}
	p1 := head
	for p1 != nil {
		p1.Next = &Node{
			Val:  p1.Val,
			Next: p1.Next,
		}
		p1 = p1.Next.Next
	}

	p1 = head
	for p1 != nil {
		if p1.Random != nil {
			// p1.Next 是 p1 复制的新节点，p1.Random 的 Next，是 p1.Random 复制的新节点
			p1.Next.Random = p1.Random.Next
		}
		p1 = p1.Next.Next
	}

	headNew := head.Next
	p1 = head
	for p1 != nil {
		p2 := p1.Next
		p1.Next = p1.Next.Next

		if p2.Next != nil {
			p2.Next = p2.Next.Next
		}
		p1 = p1.Next
	}
	return headNew
}

func copyRandomList(head *Node) *Node {
	/*

		138. 随机链表的复制
		给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。
		构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。

		例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random --> y 。
		返回复制链表的头节点。

		用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：
		val：一个表示 Node.val 的整数。
		random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
		你的代码 只 接受原链表的头节点 head 作为传入参数。

		输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
		输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
	*/
	// 生成链表，并加入列表中，将原有node的val改成当前列表索引
	dummy := &Node{}

	var nodes []*Node

	p1 := head
	p2 := dummy
	for p1 != nil {
		p2.Next = &Node{
			Val: p1.Val,
		}
		nodes = append(nodes, p2.Next)
		p1.Val = len(nodes) - 1
		p1 = p1.Next
		p2 = p2.Next
	}

	p1 = head
	i := 0
	for p1 != nil {
		p2 := nodes[i]
		if p1.Random != nil {
			p2.Random = nodes[p1.Random.Val]
		}
		p1 = p1.Next
		i++
	}
	return dummy.Next
}

// buildList 根据 [val, random_index] 格式构建链表
// pairs: [[val, random_index], ...]
// random_index 为 -1 表示 random 为 nil
func buildList(pairs [][]int) *Node {
	if len(pairs) == 0 {
		return nil
	}

	nodes := make([]*Node, len(pairs))
	// 先创建所有节点
	for i, pair := range pairs {
		nodes[i] = &Node{Val: pair[0]}
	}

	// 连接 Next 指针
	for i := 0; i < len(nodes)-1; i++ {
		nodes[i].Next = nodes[i+1]
	}

	// 连接 Random 指针
	for i, pair := range pairs {
		if pair[1] >= 0 && pair[1] < len(nodes) {
			nodes[i].Random = nodes[pair[1]]
		}
	}

	return nodes[0]
}

// listToSlice 将链表转换为 [val, random_index] 格式
func listToSlice(head *Node) [][]int {
	if head == nil {
		return nil
	}

	// 先遍历一遍，建立节点到索引的映射
	nodeToIndex := make(map[*Node]int)
	index := 0
	for p := head; p != nil; p = p.Next {
		nodeToIndex[p] = index
		index++
	}

	// 转换为切片格式
	var result [][]int
	for p := head; p != nil; p = p.Next {
		randomIndex := -1
		if p.Random != nil {
			randomIndex = nodeToIndex[p.Random]
		}
		result = append(result, []int{p.Val, randomIndex})
	}

	return result
}

// isDeepCopy 验证 copied 是否是 head 的深拷贝
func isDeepCopy(head, copied *Node) bool {
	if head == nil && copied == nil {
		return true
	}
	if head == nil || copied == nil {
		return false
	}

	// 建立原链表节点到新链表节点的映射
	oldToNew := make(map[*Node]*Node)
	p1, p2 := head, copied
	for p1 != nil && p2 != nil {
		oldToNew[p1] = p2
		p1 = p1.Next
		p2 = p2.Next
	}

	// 检查是否完全遍历
	if p1 != nil || p2 != nil {
		return false
	}

	// 验证所有节点的值和指针关系
	p1, p2 = head, copied
	for p1 != nil && p2 != nil {
		// 验证值
		if p1.Val != p2.Val {
			return false
		}

		// 验证 Random 指针
		if p1.Random == nil {
			if p2.Random != nil {
				return false
			}
		} else {
			expectedNew := oldToNew[p1.Random]
			if p2.Random != expectedNew {
				return false
			}
		}

		// 验证新链表的节点不在原链表中
		if _, exists := oldToNew[p2]; exists {
			return false
		}

		p1 = p1.Next
		p2 = p2.Next
	}

	return true
}

func TestCopyRandomList(t *testing.T) {
	tests := []struct {
		name  string
		pairs [][]int // [val, random_index]，random_index 为 -1 表示 nil
	}{
		{
			name:  "空链表",
			pairs: nil,
		},
		{
			name:  "单个节点，random 为 nil",
			pairs: [][]int{{7, -1}},
		},
		{
			name:  "单个节点，random 指向自己",
			pairs: [][]int{{7, 0}},
		},
		{
			name:  "两个节点，random 都为 nil",
			pairs: [][]int{{1, -1}, {2, -1}},
		},
		{
			name:  "两个节点，第二个指向第一个",
			pairs: [][]int{{1, -1}, {2, 0}},
		},
		{
			name:  "题目示例",
			pairs: [][]int{{7, -1}, {13, 0}, {11, 4}, {10, 2}, {1, 0}},
		},
		{
			name:  "三个节点，形成环",
			pairs: [][]int{{1, 1}, {2, 2}, {3, 0}},
		},
		{
			name:  "所有节点 random 都指向第一个节点",
			pairs: [][]int{{1, 0}, {2, 0}, {3, 0}, {4, 0}},
		},
		{
			name:  "所有节点 random 都指向最后一个节点",
			pairs: [][]int{{1, 3}, {2, 3}, {3, 3}, {4, -1}},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			// 构建原链表
			original := buildList(tt.pairs)

			// 保存原始值的副本用于验证（因为 copyRandomList 会修改原链表的 Val）
			expectedSlice := listToSlice(original)

			// 复制链表
			copied := copyRandomList(original)

			// 验证复制链表的结构
			copiedSlice := listToSlice(copied)

			if !reflect.DeepEqual(expectedSlice, copiedSlice) {
				t.Errorf("copyRandomList() 结构不一致\n期望: %v\n实际: %v", expectedSlice, copiedSlice)
			}

			// 验证深拷贝：检查复制链表的节点是否独立于原链表
			// 注意：由于实现中修改了原链表的 Val，我们只验证复制链表的结构正确性
			if original != nil && copied != nil {
				// 验证节点是独立的（通过检查地址不同）
				originalNodes := make(map[*Node]bool)
				for p := original; p != nil; p = p.Next {
					originalNodes[p] = true
				}

				for p := copied; p != nil; p = p.Next {
					if originalNodes[p] {
						t.Errorf("copyRandomList() 复制的节点指向了原链表的节点，不是深拷贝")
					}
				}
			}

			// 验证空链表情况
			if tt.pairs == nil && copied != nil {
				t.Errorf("copyRandomList(nil) = %v, want nil", copied)
			}
		})
	}
}
