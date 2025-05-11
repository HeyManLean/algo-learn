# coding=utf-8
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        """Sum of Path Numbers (medium)

        ```js
        求根到叶子节点数字之和
        给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。

        例如，从根到叶子节点路径 1->2->3 代表数字 123。

        计算从根到叶子节点生成的所有数字之和。
        点是指没有子节点的节点。

        示例 1:

        输入: [1,2,3]
          1
         / \
        2   3
        输出: 25
        解释:
        从根到叶子节点路径 1->2 代表数字 12.
        从根到叶子节点路径 1->3 代表数字 13.
        因此，数字总和 = 12 + 13 = 25.
        示例 2:

        输入: [4,9,0,5,1]
          4
         / \
        9   0
       / \
      5   1
        输出: 1026
        解释:
        从根到叶子节点路径 4->9->5 代表数字 495.
        从根到叶子节点路径 4->9->1 代表数字 491.
        从根到叶子节点路径 4->0 代表数字 40.
        因此，数字总和 = 495 + 491 + 40 = 1026.
        ```
        """
        if not root:
            return 0

        res = 0

        stack = [(root, 0)]

        while stack:
            node, temp = stack.pop()

            temp_sum = temp * 10 + node.val

            if not (node.left or node.right):
                res += temp_sum

            if node.left:
                stack.append((node.left, temp_sum))

            if node.right:
                stack.append((node.right, temp_sum))

        return res

    def sumNumbersV2(self, root: TreeNode) -> int:
        """递归"""
        def dfs(node, temp):
            if not node:
                return 0

            temp_sum = temp * 10 + node.val

            if not (node.left or node.right):
                return temp_sum

            return dfs(node.left, temp_sum) + dfs(node.right, temp_sum)
        
        return dfs(root, 0)
