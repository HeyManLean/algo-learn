# -*- coding: utf-8 -*-


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """找出二叉搜索树第k小的数"""
        # 二叉搜索树，左变节点值比右边（包括父节点）小

        self.k = k
        self.res = 0

        # 中序遍历
        def traverse(root: TreeNode):
            if not root:
                return

            traverse(root.left)
            self.k -= 1
            if self.k == 0:
                self.res = root.val
                return
            traverse(root.right)

        traverse(root)
        return self.res

    def convertBST(self, root: TreeNode) -> TreeNode:
        """538. 把二叉搜索树转换为累加树
        给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），
        使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。"""
        # 遍历，先遍历右节点，访问父节点，再遍历左节点
        # 每访问一个节点，将其数值加到当前总和中，赋值给当前节点
        self.sum = 0

        def traverse(root: TreeNode):
            if not root:
                return

            traverse(root.right)
            self.sum += root.val
            root.val = self.sum
            traverse(root.left)

        traverse(root)
        return root

    def isValidBST(self, root: TreeNode) -> bool:
        """98. 验证二叉搜索树
        给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
        有效 二叉搜索树定义如下：
        节点的左子树只包含 小于 当前节点的数。
        节点的右子树只包含 大于 当前节点的数。
        所有左子树和右子树自身必须也是二叉搜索树。
        """

        # 当前节点小于右子树所有节点（包括右子节点的左边节点）
        # 中序遍历是从小到大的，记录当前遍历的max值进行比较即可
        self.max = float('-inf')
        self.valid = True

        def traverse(root: TreeNode):
            if not root:
                return
            if not self.valid:
                return

            traverse(root.left)
            if root.val <= self.max:
                self.valid = False
                return
            self.max = root.val
            traverse(root.right)
        traverse(root)
        return self.valid

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        """701. 二叉搜索树中的插入操作
        给定二叉搜索树（BST）的根节点 root 和要插入树中的值 value ，将值插入二叉搜索树
        """
        # 如果有节点值根val一致，则更新该节点值
        # 比较左右节点，进行递归遍历，并插入该值
        # 更改操作，需要返回新的子节点
        if not root:
            return TreeNode(val)

        if root.val == val:
            return root
        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        """450. 删除二叉搜索树中的节点
        给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，
        并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

        一般来说，删除节点可分为两个步骤：
        首先找到需要删除的节点；
        如果找到了，删除它。
        """
        # 如果找不到该值，则直接返回
        # 如果没有右子树，返回左节点
        # 如果没有左子树，返回右节点
        # 否则，如果当前节点有右子树，则将该节点赋值为右子树最小值，并将右子树最小节点删除
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # 有左右子树，取右子树最小值
            p = root.right
            while p and p.left:
                p = p.left

            root.val = p.val
            root.right = self.deleteNode(root.right, p.val)

        return root
    
    memo = {}

    def numTrees(self, n: int) -> int:
        """96. 不同的二叉搜索树
        给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？
        """
        # 递归，每个节点，0~n-1 个数分别分配给左右节点进行构造，需要保证顺序
        if not n:
            return 1
        
        if n in self.memo:
            return self.memo[n]

        # 左子树可以有0~n-1 个节点
        num = 0
        for i in range(n):
            # 右子树则有 n-i - 1 个节点
            left = self.numTrees(i)
            right = self.numTrees(n - 1 - i)
            num += left * right

        self.memo[n] = num
        return num


    def generateTrees(self, n: int) -> list[TreeNode]:
        """95. 不同的二叉搜索树 II
        给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 
        """
        # 按照0~n-1分别分配给左右子树进行构建
        # 当前节点取左子树后面的一个值
        def gen_sub_trees(low, high):
            # 左闭右开
            if low >= high:
                return [None]

            # 左子树的节点个数，需要移除掉当前节点个数1
            sub_trees = []
            for left_num in range(high - low):
                left_trees = gen_sub_trees(low, low + left_num)
                right_trees = gen_sub_trees(low + left_num + 1, high)

                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(low + left_num)
                        root.left = left
                        root.right = right
                        sub_trees.append(root)
            return sub_trees

        return gen_sub_trees(1, n + 1)


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
    root = gen_tree([3, 1, 4, None, 2])
    assert Solution().kthSmallest(root, 1) == 1

    root = gen_tree([5, 4, 6, None, None, 3, 7])
    assert not Solution().isValidBST(root)

    assert Solution().numTrees(3) == 5
    assert Solution().numTrees(1) == 1

    assert len(Solution().generateTrees(3)) == 5

    print("OK")
