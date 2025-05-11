# coding=utf-8


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum_: int) -> int:
        """Count Paths for a Sum (medium)

        ```js
        路径总和 III
        给定一个二叉树，它的每个结点都存放着一个整数值。

        找出路径和等于给定数值的路径总数。

        路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

        二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

        示例：

        root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

            10
           /  \
          5   -3
         / \    \
        3   2   11
       / \   \
      3  -2   1

        返回 3。和等于 8 的路径有:

        1.  5 -> 3
        2.  5 -> 2 -> 1
        3.  -3 -> 11
        ```
        """
        def dfs(node, sum_list):
            if not node:
                return 0

            sum_list = [item + node.val for item in sum_list]
            sum_list.append(node.val)

            count = 0
            for item in sum_list:
                if item == sum_:
                    count += 1

            return count + dfs(node.left, sum_list) + dfs(node.right, sum_list)

        return dfs(root, [])
