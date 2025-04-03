# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class Graph(ABC):
    @abstractmethod
    def addEdge(self, from_: int, to: int, weight: int):
        # 添加一条边（带权重）
        pass

    @abstractmethod
    def removeEdge(self, from_: int, to: int):
        # 删除一条边
        pass

    @abstractmethod
    def hasEdge(self, from_: int, to: int) -> bool:
        # 判断两个节点是否相邻
        pass

    @abstractmethod
    def weight(self, from_: int, to: int) -> int:
        # 返回一条边的权重
        pass

    @abstractmethod
    def neighbors(self, v: int) -> list[tuple[int, int]]:
        # 返回某个节点的所有邻居节点和对应权重
        pass

    @abstractmethod
    def size(self) -> int:
        # 返回节点总数
        pass


# 有向加权图（邻接表）
class NeighborWeightedDigraph:
    class Edge:
        def __init__(self, to, weight):
            self.to = to
            self.weight = weight

    def __init__(self, n):
        self.graph = [[] for _ in range(n)]

    def addEdge(self, from_: int, to: int, weight: int):
        # 添加一条边（带权重）
        for e in self.graph[from_]:
            if e.to == to:
                e.weight = weight
                return

        self.graph[from_].append(self.Edge(to, weight))

    def removeEdge(self, from_: int, to: int):
        # 删除一条边
        self.graph[from_] = [e for e in self.graph[from_] if e.to != to]

    def hasEdge(self, from_: int, to: int) -> bool:
        # 判断两个节点是否相邻
        for e in self.graph[from_]:
            if e.to == to:
                return True
        return False

    def weight(self, from_: int, to: int) -> int:
        # 返回一条边的权重
        for e in self.graph[from_]:
            if e.to == to:
                return e.weight
        return 0

    def neighbors(self, v: int) -> list[tuple[int, int]]:
        # 返回某个节点的所有邻居节点和对应权重
        return [(e.to, e.weight) for e in self.graph[v]]
    
    def size(self):
        visited = {}
        node_map = {}

        def traverse(v):
            if visited.get(v):
                return

            visited[v] = True

            for i in self.neighbors(v):
                traverse(i[0])

                node_map[v] = True
                node_map[i[0]] = True

        for v in range(len(self.graph)):
            traverse(v)

        return len(node_map)


# 有向加权图（邻接矩阵）
class MatrixWeightedDigraph:
    def __init__(self, n):
        # n 维矩阵，每个数字记录有向边的权重
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]

    def addEdge(self, from_: int, to: int, weight: int):
        # 添加一条边（带权重）
        self.matrix[from_][to] = weight

    def removeEdge(self, from_: int, to: int):
        # 删除一条边
        self.matrix[from_][to] = 0

    def hasEdge(self, from_: int, to: int) -> bool:
        # 判断两个节点是否相邻
        return self.matrix[from_][to] > 0

    def weight(self, from_: int, to: int) -> int:
        # 返回一条边的权重
        return self.matrix[from_][to]

    def neighbors(self, v: int) -> list[tuple[int, int]]:
        # 返回某个节点的所有邻居节点和对应权重
        return [(i, w) for i, w in enumerate(self.matrix[v]) if w]
    
    def size(self):
        self._size = 0
        visited = {}

        def traverse(v):
            if visited.get(v):
                return

            self._size + 1
            for i in self.neighbors(v):
                traverse(i[0])

        return self._size


# 无向加权图（邻接表）
class NeighborWeightedUndigraph:
    """使用有向邻接表，打造成双向邻接表"""
    def __init__(self, n):
        self.graph = NeighborWeightedDigraph(n)

    def addEdge(self, from_: int, to: int, weight: int):
        # 添加一条边（带权重）
        self.graph.addEdge(from_, to, weight)
        self.graph.addEdge(to, from_, weight)

    def removeEdge(self, from_: int, to: int):
        # 删除一条边
        self.graph.removeEdge(from_, to)
        self.graph.removeEdge(to, from_)

    def hasEdge(self, from_: int, to: int) -> bool:
        # 判断两个节点是否相邻
        return self.graph.hasEdge(from_, to)

    def weight(self, from_: int, to: int) -> int:
        # 返回一条边的权重
        return self.graph.weight(from_, to)

    def neighbors(self, v: int) -> list[tuple[int, int]]:
        # 返回某个节点的所有邻居节点和对应权重
        return self.graph.neighbors(v)
    
    def size(self):
        self._size = 0
        visited = {}

        def traverse(v):
            if visited.get(v):
                return

            self._size + 1
            for i in self.neighbors(v):
                traverse(i[0])

        return self._size


class MatrixWeightedUndigraph:
    def __init__(self, n):
        self.matrix = MatrixWeightedDigraph(n)

    def addEdge(self, from_: int, to: int, weight: int):
        # 添加一条边（带权重）
        self.matrix.addEdge(from_, to, weight)
        self.matrix.addEdge(to, from_, weight)

    def removeEdge(self, from_: int, to: int):
        # 删除一条边
        self.matrix.removeEdge(from_, to)
        self.matrix.removeEdge(to, from_)

    def hasEdge(self, from_: int, to: int) -> bool:
        # 判断两个节点是否相邻
        return self.matrix.hasEdge(from_, to)

    def weight(self, from_: int, to: int) -> int:
        # 返回一条边的权重
        return self.matrix.weight(from_, to)

    def neighbors(self, v: int) -> list[tuple[int, int]]:
        # 返回某个节点的所有邻居节点和对应权重
        return self.matrix.neighbors(v)
    
    def size(self):
        self._size = 0
        visited = {}

        def traverse(v):
            if visited.get(v):
                return

            self._size + 1
            for i in self.neighbors(v):
                traverse(i[0])

        return self._size


if __name__ == "__main__":
    for graph_class in [NeighborWeightedDigraph, MatrixWeightedDigraph]:
        print(graph_class.__name__)
        graph = graph_class(3)
        graph.addEdge(0, 1, 1)
        graph.addEdge(1, 2, 2)
        graph.addEdge(2, 0, 3)
        graph.addEdge(2, 1, 4)
        assert graph.hasEdge(0, 1)
        assert not graph.hasEdge(1, 0)

        for edge in graph.neighbors(2):
            print(f"{2} <-> {edge[0]}, weight: {edge[1]}")
            assert edge[0] in [0, 1]
            if edge[0] == 0:
                assert edge[1] == 3
            if edge[0] == 1:
                assert edge[1] == 4

        graph.removeEdge(0, 1)
        assert not graph.hasEdge(0, 1)
        assert not graph.hasEdge(1, 0)
        assert graph.hasEdge(2, 0)

        print(graph.size())
        # assert graph.size() == 3

    for graph_class in [NeighborWeightedUndigraph, MatrixWeightedUndigraph]:
        print(graph_class.__name__)
        graph = graph_class(3)
        graph.addEdge(0, 1, 1)
        graph.addEdge(1, 2, 2)
        graph.addEdge(2, 0, 3)
        graph.addEdge(2, 1, 4)

        assert graph.hasEdge(0, 1)
        assert graph.hasEdge(1, 0)
        assert graph.hasEdge(2, 0)

        for edge in graph.neighbors(2):
            print(f"{2} <-> {edge[0]}, weight: {edge[1]}")
            assert edge[0] in [0, 1]
            if edge[0] == 0:
                assert edge[1] == 3
            if edge[0] == 1:
                assert edge[1] == 4

        graph.removeEdge(0, 1)
        assert not graph.hasEdge(0, 1)
        assert not graph.hasEdge(1, 0)

        # assert graph.size() == 3

    print("OK")
