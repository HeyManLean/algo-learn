# -*- coding: utf-8 -*-


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


class DFSSolution:
    """递归遍历二叉树"""
    def all_paths(self, root: TreeNode) -> list:
        
        res = []

        paths = []

        def traverse(node: TreeNode):
            if not node:
                return

            # 前序遍历：先加进去, 到了叶子结点才添加到res
            paths.append(node.val)
            if not any([node.left, node.right]):
                res.append(list(paths))

            traverse(node.left)
            traverse(node.right)

            # 后移出来
            paths.pop()

        traverse(root)

        return res
    
    def max_depth(self, root: TreeNode) -> int:
        self.depth = 0
        self.max_depth = 0

        def traverse(node: TreeNode):
            if not node:
                return

            self.depth += 1
            self.max_depth = max(self.max_depth, self.depth)

            traverse(node.left)
            traverse(node.right)

            self.depth -= 1

        traverse(root)

        return self.max_depth

    def min_depth(self, root: TreeNode) -> int:
        import math
        self.depth = 0
        self._min_depth = math.inf

        def traverse(node: TreeNode):
            if not node:
                return

            self.depth += 1
            if not any([node.left, node.right]):
                self._min_depth = min(self.depth, self._min_depth)

            traverse(node.left)
            traverse(node.right)
            self.depth -= 1

        traverse(root)
        return max(self._min_depth, 0)


class BFSSolution:
    """层序遍历二叉树"""
    def all_paths(self, root: TreeNode) -> list:
        """层序遍历，需要将父节点信息传递到子节点，使用state节点保存父节点信息"""
        class StateTreeNode:
            def __init__(self, node: TreeNode, state: list):
                self.node = node
                self.state = state

        q = [StateTreeNode(root, [])]
        res = []
        while q:
            count = len(q)
            for snode in q[:count]:
                paths = snode.state + [snode.node.val]

                if not any([snode.node.left, snode.node.right]):
                    res.append(paths)
                    continue

                if snode.node.left:
                    q.append(StateTreeNode(snode.node.left, paths))
                if snode.node.right:
                    q.append(StateTreeNode(snode.node.right, paths))
            q = q[count:]
        return res

    def max_depth(self, root: TreeNode) -> int:
        q = [root]
        depth = 0
        while q:
            depth += 1
            count = len(q)
            for node in q[:count]:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            q = q[count:]

        return depth

    def min_depth(self, root: TreeNode) -> int:
        q = [root]
        depth = 0
        while q:
            depth += 1
            count = len(q)
            for node in q[:count]:
                if not node:
                    continue

                # 当前层遇到叶子结点，就是最小深度
                if not any([node.left, node.right]):
                    return depth

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            q = q[count:]

        return depth


if __name__ == "__main__":
    for solution in [DFSSolution, BFSSolution]:
        print(solution.__name__)

        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        print(solution().all_paths(root))
        assert solution().all_paths(root) == [[3, 9], [3, 20, 15], [3, 20, 7]]
        assert solution().min_depth(root) == 2
        assert solution().max_depth(root) == 3

        root = TreeNode(2)
        root.left = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.left.left = TreeNode(5)
        root.left.left.left.left = TreeNode(6)
        print(solution().all_paths(root))
        assert solution().all_paths(root) == [[2, 3, 4, 5, 6]]
        assert solution().min_depth(root) == 5
        assert solution().max_depth(root) == 5
