# 图算法

## 1. 图表示

图是点和边组成的数据结构，使用下面两种形式存储：邻接表和邻接矩阵

### 邻接表
- n个节点，维护一个长度为n的列表
- 每个元素也是列表，存储跟该节点相连的其他节点编号或索引

```py
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
        visited = {}  # 避免重复访问
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
```

### 邻接矩阵

- `n*n` 的二维数组，当 `arr[i][j]` 对应的元素值非0，则表示 i 和 j 存在一条边

```py
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
```

## 2. 环检测

对于有向图的场景，出现环路表示不可用，需要检查出环

### 选修课

背景：你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
- 在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，
- 其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 

解法：
1. 遍历所有路径，如果同一个路径上节点访问多次，则认为有环

```py
class Solution:
    def __init__(self):
        self.has_circle = False
        self.on_path = {}
        self.visited = {}
        self.postorder = []

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # 环检测
        # 遍历图的所有路径，分别检查每个路径是否有环
        graph = [[] for i in range(numCourses)]
        for target, source in prerequisites:
            graph[source].append(target)

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
```

## 3. 拓扑排序

有向图，要求某些节点的访问需要先访问前驱节点，返回拓扑排序的节点顺序

### 课程拓扑排序

题目：现在你总共有 numCourses 门课需要选，记为 0 到 numCourses - 1。
- 给你一个数组 prerequisites，其中 prerequisites[i] = [ai, bi] ，表示在选修课程 ai 前 必须 先选修 bi 。
- 返回你为了学完所有课程所安排的学习顺序。


方案1：递归遍历
1. 对图进行访问，并记录后序遍历的序列；
2. 返回后序遍历的逆序作为结果；

```py
class Solution:
    def __init__(self):
        self.has_circle = False
        self.on_path = {}
        self.visited = {}
        self.postorder = []

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

    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # 拓扑排序
        # 后序遍历，反转就是拓扑排序顺序！！
        graph = [[] for i in range(numCourses)]
        for target, source in prerequisites:
            graph[source].append(target)
        for i in range(numCourses):
            self.traverse(graph, i)
        if self.has_circle:
            return []

        return self.postorder[::-1]
```


方案2：层序遍历

思想：先访问无前驱节点的节点
1. 每个节点维护该节点的入度，即前驱节点数量
- 每次访问入度为 0 的节点加入队列
2. 当访问某个节点时，将该节点的邻节点的入度都减一
- 如果邻节点的入度为0，则加入队列中
3. 如果遍历后节点数跟实际不一致，则表示有环路，否则返回结果
- 如果有环，则入度不会减为 0，不会加入队列中

```py
class Solution:
    def bfsFindOrder(
        self, numCourses: int, prerequisites: list[list[int]]
    ) -> list[int]:
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
```

## 4. 二分集

二分集：图中的节点可以明确分为两个集合，同集合节点不想交，不同集合的节点允许相交

### 判断二分图（785）

```py
class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
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
```

## 5. 并查集 UnionFind

并查集，高效解决**无向图**的连通性问题
- 节点间是否连通
    - 自反性：p和q自身也是连通的
    - 对称性：p和q连通，则q和p也连通
    - 传递性：p和q连通，q和r连通，则p和r也连通
- 连通分量（图有多少个树）

数据结构：森林结构，维护多个多叉树
1. 连接节点只需要将两个多叉树根节点相连，将其中一个根节点接到另一个根节点下面
2. 多叉树的数量，等于连通分量的数量

树的高度决定了操作的时间复杂度，需要保证树高度是常量
1. 使用 parent 索引找到根节点
2. 路径压缩：将节点的 parent 节点直接连接到根节点

特别注意：
1. 有时候，节点编码需要额外通过映射关系到 n 的空间内，一维数组空间

```py
class UF:
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
```

### 省份数量（547）

```py
class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        """省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。

        其中 isConnected[i][j] = 1
        表示第 i 个城市和第 j 个城市直接相连

        返回矩阵中 省份 的数量。
        """
        uf = UF(len(isConnected))
        for i, row in enumerate(isConnected):
            for j, connected in enumerate(row):
                if connected:
                    uf.union(i, j)

        return uf.count()
```

### 验证二叉树（1361）

1. 确认所有节点都在同一个连通分量里面
2. 不存在环

```py
class Solution:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: list[int], rightChild: list[int]
    ) -> bool:
        uf = UF(n)
        is_children = {}  # 记录节点是否已经是子节点

        for i in range(n):
            if leftChild[i] != -1:
                # 已经是子节点，返回 False
                if leftChild[i] in is_children:
                    return False

                # 已经连接过，存在环，返回 False
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
```

### 移除最多的同行或同列的石头

- 需要将石头所在行列转换成一维数组的位置

```py
class Solution:
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
```

## 6. Kruskal 最小生成树算法

通过有环（无环）加权连通图，找到最小的无环加权树
- 连通所有节点
- 没有环
- 累加权重最小

基于并查集 UnionFind 判断连通分量
1. 将边按照权重从小到大排序
2. 每次将较小的边加入到树中，如果已经连通则跳过
3. 直到树的连通分量为1，即所有节点都连通完成

### 以图判树（261）

判断图是否是一棵树：连通分量的数量为1，且无环

```py
class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        uf = UF(n)
        for edge in edges:
            p, q = edge
            if uf.connected(p, q):
                return False
            uf.union(p, q)

        return uf.count() == 1
```

### 最低成本联通所有城市（1135）

```py
class Solution:
    def minimumCost(self, n: int, connections: list[list[int]]) -> int:
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
```

### 连接所有点的最小费用（1584）

- 点的编码映射到一维数组空间
- 边的建立，任意两个点都可能生成边
```py
def minCostConnectPoints(self, points: list[list[int]]) -> int:
        """
        连接点 [xi, yi] 和点 [xj, yj] 的费用为它们之间的
        曼哈顿距离 ：|xi - xj| + |yi - yj| ，其中 |val| 表示 val 的绝对值。

        请你返回将所有点连接的最小总费用。
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
```

## 7. Dijkstra 单源最短路径算法

计算从某个点开始，到其他每个点的最短路径
- 使用二叉堆的优先级队列
- 贪心算法

BFS 层序遍历方式
1. 初始化长度为 n 的结果最短路径数组（n是节点数量）
2. 从start点出发
- 当访问节点，在当前路径的最短路径，比结果数组上记录最短路径的小，则进行下一层遍历
3. 判断该节点各邻节点的最短路径大小
- 取到邻节点的权重和当前路径的权重累加，跟结果数组上的邻节点位置路径对比
- 如果小于结果数值上的值，则将邻节点结果数值更新，并加入到队列中

```py
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

def dijkstra(start: int, graph: list[list[int]]) -> list[int]:
    # 结果数组，记录到其他各个节点的最短距离
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
```

### 网络延迟时间（743）

- 计算 k 到其他点的最短路径
- 取最短路径最大值

```py
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        """7
        给你一个列表 times，表示信号经过 有向 边的传递时间。
        times[i] = (ui, vi, wi)，其中 ui 是源节点，vi 是目标节点， wi 是一个信号从源节点传递到目标节点的时间。

        现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1 
        """
        graph = build_graph(n + 1, times)
        res = dijkstra(k, graph)
        max_time = 0
        for t in res[1:]:
            if t == float("inf"):
                return -1
            max_time = max(t, max_time)
        return max_time
```

### 最小体力消耗路径（1631）

```py
class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        """1631. 最小体力消耗路径
        你准备参加一场远足活动。给你一个二维 rows x columns 的地图 heights ，
        其中 heights[row][col] 表示格子 (row, col) 的高度。一开始你在最左上角的格子 (0, 0) ，
        且你希望去最右下角的格子 (rows-1, columns-1) （注意下标从 0 开始编号）。

        你每次可以往 上，下，左，右 四个方向之一移动，你想要找到耗费 体力 最小的一条路径。

        一条路径耗费的 体力值 是路径上相邻格子之间 高度差绝对值 的 最大值 决定的。请你返回从左上角走到右下角的最小 体力消耗值 。
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
```