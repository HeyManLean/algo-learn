# -*- coding: utf-8 -*-


class Solution:
    def __init__(self):
        self.has_circle = False
        self.on_path = {}
        self.visited = {}
        self.postorder = []

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

        在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，
        其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。

        例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
        输入：numCourses = 2, prerequisites = [[1,0]]
        输出：true

        输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
        输出：false

        1 <= numCourses <= 2000
        """
        # 环检测
        # 遍历图的所有路径，分别检查每个路径是否有环
        graph = self.build_graph(numCourses, prerequisites)
        for i in range(len(graph)):
            self.traverse(graph, i)

        return not self.has_circle

    def traverse(self, graph, i):
        """遍历邻接表"""
        # 已经有环直接返回
        if self.has_circle:
            return

        # 检测出同一个路径重复访问同一个节点，返回有环
        if i in self.on_path:
            self.has_circle = True
            return

        # 已经访问过，避免重复访问
        if i in self.visited:
            return
        self.visited[i] = 1

        # 记录当前节点已经在该路径上
        self.on_path[i] = 1
        for to in graph[i]:
            self.traverse(graph, to)
        self.postorder.append(i)
        # 离开该节点
        self.on_path.pop(i)

    def build_graph(self, num: int, prerequisites: list[list[int]]):
        """建立邻接表"""
        graph = [[] for i in range(num)]
        for target, source in prerequisites:
            graph[source].append(target)

        return graph

    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        """现在你总共有 numCourses 门课需要选，记为 0 到 numCourses - 1。
        给你一个数组 prerequisites
        其中 prerequisites[i] = [ai, bi] ，表示在选修课程 ai 前 必须 先选修 bi 。

        例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示：[0,1] 。
        返回你为了学完所有课程所安排的学习顺序。
        可能会有多个正确的顺序，你只要返回 任意一种 就可以了。如果不可能完成所有课程，返回 一个空数组 。

        输入：numCourses = 2, prerequisites = [[1,0]]
        输出：[0,1]

        输入：numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
        输出：[0,2,1,3]

        输入：numCourses = 1, prerequisites = []
        输出：[0]
        """
        # 拓扑排序
        # 后序遍历，反转就是拓扑排序顺序！！
        graph = self.build_graph(numCourses, prerequisites)
        for i in range(numCourses):
            self.traverse(graph, i)
        if self.has_circle:
            return []

        return self.postorder[::-1]

    def bfsFindOrder(
        self, numCourses: int, prerequisites: list[list[int]]
    ) -> list[int]:
        """拓扑排序的层序遍历版本

        每个节点维护入度和出度，每次访问入度为 0 的节点加入队列，
        当访问某个节点时，将该节点的邻节点的入度都减一
        """
        # 记录每个节点的入度
        indegree = [0] * numCourses

        # 如果有环，则入度不会减为 0，不会加入队列中，最后通过检查数量一致判断是否有环
        for pre in prerequisites:
            to = pre[0]
            indegree[to] += 1

        q = []
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        graph = self.build_graph(numCourses, prerequisites)

        res = []
        while q:
            i = q.pop()
            res.append(i)

            for to in graph[i]:
                indegree[to] -= 1
                if indegree[to] == 0:
                    q.append(to)

        if len(res) != numCourses:
            return []
        return res

    def isBipartite(self, graph: list[list[int]]) -> bool:
        """785. 判断二分图
        存在一个 无向图 ，图中有 n 个节点。
        给你一个二维数组 graph ，其中 graph[u] 是一个节点数组，由节点 u 的邻接节点组成。
        形式上，对于 graph[u] 中的每个 v ，都存在一条位于节点 u 和节点 v 之间的无向边。

        二分图 定义：如果能将一个图的节点集合分割成两个独立的子集 A 和 B ，
        并使图中的每一条边的两个节点一个来自 A 集合，
        一个来自 B 集合，就将这个图称为 二分图 。

        如果图是二分图，返回 true ；否则，返回 false 。
        """
        # 连接的两个节点属于不同集合，且一个节点只属于一个结合
        # 遍历
        # 1. 如果节点没有颜色，对节点进行染色，标记为不同颜色
        # 2. 遍历节点的边，如果边上两节点属性不一致则为 False
        # 3. 无向边，[u]->v, [v]->u 都存在

        visited = {}
        colors = [0] * len(graph)  # 0, 1
        self.is_bipartite = True

        def traverse(graph, i):
            if not self.is_bipartite:
                return

            if i in visited:
                return
            visited[i] = True

            for neighbor in graph[i]:
                if neighbor not in visited:
                    colors[neighbor] = 1 - colors[i]
                    traverse(graph, neighbor)
                else:
                    if colors[neighbor] == colors[i]:
                        self.is_bipartite = False
                        return

        for i in range(len(graph)):
            traverse(graph, i)

        return self.is_bipartite

    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        """886. 可能的二分法
        给定一组 n 人（编号为 1, 2, ..., n）， 我们想把每个人分进任意大小的两组。每个人都可能不喜欢其他人，那么他们不应该属于同一组。

        给定整数 n 和数组 dislikes ，其中 dislikes[i] = [ai, bi] ，
        表示不允许将编号为 ai 和  bi的人归入同一组。当可以用这种方法将所有人分进两组时，返回 true；否则返回 false。

        输入：n = 4, dislikes = [[1,2],[1,3],[2,4]]
        输出：true

        输入：n = 3, dislikes = [[1,2],[1,3],[2,3]]
        输出：false

        输入：n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
        输出：false
        """
        # 对记录进行染色
        # 本次使用 BFS 层序遍历，dislike 表示一条边，两侧节点不能同一个颜色
        colors = [0] * (n + 1)  # 0,1

        graph = self.build_bi_graph(n + 1, dislikes)

        q = []
        for i, neighbors in enumerate(graph):
            if not neighbors:
                continue

            q.append(i)

        visited = {}
        while q:
            i = q.pop()
            if i in visited:
                continue
            visited[i] = True

            for neighbor in graph[i]:
                if neighbor not in visited:
                    colors[neighbor] = 1 - colors[i]
                    q.append(neighbor)
                else:
                    if colors[i] == colors[neighbor]:
                        return False
        return True
    
    def build_bi_graph(self, num: int, edges: list[list[int]]):
        """建立双向邻接表"""
        graph = [[] for i in range(num)]
        for target, source in edges:
            graph[source].append(target)
            graph[target].append(source)

        return graph


if __name__ == "__main__":
    assert Solution().canFinish(numCourses=2, prerequisites=[[1, 0]])
    assert not Solution().canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]])

    assert Solution().findOrder(numCourses=2, prerequisites=[[1, 0]]) == [0, 1]
    assert Solution().findOrder(
        numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]
    ) == [0, 2, 1, 3]
    assert Solution().findOrder(numCourses=1, prerequisites=[]) == [0]

    assert Solution().bfsFindOrder(numCourses=2, prerequisites=[[1, 0]]) == [0, 1]
    assert Solution().bfsFindOrder(
        numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]
    ) == [0, 2, 1, 3]
    assert Solution().bfsFindOrder(numCourses=1, prerequisites=[]) == [0]

    assert not Solution().isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]])
    assert Solution().isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]])

    assert Solution().possibleBipartition(n=4, dislikes=[[1, 2], [1, 3], [2, 4]])
    assert not Solution().possibleBipartition(n=3, dislikes=[[1, 2], [1, 3], [2, 3]])
    assert not Solution().possibleBipartition(
        n=5, dislikes=[[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
    )

    print("OK")
