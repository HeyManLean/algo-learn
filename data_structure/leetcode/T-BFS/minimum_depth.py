# coding=utf-8
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def min_depth(root: TreeNode) -> list:
    """Minimum Depth of a Binary Tree (easy)

    ```js
    二叉树的最小深度
    给定一个二叉树，找出其最小深度。

    最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

    说明: 叶子节点是指没有子节点的节点。

    示例:

    给定二叉树 [3,9,20,null,null,15,7],

        3
    / \
    9  20
        /  \
    15   7
    返回它的最小深度  2.
    ```
    """
    if not root:
        return 0

    node_list = [root]

    depth = 1

    while True:
        new_node_list = []

        for node in node_list:
            if node.left:
                new_node_list.append(node.left)
            if node.right:
                new_node_list.append(node.right)

            if not (node.left or node.right):
                return depth

        node_list = new_node_list
        depth += 1

    return depth
