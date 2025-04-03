# -*- coding: utf-8 -*-
class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.left = None
        self.right = None

        self.size = 1  # 表示以当前节点为根节点的子树，包含节点的数量


class TreeMap:
    """二叉搜索树，BST 左边节点比右边节点小，不支持自动平衡"""
    def __init__(self):
        self.root = None

    def put(self, key, val):
        self.root = self._put(self.root, key, val)

    def _put(self, root: TreeNode, key, val) -> TreeNode:
        """root 表示当前子树的根节点"""
        if not root:
            return TreeNode(key, val)
        if key == root.key:
            root.val = val
            return root

        if key < root.key:
            root.left = self._put(root.left, key, val)
        else:
            root.right = self._put(root.right, key, val)

        root.size += 1
        return root

    def get(self, key):
        return self._get(self.root, key)

    def _get(self, root, key):
        if not root:
            return None
        
        if key == root.key:
            return root.val
        elif key < root.key:
            return self._get(root.left, key)
        else:
            return self._get(root.right, key)

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, root, key):
        if not root:
            return None
        
        if key < root.key:
            root.left = self._remove(root.left, key)
        elif key > root.key:
            root.right = self._remove(root.right, key)

        if key == root.key:
            # 无左节点，返回右节点替换当前节点
            if not root.left:
                return root.right
            # 无右节点，返回左节点替换当前节点
            if not root.right:
                return root.left
            # 有左右节点，取右节点最小（最左边）节点替换当前节点，后移除掉右节点最小节点
            temp = root.right
            while temp.left:
                temp = temp.left

            root.key = temp.key
            root.val = temp.val
            root.right = self._remove(root.right, temp.key)

        root.size = self.get_size(root.left) + self.get_size(root.right)
        return root

    def contains_key(self, key) -> bool:
        # 可以递归，也可以遍历
        root = self.root

        while root:
            if key == root.key:
                return True
            if key < root.key:
                root = root.left
            else:
                root = root.right
        return False

    def keys(self):
        """返回所有键的集合，结果有序，复杂度"""
        # 需要保证顺序，必须中序遍历，使用DFS
        keys = []

        def traverse(root: TreeNode):
            if not root:
                return

            traverse(root.left)
            keys.append(root.key)
            traverse(root.right)

        traverse(self.root)

        return keys

    def first_key(self):
        if not self.root:
            return None

        root = self.root
        while root.left:
            root = root.left

        return root.key

    def last_key(self):
        if not self.root:
            return None

        root = self.root
        while root.right:
            root = root.right

        return root.key

    def floor_key(self, key):
        """ 查找小于等于 key 的最大键，复杂度 O(logN)"""
        root = self.root
        max_key = None
        while root:
            if key == root.key:
                return root.key
            if key < root.key:
                root = root.left
            else:
                max_key = root.key
                root = root.right

        return max_key
    
    def ceiling_key(self, key):
        """ 查找大于等于 key 的最小键，复杂度 O(logN)"""
        root = self.root
        min_key = None
        while root:
            if key == root.key:
                return key
            if key < root.key:
                min_key = root.key
                root = root.left
            else:
                root = root.right
        return min_key

    def select_key(self, rank):
        """ 查找排名为 k 的键，复杂度 O(logN)"""
        # 通过 size 可以减少递归查询的次数
        root = self.root

        # 遍历方式
        base = 0
        while root:
            root_rank = self.get_size(root.left) + 1 + base
            if rank == root_rank:
                return root.key
            if rank < root_rank:
                root = root.left
            else:
                # 每次向右边搜索时，需要把左边节点数加上
                base += self.get_size(root.left) + 1
                root = root.right

        return None

    def rank_key(self, key):
        """查找键 key 的排名，复杂度 O(logN)"""
        # 递归方式
        def traverse(node, rank=0):
            if not node:
                return
            if key == node.key:
                return self.get_size(node.left) + 1 + rank
            if key < node.key:
                return traverse(node.left)
            else:
                return traverse(node.right, rank + self.get_size(node.left) + 1)

        return traverse(self.root)

    def range_keys(self, low, high):
        """区间查找，复杂度 O(logN + M)，M 为区间大小"""
        low_key = self.select_key(low) or self.first_key()
        high_key = self.select_key(high - 1) or self.last_key()
        keys = []

        def traverse(node):
            if not node:
                return

            # 中序遍历保持顺序

            # 如果当前节点 key < low_key, 则左子树不需要遍历
            if node.key >= low_key:
                traverse(node.left)

            if low_key <= node.key <= high_key:
                keys.append(node.key)

            # 如果当前节点 key > high_key，则右子树不需要遍历
            if node.key <= high_key:
                traverse(node.right)

        traverse(self.root)
        return keys

    def get_size(self, root):
        if not root:
            return 0
        return root.size


if __name__ == '__main__':
    tmap = TreeMap()
    tmap.put('d', 2)
    tmap.put('b', 5)
    tmap.put('a', 1)
    tmap.put('f', 9)
    tmap.put('e', 10)
    tmap.put('g', 3)
    assert tmap.keys() == ['a', 'b', 'd', 'e', 'f', 'g']

    """
             d
            /  \
           b    f
          /    /  \
        a     e    g
    """

    tmap.remove('f')
    assert tmap.keys() == ['a', 'b', 'd', 'e', 'g']

    """
             d
            /  \
           b    g
          /    /
        a     e
    """


    assert tmap.get('d') == 2
    assert tmap.get('e') == 10
    assert tmap.first_key() == 'a'
    assert tmap.last_key() == 'g'
    assert tmap.floor_key('c') == 'b'
    assert tmap.ceiling_key('c') == 'd'

    assert tmap.rank_key('b') == 2
    assert tmap.rank_key('g') == 5
    assert tmap.select_key(2) == 'b'
    assert tmap.select_key(5) == 'g'
    assert tmap.range_keys(2, 4) == ['b', 'd']

    print("OK")
