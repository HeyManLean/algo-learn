# -*- coding: utf-8 -*-

"""
Dijkstra 算法

计算单源最短路径算法

计算从某个点起，到其他每个点的最小路径，返回数组

"""
import heapq


def build_graph(n: int, weights: list[list[int]]):
    """
    weights 三元组，(i, j, weight)
    """
    graph = [[] for _ in range(n)]
    for weight in weights:
        i, j, w = weight
        graph[i].append((j, w))
    return graph


def dijkstra(start: int, graph: list[list[tuple]]) -> list[int]:
    """

    graph 使用带权重的邻接表
    0: [(1,10), (3, 20)]

    从 start 开始，进行 BFS 遍历
    1. 维护数组，表示 start 从某个点目前的最小距离
    2. 遍历，如果当前距离小于最小距离，则交换，否则不需要加入遍历队列中
    - 优先遍历最小权重的边
    """
    dist_to = [float('inf')] * len(graph)
    dist_to[start] = 0  # 到自身距离为 0

    pq = [(0, start)]  # 将自己加到队列中，开始层序遍历

    while pq:
        cur_dist, cur = heapq.heappop(pq)
        # 如果已经有过其他路径比当前路径小，则跳过
        if dist_to[cur] < cur_dist:
            continue

        # 对该节点的其他邻节点进行判断
        for nxt, dist in graph[cur]:
            # 邻节点的最新距离为当前节点距离+到邻节点的距离
            nxt_dist = cur_dist + dist
            if dist_to[nxt] < nxt_dist:
                continue

            dist_to[nxt] = nxt_dist
            heapq.heappush(pq, (nxt_dist, nxt))

    return dist_to


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        """743. 网络延迟时间
        有 n 个网络节点，标记为 1 到 n。

        给你一个列表 times，表示信号经过 有向 边的传递时间。
        times[i] = (ui, vi, wi)，其中 ui 是源节点，vi 是目标节点， wi 是一个信号从源节点传递到目标节点的时间。

        现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1 。
        https://assets.leetcode.com/uploads/2019/05/23/931_example_1.png
        """
        graph = build_graph(n + 1, times)
        res = dijkstra(k, graph)
        max_time = 0
        for t in res[1:]:
            if t == float("inf"):
                return -1
            max_time = max(t, max_time)
        return max_time

    def maxProbability(
        self,
        n: int,
        edges: list[list[int]],
        succProb: list[float],
        start_node: int,
        end_node: int,
    ) -> float:
        """1514. 概率最大的路径
        给你一个由 n 个节点（下标从 0 开始）组成的无向加权图，
        该图由一个描述边的列表组成，其中 edges[i] = [a, b] 表示连接节点 a 和 b 的一条无向边，
        且该边遍历成功的概率为 succProb[i]

        指定两个节点分别作为起点 start 和终点 end ，请你找出从起点到终点成功概率最大的路径，并返回其成功概率。

        如果不存在从 start 到 end 的路径，请 返回 0 。只要答案与标准答案的误差不超过 1e-5 ，就会被视作正确答案。

        输入：n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
        输出：0.25000

        输入：n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
        输出：0.30000

        输入：n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
        输出：0.00000
        """
        # 路径的成功率等于每个边的概率相乘
        graph = [[] for _ in range(n)]
        for i, edge in enumerate(edges):
            graph[edge[0]].append((edge[1], succProb[i]))
            graph[edge[1]].append((edge[0], succProb[i]))

        prob_to = [0] * n
        prob_to[start_node] = 1

        pq = [(1, start_node)]
        while pq:
            cur_prob, cur_node = heapq.heappop(pq)

            # 保留概率更大的记录
            if cur_prob < prob_to[cur_node]:
                continue

            for nxt, prob in graph[cur_node]:
                nxt_prob = prob_to[cur_node] * prob
                if nxt_prob > prob_to[nxt]:
                    prob_to[nxt] = nxt_prob
                    heapq.heappush(pq, (nxt_prob, nxt))

        return prob_to[end_node]

    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        """1631. 最小体力消耗路径
        你准备参加一场远足活动。给你一个二维 rows x columns 的地图 heights ，
        其中 heights[row][col] 表示格子 (row, col) 的高度。一开始你在最左上角的格子 (0, 0) ，
        且你希望去最右下角的格子 (rows-1, columns-1) （注意下标从 0 开始编号）。

        你每次可以往 上，下，左，右 四个方向之一移动，你想要找到耗费 体力 最小的一条路径。

        一条路径耗费的 体力值 是路径上相邻格子之间 高度差绝对值 的 最大值 决定的。

        请你返回从左上角走到右下角的最小 体力消耗值 。

        输入：heights = [[1,2,2],[3,8,2],[5,3,5]]
        输出：2

        输入：heights = [[1,2,3],[3,8,4],[5,3,5]]
        输出：1

        输入：heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
        输出：0
        """
        rows = len(heights)
        cols = len(heights[0])

        def get_neighbors(x: int, y: int) -> tuple[int, int]:
            neighbors = []
            if x - 1 >= 0:
                neighbors.append((x - 1, y))
            if y - 1 >= 0:
                neighbors.append((x, y - 1))
            if x + 1 < rows:
                neighbors.append((x + 1, y))
            if y + 1 < cols:
                neighbors.append((x, y + 1))
            return neighbors

        height_to = [float("inf") for _ in range(rows * cols)]
        pq = [(0, 0, 0)]  # 高度差，行，列
        while pq:
            h, x, y = heapq.heappop(pq)
            if h > height_to[x * cols + y]:
                continue

            for nxt_x, nxt_y in get_neighbors(x, y):
                # 路径上的最大高度差
                nxt_h = max(abs(heights[nxt_x][nxt_y] - heights[x][y]), h)
                if nxt_h < height_to[nxt_x * cols + nxt_y]:
                    height_to[nxt_x * cols + nxt_y] = nxt_h
                    heapq.heappush(pq, (nxt_h, nxt_x, nxt_y))

        return height_to[-1] if height_to[-1] != float("inf") else 0


if __name__ == "__main__":
    assert Solution().networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2
    assert Solution().networkDelayTime(times=[[1, 2, 1]], n=2, k=1) == 1
    assert Solution().networkDelayTime(times=[[1, 2, 1]], n=2, k=2) == -1
    assert Solution().networkDelayTime([[1, 2, 1], [2, 3, 2], [1, 3, 1]], 3, 2) == -1
    assert (
        Solution().maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2)
        == 0.25
    )
    assert (
        Solution().maxProbability(3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2)
        == 0.3
    )
    assert Solution().maxProbability(3, [[0, 1]], [0.5], 0, 2) == 0

    assert Solution().minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]) == 2
    assert Solution().minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]) == 1
    assert (
        Solution().minimumEffortPath(
            [
                [1, 2, 1, 1, 1],
                [1, 2, 1, 2, 1],
                [1, 2, 1, 2, 1],
                [1, 2, 1, 2, 1],
                [1, 1, 1, 2, 1],
            ]
        )
        == 0
    )
    assert Solution().minimumEffortPath([[3]]) == 0
    assert Solution().minimumEffortPath([[1, 10, 6, 7, 9, 10, 4, 9]]) == 9
    print("OK")
