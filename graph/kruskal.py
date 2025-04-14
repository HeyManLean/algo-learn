# -*- coding: utf-8 -*-


"""
Kruskal 最小生成树算法

树：无环连通图

找到一个最小的加权树，能否连通所有节点，且没有环，权重最小

将边按照权重从小到大排序，对边进行遍历，如果不会构成环，则加入到树中，直到连通变量为 1
"""


class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
        self._count = n

    def find_root(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find_root(self.parent[p])
        return self.parent[p]

    def connected(self, p, q):
        return self.find_root(p) == self.find_root(q)

    def union(self, p, q):
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

    def count(self):
        return self._count


class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        """261. 以图判树

        判断图是否是一棵树：连通分量的数量为1，且无环

        n = 5
        edges = [[0,1], [0,2], [0,3], [1,4]]
        """
        uf = UF(n)

        for edge in edges:
            p, q = edge
            if uf.connected(p, q):
                return False
            uf.union(p, q)

        return uf.count() == 1

    def minimumCost(self, n: int, connections: list[list[int]]) -> int:
        """1135. 最低成本联通所有城市

        给你输入数组 conections，其中 connections[i] = [xi, yi, costi]
        表示将城市 xi 和城市 yi 连接所要的costi（连接是双向的），
        请你计算连接所有城市的最小成本。
        """
        # 按照 cost 将边从小到大排序
        # 对边进行遍历，如果不存在环则加入到树中，否则跳过
        uf = UF(n + 1)

        # 按照 cost 将边排序
        conns = sorted(connections, key=lambda x: x[-1])

        res = 0
        for conn in conns:
            p, q, cost = conn
            if uf.connected(p, q):
                continue
            uf.union(p, q)
            res += cost

            if uf.count() == 1:
                break

        return res

    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        """1584. 连接所有点的最小费用
        给你一个points 数组，表示 2D 平面上的一些点，其中 points[i] = [xi, yi] 。

        连接点 [xi, yi] 和点 [xj, yj] 的费用为它们之间的
        曼哈顿距离 ：|xi - xj| + |yi - yj| ，其中 |val| 表示 val 的绝对值。

        请你返回将所有点连接的最小总费用。只有任意两点之间 有且仅有 一条简单路径时，才认为所有点都已连接。
        """
        id_map = {}
        n = 0
        for point in points:
            code = f'{point[0]}_{point[1]}'
            if code not in id_map:
                id_map[code] = n
                n += 1

        # 对点之间建立边和权重，并排序
        edges = []
        for i, point_i in enumerate(points):
            for j in range(i + 1, len(points)):
                point_j = points[j]

                edges.append([
                    id_map[f'{point_i[0]}_{point_i[1]}'],
                    id_map[f'{point_j[0]}_{point_j[1]}'],
                    abs(point_i[0] - point_j[0]) + abs(point_i[1] - point_j[1])
                ])

        edges.sort(key=lambda x: x[-1])

        uf = UF(n)
        res = 0
        for edge in edges:
            p, q, cost = edge
            if uf.connected(p, q):
                continue
            uf.union(p, q)
            res += cost

            if uf.count() == 1:
                break

        return res


if __name__ == "__main__":
    assert Solution().validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])
    assert not Solution().validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])

    assert (
        Solution().minimumCost(
            6,
            [
                [1, 2, 3],
                [1, 3, 1],
                [2, 3, 1],
                [2, 4, 6],
                [3, 4, 5],
                [4, 5, 2],
                [5, 6, 3],
                [3, 6, 10],
                [1, 6, 100],
            ],
        )
        == 12
    )

    assert (
        Solution().minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]) == 20
    )
    assert Solution().minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]) == 18
    assert Solution().minCostConnectPoints([[0, 0], [1, 1], [1, 0], [-1, 1]]) == 4
    assert (
        Solution().minCostConnectPoints([[-1000000, -1000000], [1000000, 1000000]])
        == 4000000
    )
    assert Solution().minCostConnectPoints([[0, 0]]) == 0

    print("OK")
