# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> list:
        """All Paths for a Sum (medium)

        ```js
        路径总和 II
        给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

        说明: 叶子节点是指没有子节点的节点。

        示例:
        给定如下二叉树，以及目标和 sum = 22，

                   5
                  / \
                 4   8
                /   / \
               11  13  4
              /  \    / \
             7    2  5   1
        返回:

        [
        [5,4,11,2],
        [5,8,4,5]
        ]
        ```
        """
        if not root:
            return []

        stack = [([root.val], root)]
        res = []

        while stack:
            tmp, node = stack.pop()

            if not (node.left or node.right) and sum(tmp) == sum:
                res.append(tmp)

            if node.right:
                stack.append((tmp + [node.right.val], node.right))

            if node.left:
                stack.append((tmp + [node.left.val], node.left))

        return res

    def pathSumV2(self, root: TreeNode, sum_: int) -> list:
        """递归方式"""
        res = []

        def dfs(node: TreeNode, tmp: list, sum_: int):
            if not node:
                return

            if not (node.left or node.right) and node.val == sum_:
                tmp += [node.val]
                res.append(tmp)

            dfs(node.left, tmp + [node.val], sum_ - node.val)
            dfs(node.right, tmp + [node.val], sum_ - node.val)

        dfs(root, [], sum_)
        return res
