# coding=utf-8
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def average_of_levels(root: TreeNode) -> list:
    """Level Averages in a Binary Tree (easy)

    ```js
    二叉树的层平均值
    给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。

    

    示例 1：

    输入：
        3
    / \
    9  20
        /  \
    15   7
    输出：[3, 14.5, 11]
    解释：
    第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。
    ```
    """
    if not root:
        return []

    node_list = [root]

    res = []

    while True:
        new_node_list = []
        
        sum_val = 0

        for node in node_list:
            sum_val += node.val

            if node.left:
                new_node_list.append(node.left)
            if node.right:
                new_node_list.append(node.right)

        res.append(sum_val / len(node_list))

        if not new_node_list:
            break

        node_list = new_node_list

    return res
