package bytedance

func rightSideView(root *TreeNode) []int {
	/*
		199. 二叉树的右视图

		给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。


		示例 1：
		输入: root = [1,2,3,null,5,null,4]
		输出: [1,3,4]
		解释:
		   1            <---
		 /   \
		2     3         <---
		 \     \
		  5     4       <---

		示例 2：
		输入: root = [1,null,3]
		输出: [1,3]

		示例 3：
		输入: root = []
		输出: []


		二叉树的节点个数的范围是 [0, 100]
		-100 <= Node.val <= 100
	*/
	if root == nil {
		return []int{}
	}
	// 层序遍历，只显示最右侧
	res := []int{}
	q := []*TreeNode{root}

	for len(q) > 0 {
		res = append(res, q[len(q)-1].Val)
		newQ := []*TreeNode{}

		for _, node := range q {
			if node.Left != nil {
				newQ = append(newQ, node.Left)
			}
			if node.Right != nil {
				newQ = append(newQ, node.Right)
			}
		}
		q = newQ
	}

	return res
}
