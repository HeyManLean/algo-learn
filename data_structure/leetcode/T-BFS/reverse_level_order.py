# coding=utf-8
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def reverse_level_order(root: TreeNode) -> list:
    """Reverse Level Order Traversal (easy)

    ```js
    二叉树的层次遍历 II
    给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

    例如：
    给定二叉树 [3,9,20,null,null,15,7],

     3
    / \
    9  20
      /  \
     15   7
    返回其自底向上的层次遍历为：

    [
        [15,7],
        [9,20],
        [3]
    ]
    ```
    """
    if not root:
        return []

    node_list = [root]

    res = []

    while True:
        new_node_list = []
        node_vals = []

        for node in node_list:
            node_vals.append(node.val)

            if node.left:
                new_node_list.append(node.left)
            if node.right:
                new_node_list.append(node.right)

        res.append(node_vals)

        if not new_node_list:
            break

        node_list = new_node_list

    return res
