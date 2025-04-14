# 二叉树

## 1.思维模式

抽象出二叉树节点，需要在（前/中/后序位置）做什么
- 遍历：递归遍历函数+外部变量，得出结果
- 分解：利用子问题的结果，推到出原问题的答案

## 2.分解问题

将一个规模较大的问题分解为规模更小的子问题，通过子问题的解得到原问题的解
- 结合二叉树属性，可以先算出子树的解，再得到当前节点的解
- 需要返回值

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


## 3.遍历问题


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


### 二叉树所有路径（257）

递归遍历，找到叶子节点，将经过路径加入结果中

```py
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
```

### 求根节点到叶节点数字之和（129）

递归遍历，将路径加入结果中，最后算每个路径的和

```py
class Solution:
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
```


### 二叉树的右视图（199）

层序遍历，将每一层最右侧的节点值加入结果中

```py
class Solution:
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
```

### 二叉树中的伪回文路径（1457）

伪回文路径，只有一个奇数个数的值，其他都是偶数
- 递归遍历所有路径，到了叶子节点，计算当前路径的奇数个数的值

```py
class Solution:
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
```


## 4. 构造二叉树

### 从前序与中序遍历序列构造二叉树（105）

前提是元素不重复
- 前序遍历第一个值就是根节点
- 将中序遍历序列，按照当前根节点值位置，将其左右划分为两块，左边是左子树，右边是右子树，进行递归创建左右子树

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
- 后序遍历最后一个节点就是根节点
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

## 5.序列化

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

## 6.公共祖先

### 二叉树的最近公共祖先 IV（1676）

递归遍历，找到一个节点，满足一下条件均认为是最近公共祖先
- p 和 q 分别在该节点左右子树中
- p 在 q 的子树中 或 q 在 p 的子树中

```py
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
```


### 正确的二叉树的前序序列化


分解问题
- 当前根节点下一个节点作为左子树根节点，获取左子树的最远节点
- 以左子树下一个节点作为右子树根节点，获取右子树的最远节点
- 如果右子树下一个节点跟数组长度一致，则符合要求


```py
class Solution:
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
```

## 7.二叉搜索树

### 遍历: 验证二叉搜索树（98）

```py
class Solution:
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
```


### 构造: 不同的二叉搜索树 II（95）

当前节点
1. 按照 0~n-1 将节点个数分配到左子树，构建出多个左子树
2. 将剩余除了当前节点，其他节点数分配给右子树，构建出多个右子树
3. 排列组合，当前节点左右连接上左右子树，生成结果集

```py
class Solution:
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
```


### 插入或修改：二叉搜索树中的插入操作（701）

二分搜索
1. 如果当前值等于当前节点值，则返回当前节点
2. 如果小于当前节点值，则对左子树进行插入操作，返回新的左子树节点
3. 如果大于当前节点值，则对右子树进行插入操作，返回新的右子树节点

```py
class Solution:
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
```


### 删除：删除二叉搜索树中的节点（450）

1. 如果找不到该值，则直接返回
2. 如果当前节点值跟删除值一样：
    - 如果没有右子树，返回左节点
    - 如果没有左子树，返回右节点
    - 否则，如果当前节点有右子树，则将该节点赋值为右子树最小值，并将右子树最小节点删除

```py
class Solution:
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
```

## 8. 线段树

用于对区间聚合值进行频繁读取的场景，更新支持区间更新，并算出区间聚合值

结构：
1. 每个节点维护区间的聚合值，`[start,end]`
2. 访问该节点区间的子区间时，需要进一步二分初始化左右节点
    - 左节点：`[start,mid]`
    - 右节点: `[mid+1,end]`

更新：
1. 懒加载，先更新当前区间的值，并标记 assign 为当前缓存值，等到访问子区间时需要将 assign 往下传递
2. 子区间的取值为：`(end-start)*val`

查询：
1. 判断查询的区间是在当前节点区间中点的左侧，还是右侧，进行二分递归查询


```py

class RangeSegmentNode:
    def __init__(self, start, end, val=0, left=None, right=None):
        self.start = start
        self.end = end
        self.val = val
        self.left = left  # type:RangeSegmentNode
        self.right = right  # type:RangeSegmentNode
        self.has_assign = False  # 判断是否有值需要往下传递
        self.assign = 0         # 缓存需要向下传递的值


class SumRangeSegmentTree:
    """懒加载线段树（求和）

    更新上级线段树时，先对该范围的上层线段树进行更新，
    并记录更新的值，等到下次要范围下层线段树时，将更新的值传递到下层

    主要用于范围更新和范围取值
    """
    def __init__(self, start=0, end=1000, default=0):
        self.root = RangeSegmentNode(start, end, (end - start + 1) * default)
        self.default = default

    def init_children_node(self, node: RangeSegmentNode):
        if node.start >= node.end:
            return

        mid = node.start + (node.end - node.start) // 2
        if not node.left:
            node.left = RangeSegmentNode(node.start, mid, self.default)
        if not node.right:
            node.right = RangeSegmentNode(mid + 1, node.end, self.default)

    def push_down(self, node: RangeSegmentNode):
        """先把左右节点当前的 assign 下钻，再将当前节点的 assign 同步到左右节点"""
        if not node.has_assign:
            return

        self.init_children_node(node)

        # 一般为覆盖原有的值，不需要将子节点的assign继续往下传递，直接将当前节点assign覆盖
        left = node.left
        right = node.right

        left.val = (left.end - left.start + 1) * node.assign
        left.has_assign = True
        left.assign = node.assign

        right.val = (right.end - right.start + 1) * node.assign
        right.has_assign = True
        right.assign = node.assign

        node.has_assign = False

    def range_update(self, start, end, val):
        return self._range_update(self.root, start, end, val)

    def _range_update(self, node: RangeSegmentNode, start, end, val):
        """更新范围，如果节点范围在需要更新的范围内，则更新节点的值，并设置懒加载数值"""
        if node.start >= start and node.end <= end:
            node.val = (node.end - node.start + 1) * val
            node.has_assign = True
            node.assign = val
            return

        self.init_children_node(node)
        self.push_down(node)

        mid = node.start + (node.end - node.start) // 2
        if end <= mid:
            self._range_update(node.left, start, end, val)
        elif start > mid:
            self._range_update(node.right, start, end, val)
        else:
            self._range_update(node.left, start, mid, val)
            self._range_update(node.right, mid + 1, end, val)

        # 当前节点的值
        node.val = node.left.val + node.right.val


    def query(self, start, end):
        return self._query(self.root, start, end)

    def _query(self, node: RangeSegmentNode, start, end):
        """对node的值进行二分，判断区域左右进行递归"""
        if start > end:
            return 0

        # 如果目标区间包含了当前区间，则返回当前区间的值
        if start <= node.start and end >= node.end:
            return node.val

        self.init_children_node(node)
        self.push_down(node)

        mid = node.start + (node.end - node.start) // 2
        if end <= mid:
            return self._query(node.left, start, end)
        if start > mid:
            return self._query(node.right, start, end)

        return self._query(node.left, start, mid) + self._query(node.right, mid + 1, end)
```

## 9. 二叉堆

二叉堆是一种数据结构，主要用于优先级队列的场景，从多个元素中多次获取最小或最大值
- 涉及最值问题
- 第 K 大数值

二叉堆结构，使用数组表示一棵完美二叉树
- 根节点都小于（或大于）左右两个节点
- 通过根节点获取左右节点位置：
    - 左节点: `n * 2 + 1`
    - 右节点: `n * 2 + 2`
- 通过子节点获取根节点: `(n - 1) // 2`

构造二叉堆：
- 新增节点：先加到数组尾部，向上跟父节点比较，如果较小（或较大）则交换
- 删除节点：将节点跟尾部节点值交换，向下跟（较小或较大）的子节点进行比较并交换

```py

class MinPriorityQueue:
    # 创建一个容量为 capacity 的最小优先级队列
    def __init__(self, capacity: int):
        self.heap = [None] * capacity
        self.size = 0

    # 向队列中插入一个元素
    def push(self, x: int):
        if self.is_full():
            raise ValueError('queue full')

        last = self.size
        self.heap[last] = x
        self.size += 1
        self.swim(last)

    # 返回队列中的最小元素（堆顶元素）
    def peek(self) -> int:
        return self.heap[0]

    # 删除并返回队列中的最小元素（堆顶元素）
    def pop(self) -> int:
        if self.is_empty():
            raise ValueError('queue empty')
        
        val = self.heap[0]

        self.heap[0] = self.heap[self.size - 1]
        # self.heap[self.size - 1] = None  # 可以不用删除
        self.size -= 1

        self.sink(0)
        return val

    def swim(self, node):
        """向上上浮，跟父节点交换"""
        parent = self.parent(node)
        if parent < 0:
            return

        # 当前节点小于父节点，跟父节点交换
        if self.heap[node] < self.heap[parent]:
            self.swap(node, parent)
            return self.swim(parent)

    def sink(self, node):
        """向下下沉，跟子节点交换"""
        left = self.left(node)
        if left >= self.size:
            return

        min_node = left
        right = self.right(node)
        if right < self.size and self.heap[left] > self.heap[right]:
            min_node = right

        if self.heap[min_node] < self.heap[node]:
            self.swap(min_node, node)
            self.sink(min_node)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def parent(self, node):
        return (node - 1) // 2
    
    def left(self, node):
        return node * 2 + 1
    
    def right(self, node):
        return node * 2 + 2
    
    def is_full(self):
        return len(self.heap) == self.size
    
    def is_empty(self):
        return self.size == 0
```