# -*- coding: utf-8 -*-


class UF:
    """并查集，高效解决无向图的连通性

    自反性：p和q自身也是连通的
    对称性：p和q连通，则q和p也连通
    传递性：p和q连通，q和r连通，则p和r也连通

    结构：森林结构，维护多个多叉树
    1. 连接节点只需要将两个多叉树根节点相连，将其中一个根节点接到另一个根节点下面
    2. 多叉树的数量，等于连通分量的数量

    树的高度决定操作的时间复杂度，需要保持高度在常量
    1. 使用parent往上找到根节点
    3. 压缩路径：将节点的父节点改为根节点，保持高度为 1

    """

    def __init__(self, n: int):
        # 初始化时，节点的根节点指向自己
        # 有时需要将点编码为 n 里面的数值
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]
        self._count = n

    def union(self, p: int, q: int):
        """将两个节点连接"""
        # 找到两个节点所在树的根节点，连接根节点
        # 平衡两个树：小树接到大树下面，维护每棵树的节点数量
        p_root = self.find_root(p)
        q_root = self.find_root(q)
        if p_root == q_root:
            return
        
        # self.parent[q_root] = p_root
        # 优化，记录树的节点数，将节点数小的数接到节点数大的树下面，保持平衡
        if self.size[p_root] >= self.size[q_root]:
            self.parent[q_root] = p_root
            self.size[p_root] += self.size[q_root]
        else:
            self.parent[p_root] = q_root
            self.size[q_root] += self.size[p_root]

        self._count -= 1

    def connected(self, p: int, q: int) -> bool:
        """判断两个节点是否相连"""
        # 判断两个节点所在树根节点是否一致
        return self.find_root(p) == self.find_root(q)

    def find_root(self, p: int) -> int:
        """找到节点所在树的根节点"""
        # 沿着 parent 找到根节点，即parent[i] = i
        # 压缩路径：将沿路的节点的 parent 指向根节点，保持高度为 1
        if self.parent[p] != p:
            self.parent[p] = self.find_root(self.parent[p])
        return self.parent[p]

    def count(self) -> int:
        """计算连通变量的数量"""
        # 返回树数量
        return self._count


class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:
        """990. 等式方程的可满足性

        给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，
        并采用两种不同的形式之一："a==b" 或 "a!=b"。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。

        只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。
        输入：["a==b","b!=a"]
        输出：false

        输入：["b==a","a==b"]
        输出：true

        输入：["a==b","b==c","a==c"]
        输出：true

        输入：["a==b","b!=c","c==a"]
        输出：false

        输入：["c==c","b==d","x!=z"]
        输出：true
        """
        # 等号传递性，判断不同节点的连通性
        # 使用并查集
        # 将变量映射到数组索引

        char_map = {}
        pos = 0
        for equa in equations:
            if equa[0] not in char_map:
                char_map[equa[0]] = pos
                pos += 1
            if equa[-1] not in char_map:
                char_map[equa[-1]] = pos
                pos += 1

        uf = UF(len(char_map))
        for equa in equations:
            left = char_map[equa[0]]
            right = char_map[equa[-1]]

            if equa[1:3] == "==":
                uf.union(left, right)

        for equa in equations:
            left = char_map[equa[0]]
            right = char_map[equa[-1]]
            if equa[1:3] == "!=" and uf.connected(left, right):
                return False

        return True

    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        """547. 省份数量
        有 n 个城市，其中一些彼此相连，另一些没有相连。
        如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。

        省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。

        给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1
        表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。

        返回矩阵中 省份 的数量。

        输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
        输出：2

        输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
        输出：3
        """
        uf = UF(len(isConnected))

        for i, row in enumerate(isConnected):
            for j, connected in enumerate(row):
                if connected:
                    uf.union(i, j)

        return uf.count()

    def validateBinaryTreeNodes(
        self, n: int, leftChild: list[int], rightChild: list[int]
    ) -> bool:
        """1361.验证二叉树
        二叉树上有 n 个节点，按从 0 到 n - 1 编号，其中节点 i 的两个子节点分别是 leftChild[i] 和 rightChild[i]。

        只有 所有 节点能够形成且 只 形成 一颗 有效的二叉树时，返回 true；否则返回 false。
        如果节点 i 没有左子节点，那么 leftChild[i] 就等于 -1。右子节点也符合该规则。

        输入：n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
        输出：true

        输入：n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
        输出：false

        输入：n = 2, leftChild = [1,0], rightChild = [-1,-1]
        输出：false
        """
        uf = UF(n)
        is_children = {}  # 记录节点是否已经是子节点

        for i in range(n):
            if leftChild[i] != -1:
                # 已经是子节点，返回 False
                if leftChild[i] in is_children:
                    return False

                # 已经连接过，返回 False
                if uf.connected(i, leftChild[i]):
                    return False
                uf.union(i, leftChild[i])
                is_children[leftChild[i]] = True

            if rightChild[i] != -1:
                if rightChild[i] in is_children:
                    return False
                if uf.connected(i, rightChild[i]):
                    return False
                uf.union(i, rightChild[i])
                is_children[rightChild[i]] = True

        return uf.count() == 1

    def removeStones(self, stones: list[list[int]]) -> int:
        """947. 移除最多的同行或同列石头
        n 块石头放置在二维平面中的一些整数坐标点上。每个坐标点上最多只能有一块石头。

        如果一块石头的 同行或者同列 上有其他石头存在，那么就可以移除这块石头。
        给你一个长度为 n 的数组 stones ，其中 stones[i] = [xi, yi] 表示第 i 块石头的位置，返回 可以移除的石子 的最大数量。

        输入：stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
        输出：5
        解释：一种移除 5 块石头的方法如下所示：
        1. 移除石头 [2,2] ，因为它和 [2,1] 同行。
        2. 移除石头 [2,1] ，因为它和 [0,1] 同列。
        3. 移除石头 [1,2] ，因为它和 [1,0] 同行。
        4. 移除石头 [1,0] ，因为它和 [0,0] 同列。
        5. 移除石头 [0,1] ，因为它和 [0,0] 同行。
        石头 [0,0] 不能移除，因为它没有与另一块石头同行/列。

        输入：stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
        输出：3

        输入：stones = [[0,0]]
        输出：0
        解释：[0,0] 是平面上唯一一块石头，所以不可以移除它。
        """
        # 节点在同一行，则表示连通，在同一列也表示连通
        # 节点总数 - 连通分量数量，就是需要移除的石头数量

        # 将节点映射到 n 位的索引
        stone_map = {}
        for i, s in enumerate(stones):
            stone_map[s[0] * 10000 + s[1]] = i

        # 记录每行的石头编码
        row_map = {}
        col_map = {}
        for s in stones:
            row_map.setdefault(s[0], []).append(s[0] * 10000 + s[1])
            col_map.setdefault(s[1], []).append(s[0] * 10000 + s[1])

        # 建立连通性
        uf = UF(len(stones))
        for _, points in row_map.items():
            first = points[0]
            for point in points[1:]:
                uf.union(stone_map[first], stone_map[point])

        for _, points in col_map.items():
            first = points[0]
            for point in points[1:]:
                uf.union(stone_map[first], stone_map[point])

        return len(stones) - uf.count()


if __name__ == "__main__":
    assert not Solution().equationsPossible(["a==b", "b!=a"])
    assert Solution().equationsPossible(["a==b", "b==a"])
    assert Solution().equationsPossible(["a==b", "b==c", "a==c"])
    assert not Solution().equationsPossible(["a==b", "b!=c", "c==a"])
    assert Solution().equationsPossible(["c==c", "b==d", "x!=z"])
    assert Solution().equationsPossible(["c==c", "f!=a", "f==b", "b==c"])

    assert Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
    assert Solution().findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3

    assert Solution().validateBinaryTreeNodes(
        n=4, leftChild=[1, -1, 3, -1], rightChild=[2, -1, -1, -1]
    )
    assert not Solution().validateBinaryTreeNodes(
        n=4, leftChild=[1, -1, 3, -1], rightChild=[2, 3, -1, -1]
    )
    assert not Solution().validateBinaryTreeNodes(
        n=2, leftChild=[1, 0], rightChild=[-1, -1]
    )

    assert (
        Solution().removeStones(
            stones=[[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
        )
        == 5
    )
    assert (
        Solution().removeStones(stones=[[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]])
        == 3
    )
    assert Solution().removeStones(stones=[[0, 0]]) == 0
    print("OK")
