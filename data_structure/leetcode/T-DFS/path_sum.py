# coding=utf-8
# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def has_path_sum(self, root: TreeNode, sum: int) -> bool:
        """Binary Tree Path Sum (easy)

        ```js
        路径总和
        给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

        说明: 叶子节点是指没有子节点的节点。

        示例:
        给定如下二叉树，以及目标和 sum = 22，

                   5
                  / \
                 4   8
                /   / \
               11  13  4
              /  \      \
             7    2      1
        返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
        ```
        """
        if not root:
            return False

        que_node = collections.deque([root])
        que_val = collections.deque([root.val])

        while que_node:
            node = que_node.popleft()
            temp = que_val.popleft()

            if not (node.left or node.right):
                if temp == sum:
                    return True
                else:
                    continue

            if node.left:
                que_node.append(node.left)
                que_val.append(node.left.val + temp)

            if node.right:
                que_node.append(node.right)
                que_val.append(node.right.val + temp)

        return False

        """递归
        if not root:
            return False

        if not (root.left or root.right):
            if root.val == sum:
                return True
            else:
                return False

        return self.has_path_sum(root.left) or self.has_path_sum(root.right)
        """
