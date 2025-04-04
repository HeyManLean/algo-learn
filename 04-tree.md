# 二叉树

## 思维模式

抽象出二叉树节点，需要在（前/中/后序位置）做什么
- 遍历：递归遍历函数+外部变量，得出结果
- 分解：利用子问题的结果，推到出原问题的答案

### 分解问题

将一个规模较大的问题分解为规模更小的子问题，通过子问题的解得到原问题的解

结合二叉树属性，可以先算出子树的解，再得到当前节点的解

```py

def fib(n int) -> int:
    if n < 2:
        return n
    
    n1 = fib(n - 1)
    n2 = fib(n - 2)
    return n1 + n2


# 最大深度问题
class Solution:
    def max_depth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_max = self.max_depth(root.left)
        right_max = self.max_depth(root.right)
        return max(left_max, right_max) + 1
```


### 遍历问题


```py
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class MyTree:
    def traverse(self, node: TreeNode):
        """DFS 递归"""
        if not node:
            return

        # 前序遍历：父节点->左节点->右节点
        self.traverse(node.left)
        # 中序遍历：左节点->父节点->右节点
        self.traverse(node.right)
        # 后序遍历：左节点->右节点->父节点

    def bfs(self, node: TreeNode):
        """BFS 层序遍历"""
        q = [node]
        while q:
            node = q[0]
            q = q[1:]
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

# 最大深度问题
class Solution:
    def __init__(self):
        self.depth = 0
        self.res = 0

    def max_depth(self, root:TreeNode):
        self.traverse(root)
        return self.res

    def traverse(self, root:TreeNode):
        if not root:
            return

        # 前序遍历，进入节点
        self.depth += 1

        # 叶子节点
        if not root.right and not root.left:
            self.res = max(self.res, self.depth)
        self.traverse(root.left)
        self.traverse(root.right)

        # 后序遍历，离开节点
        self.depth -= 1
```


## 构造二叉树

### 从前序与中序遍历序列构造二叉树（105）

前提是元素不重复

```py
class Solution(object):
    def buildTree(self, preorder: list[int], inorder: list[int]):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
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

```

### 从中序与后序遍历序列构造二叉树（106）

前提是元素不重复
```py
class Solution(object):
    def buildTree(self, inorder: list[int], postorder: list[int]):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not inorder:
            return None
        
        # 后序遍历最后一个节点就是根节点
        root = TreeNode(postorder[-1])
        root_pos = inorder.index(postorder[-1])

        # 中序遍历序列中，root 左边是左子树，右边是右子树
        left_inorder = inorder[:root_pos]
        right_inorder = inorder[root_pos+1:]

        # 后序遍历序列中，最前面数量跟左子树数量一致的，是左子树的后续遍历
        left_postorder = postorder[:len(left_inorder)]
        right_postorder = postorder[len(left_inorder):-1]

        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)
        return root
```

### 通过后序和前序遍历结果构造二叉树（889）

前提是元素不重复
```py
class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder:
            return None

        # 前序遍历第一个节点认为是根节点
        root = TreeNode(preorder[0])

        # 找左子树，前序遍历第一个值，后序遍历最后一个值一致，可以形成一个子树
        if len(preorder) <= 1:
            return root

        # 左子树：前序遍历第一个值和后续遍历最后一个值相等
        left = preorder[1]
        left_pos = postorder.index(left)
        left_preorder = preorder[1:left_pos + 2]
        left_postorder = postorder[:left_pos+1]
        root.left = self.constructFromPrePost(left_preorder, left_postorder)

        right_preorder = preorder[left_pos+2:]
        right_postorder = postorder[left_pos+1:-1]
        root.right = self.constructFromPrePost(right_preorder, right_postorder)

        return root
```

## 序列化

### 二叉树的序列化与反序列化（297）

中序遍历解法（前中后也可以）

```py
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
```