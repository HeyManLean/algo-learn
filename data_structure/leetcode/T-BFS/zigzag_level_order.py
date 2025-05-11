# coding=utf-8
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def zigzag_level_order(root: TreeNode) -> list:
    """Zigzag Traversal (medium)

    ```js
    二叉树的锯齿形层次遍历
    给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

    例如：
    给定二叉树 [3,9,20,null,null,15,7],

     3
    / \
    9  20
      /  \
     15   7
    返回锯齿形层次遍历如下：

    [
        [3],
        [20,9],
        [15,7]
    ]
    ```
    """
    if not root:
        return []

    node_list = [root]

    res = []

    turn = 1

    while True:
        new_node_list = []
        node_vals = []

        for node in node_list:
            node_vals.append(node.val)

            if node.left:
                new_node_list.append(node.left)
            if node.right:
                new_node_list.append(node.right)

        res.append(node_vals[::turn])

        if not new_node_list:
            break

        node_list = new_node_list
        turn *= -1

    return res
