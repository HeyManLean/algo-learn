# -*- coding: utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder: list[int], inorder: list[int]):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        # 前序+中序序列重构二叉树
        if not preorder:
            return None

        # 前序遍历第一个值就是根节点
        root = TreeNode(preorder[0])
        pos = inorder.index(preorder[0])

        # 中序遍历，根节点值左右划分为两块，左边是左子树，右边是右子树
        left_inorder = inorder[:pos]
        right_inorder = inorder[pos+1:]

        # 前序遍历与左子树对应区间，为根节点左边根中序遍历个数一直的区间
        left_preorder = preorder[1:len(left_inorder) + 1]
        # 前序遍历与右子树对应区间
        right_preorder = preorder[len(left_inorder)+1:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root


def gen_tree(arr: list[int]):
    root = TreeNode(arr[0])

    q = [root]
    i = 0
    while q:
        cur = q.pop(0)
        if i + 1 < len(arr) and arr[i + 1]:
            cur.left = TreeNode(arr[i + 1])
            q.append(cur.left)
        if i + 2 < len(arr) and arr[i + 2]:
            cur.right = TreeNode(arr[i + 2])
            q.append(cur.right)
        i += 2

    return root


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # 将二叉树按照层序遍历方式生成一个数组，对于叶子节点，需要将其左右指针改为 #
        # 构造一个完全二叉树
        if not root:
            return ""

        q = [root]
        nums = [str(root.val)]
        while q:
            node = q.pop(0)

            if node.left:
                q.append(node.left)
                nums.append(str(node.left.val))
            else:
                nums.append("#")

            if node.right:
                q.append(node.right)
                nums.append(str(node.right.val))
            else:
                nums.append("#")

        return ",".join(nums)

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # 解析一个完全二叉树
        if not data:
            return None

        nums = data.split(",")
        root = TreeNode(int(nums[0]))
        q = [root]
        i = 0

        while q:
            node = q.pop(0)
            if i + 1 < len(nums) and nums[i + 1] != "#":
                node.left = TreeNode(int(nums[i + 1]))
                q.append(node.left)
            if i + 2 < len(nums) and nums[i + 2] != "#":
                node.right = TreeNode(int(nums[i + 2]))
                q.append(node.right)
            i += 2

        return root


if __name__ == "__main__":
    root = gen_tree([1, 2, 3, None, None, 4, 5])
    s = Codec().serialize(root)
    print(s)
    new_root = Codec().deserialize(s)

    
