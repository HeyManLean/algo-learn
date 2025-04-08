# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> list[str]:
        """257. 二叉树所有路径
        输出：["1->2->5","1->3"]
        """
        res = []
        path = []

        def traverse(root: TreeNode):
            if not root:
                return None

            path.append(root.val)

            traverse(root.left)
            traverse(root.right)

            # 叶子节点直接将当前路径加入结果
            if not root.left and not root.right:
                res.append("->".join(map(str, path)))

            path.pop()

        traverse(root)
        return res

    def sumNumbers(self, root: TreeNode) -> int:
        """129.求根节点到叶节点数字之和
        每个路径生成一个数（1->2=12,1->3=13)，将所有路径的数求和(12+13=25)
        """
        all_paths = []
        path = []

        def traverse(root: TreeNode):
            if not root:
                return

            path.append(root.val)
            traverse(root.left)
            traverse(root.right)

            if not root.left and not root.right:
                all_paths.append(list(path))
            path.pop()

        traverse(root)

        res = 0
        for path in all_paths:
            num = 0
            for val in path:
                num = num * 10 + val
            res += num

        return res

    def rightSideView(self, root: TreeNode) -> list[int]:
        """199. 二叉树的右视图
        给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
        https://assets.leetcode.com/uploads/2024/11/24/tmpd5jn43fs-1.png
        输入：root = [1,2,3,None,5,None,4]
        输出：[1,3,4]
        """
        if not root:
            return []
        # 使用层序遍历，取每一层最右侧节点值
        res = []
        q = [root]
        while q:
            res.append(q[-1].val)
            nodes = list(q)
            q = []
            for node in nodes:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res

    def smallestFromLeaf(self, root: TreeNode) -> str:
        """988. 从叶结点开始的最小字符串
        给定一颗根结点为 root 的二叉树，树中的每一个结点都有一个 [0, 25] 范围内的值，分别代表字母 'a' 到 'z'。
        返回 按字典序最小 的字符串，该字符串从这棵树的一个叶结点开始，到根结点结束。
        https://assets.leetcode.com/uploads/2019/02/01/tree3.png
        输入：root = [2,2,1,None,1,0,None,0]
        输出："abc"
        """
        path = []
        all_paths = []

        def traverse(root: TreeNode):
            if not root:
                return

            path.append(root.val)
            traverse(root.left)
            traverse(root.right)

            if not root.left and not root.right:
                all_paths.append(list(path))
            path.pop()

        traverse(root)

        def to_res(path: list[int]):
            return "".join(map(str, [chr(97 + i) for i in path[::-1]]))

        min_res = min([to_res(path) for path in all_paths])
        return min_res

    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        """1457. 二叉树中的伪回文路径
        给你一棵二叉树，每个节点的值为 1 到 9 。
        我们称二叉树中的一条路径是 「伪回文」的，当它满足：路径经过的所有节点值的排列中，存在一个回文序列。
        请你返回从根到叶子节点的所有路径中 伪回文 路径的数目。
        https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/23/palindromic_paths_1.png
        root = [2,3,1,3,1,null,1]
        输出：2
        """

        # 提示排列是回文序列，而不是原本路径，那只需要满足：最多有一个数值是单数，其他数值都是双数
        self.traverse_palindromic(root)
        return self.palindromic_res

    palindromic_counter = {}
    palindromic_res = 0

    def traverse_palindromic(self, root: TreeNode):
        if not root:
            return

        self.palindromic_counter.setdefault(root.val, 0)
        self.palindromic_counter[root.val] += 1

        self.traverse_palindromic(root.left)
        self.traverse_palindromic(root.right)

        if not root.left and not root.right:
            odd = 0
            for _, num in self.palindromic_counter.items():
                if num % 2 == 1:
                    odd += 1
            if odd <= 1:
                self.palindromic_res += 1

        self.palindromic_counter[root.val] -= 1

    def isValidSerialization(self, preorder: str) -> bool:
        """给定一串以逗号分隔的序列，验证它是否是正确的二叉树的前序序列化
        不在重构树的前提下，如果它是一个空节点，我们可以使用一个标记值记录，例如 #
        输入: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
        输出: true
        输入: preorder = "1,#"
        输出: false
        示例 3:

        输入: preorder = "9,#,#,1"
        输出: false
        """
        # 规律：
        # 1. 叶子节点必须有空的两个子节点 `#`
        # 2. 空节点没有子节点

        # 分解问题
        # 1. 当前根节点下一个节点作为左子树根节点，获取左子树的最远节点
        # 2. 以左子树下一个节点作为右子树根节点，获取右子树的最远节点
        # 3. 如果右子树下一个节点跟数组长度一致，则符合要求
        nums = preorder.split(',')
        last = self.get_sub_tree_last(nums, 0)
        if last == -1:
            return False
        if last != len(nums):
            return False
        return True

    def get_sub_tree_last(self, nums, low) -> int:
        """返回子树最远位置"""
        if low >= len(nums):
            return -1

        if nums[low] == '#':
            return low + 1

        left = self.get_sub_tree_last(nums, low + 1)
        if left == -1:
            return -1

        right = self.get_sub_tree_last(nums, left)
        if right == -1:
            return -1

        return right

    def allPossibleFBT(self, n: int) -> list[TreeNode]:
        """894. 所有可能的真二叉树
        给你一个整数 n ，请你找出所有可能含 n 个节点的 真二叉树 ，并以列表形式返回
        真二叉树 是一类二叉树，树中每个节点恰好有 0 或 2 个子节点

        https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/22/fivetrees.png
        如 n=7，7个节点，有五个真子树（不需要标记节点的值，全部为0）

        """
        # 构建树，每个节点有两个处理
        # 1.不添加子节点；2.添加左右两个子节点
        # 3. 左右子树都是单个节点数
        if n <= 0:
            return []
        if n == 1:
            return [TreeNode()]
        if n % 2 == 0:
            return []

        # 分解问题
        # 1. 根节点，假设左子树节点树是 1, 3, 5..，右子树是 n-2, n-4，n-6
        # 2. 将能否满足结果的路径加入左子树路径列表，右子树列表，root 将左右子树列表分别连接，生成新的子树路径列表返回
        res = []
        for i in range(1, n - 1, 2):  # 按照2位数递增，最大为 n-2
            left_list = self.allPossibleFBT(i) or [None]
            right_list = self.allPossibleFBT(n - i - 1) or [None]  # 不包括根节点

            for left in left_list:
                for right in right_list:
                    root = TreeNode()
                    root.left = left
                    root.right = right
                    res.append(root)

        return res

    def delNodes(self, root: TreeNode, to_delete: list[int]) -> list[TreeNode]:
        """1110. 删点成林
        给出二叉树的根节点 root，树上每个节点都有一个不同的值。
        如果节点值在 to_delete 中出现，我们就把该节点从树上删去，最后得到一个森林（一些不相交的树构成的集合）。
        """
        # 分解问题
        # 1. 删除的是根节点，分别对左右子树进行递归删除
        # 2. 否则，将根节点加入结果中
        self.delete_res = []
        self.do_delete(root, to_delete, False)
        return self.delete_res

    def do_delete(self, root: TreeNode, to_delete: list[int], has_parent: bool) -> TreeNode:
        """删除根节点，如果在 to_delete 里面"""
        if not root:
            return None

        deleted = root.val in to_delete
        if not deleted and not has_parent:
            self.delete_res.append(root)

        root.left = self.do_delete(root.left, to_delete, not deleted)
        root.right = self.do_delete(root.right, to_delete, not deleted)
        return root if not deleted else None


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
    root = gen_tree([1, 2, 3, None, 5])
    res = Solution().binaryTreePaths(root)
    print(res)
    assert res == ["1->2->5", "1->3"]

    root = gen_tree([4, 9, 0, 5, 1])
    res = Solution().sumNumbers(root)
    print(res)
    assert res == 1026

    root = gen_tree([1, 2, 3, 4, None, None, None, 5])
    res = Solution().rightSideView(root)
    print(res)
    assert res == [1, 3, 4, 5]

    root = gen_tree([2, 2, 1, None, 1, 0, None, 0])
    res = Solution().smallestFromLeaf(root)
    print(res)
    assert res == "abc"

    root = gen_tree([2, 3, 1, 3, 1, None, 1])
    res = Solution().pseudoPalindromicPaths(root)
    print(res)
    assert res == 2

    assert Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")
    assert not Solution().isValidSerialization("1,#")
    assert not Solution().isValidSerialization("9,#,#,1")

    root = gen_tree([1,2,3,4,5,6,7])
    res = Solution().delNodes(root, [3, 5])
    print(len(res))