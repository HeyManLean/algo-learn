package bytedance

func maxPathSum(root *TreeNode) int {
	/*
		124. 二叉树中的最大路径和

		二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。
		同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

		路径和 是路径中各节点值的总和。

		给你一个二叉树的根节点 root ，返回其 最大路径和 。


		示例 1：
		输入：root = [1,2,3]
		输出：6
		解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6

		示例 2：
		输入：root = [-10,9,20,null,null,15,7]
		输出：42
		解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42


		树中节点数目范围是 [1, 3 * 10^4]
		-1000 <= Node.val <= 1000
	*/

	// 处于某个节点，有三个方案，左子树+顶点、右子树+顶点，左右子树+定点

	// 自底向上，当前节点路径最大值 = max(左节点路径最大值，右节点路径最大值) + 当前节点
	// 或者不向上了，res = max(res, 左节点路径最大值，右节点路径最大值 + 当前节点)
	res := root.Val
	var max = func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	var dfs func(start *TreeNode) int
	dfs = func(start *TreeNode) int {
		if start == nil {
			return 0
		}
		// 包含start的路径最大值
		left := max(dfs(start.Left), 0)
		right := max(dfs(start.Right), 0)

		res = max(res, left+right+start.Val)
		return max(left, right) + start.Val
	}
	dfs(root)
	return res
}
