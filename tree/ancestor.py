# -*- coding: utf-8 -*-
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode):
        """236. 二叉树的最近公共祖先"""
        return self.find(root, p, q)

    def find(self, root: TreeNode, p: TreeNode, q: TreeNode):
        # 递归遍历，找到一个节点，满足一下条件均认为是最近公共祖先
        # 1. p 和 q 分别在该节点左右子树中
        # 2. p 在 q 的子树中 或 q 在 p 的子树中
        if not root:
            return None

        if root.val == p.val or root.val == q.val:
            return root

        left = self.find(root.left, p, q)
        right = self.find(root.right, p, q)
        if left and right:
            return root

        return left or right

    def lowestCommonAncestorNodes(self, root: TreeNode, nodes: list[TreeNode]):
        """1676. 二叉树的最近公共祖先 IV"""
        if not root:
            return None

        for node in nodes:
            if root.val == node.val:
                return root

        left = self.lowestCommonAncestorNodes(root.left, nodes)
        right = self.lowestCommonAncestorNodes(root.right, nodes)
        if left and right:
            return root

        return left or right


def gen_tree(arr: list[int]):
    root = TreeNode(arr[0])

    q = [root]
    i = 0
    while q:
        cur = q.pop(0)
        if i + 1 < len(arr) and arr[i + 1] is not None:
            cur.left = TreeNode(arr[i + 1])
            q.append(cur.left)
        if i + 2 < len(arr) and arr[i + 2] is not None:
            cur.right = TreeNode(arr[i + 2])
            q.append(cur.right)
        i += 2

    return root


if __name__ == "__main__":
    root = gen_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    res = Solution().lowestCommonAncestor(root, TreeNode(5), TreeNode(1))
    print(res.val)
    assert res.val == 3

    res = Solution().lowestCommonAncestorNodes(
        root, [TreeNode(7), TreeNode(4), TreeNode(6)]
    )
    print(res.val)
    assert res.val == 5

    print("OK")
