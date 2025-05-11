# coding=utf-8
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def level_order(root: TreeNode) -> list:
    """Binary Tree Level Order Traversal (easy)

    ```js
    102. 二叉树的层序遍历
    给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

    

    示例：
    二叉树：[3,9,20,null,null,15,7],

     3
    / \
    9  20
      /  \
     15   7
    返回其层次遍历结果：

    [
        [3],
        [9,20],
        [15,7]
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
