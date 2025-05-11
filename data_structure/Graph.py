# coding=utf-8

from enum import Enum

from Vector import Vector
from List import List
from Stack import Stack
from Queue import Queue


class VStatus(Enum):
    UNDISCOVERED = 0
    DISCOVERED = 1
    VISITED = 2


class EType(Enum):
    UNDETERMINED = 0
    TREE = 1
    CROSS = 2
    FORWARD = 3
    BACKWARD = 4


class Vertex:
    def __init__(self, d=0):
        self.data = d
        self.inDegree = 0
        self.outDegree = 0
        self.status = VStatus.UNDISCOVERED.value
        self.dTime = -1
        self.fTime = -1
        self.parent = -1
        self.priority = 1000000


class Edge:
    def __init__(self, j, d=0, w=0):
        self.jVertex = j  # 终点顶点
        self.data = d
        self.weight = w
        self.type = EType.UNDETERMINED.value


class Graph:
    """使用邻接列表实现"""

    def __init__(self):
        self.n = 0  # 顶点数
        self.e = 0  # 边数

        self.V = Vector()  # 顶点集
        self.E = Vector()  # 边集（邻接表）

    def __del__(self):
        del self.V
        del self.E

    def insertV(self, d):
        """
            d: 顶点数据
        """
        vertex = Vertex(d)
        self.V.insert(self.V.size(), vertex)
        self.E.insert(self.E.size(), List())  # 第i个列表对应第i个顶点， 里面存放Edge对象.
        self.n += 1
        return self.n - 1

    def removeV(self, i):
        self.E.remove(i)
        self.n -= 1
        return self.V.remove(i)

    def getVertex(self, i):
        """获取顶点的数据"""
        return self.V[i].data

    def setVertex(self, i, value):
        self.V[i].data = value

    def getInDegree(self, i):
        return self.V[i].inDegree

    def setInDegree(self, i, value):
        self.V[i].inDegree = value

    def getOutDegree(self, i):
        return self.V[i].outDegree

    def setOutDegree(self, i, value):
        self.V[i].outDegree = value

    def getFirstNbr(self, i):
        """首个邻接顶点"""
        if self.E[i].size() > 0:
            return self.E[i][0].jVertex
        return -1

    def setFirstNbr(self, i, j):
        if self.E[i].size() > 0:
            self.E[i][0].jVertex = j
        else:
            self.insertE(i, j)

    def getNextNbr(self, i, j):
        """获取顶点i边中j的下一个邻接顶点"""
        jEdge = self.findE(i, j)
        if jEdge is not None:
            if self.E[i].valid(jEdge.succ):
                return jEdge.succ.data.jVertex
        return -1

    def getStatus(self, i):
        return self.V[i].status

    def setStatus(self, i, value):
        self.V[i].status = value

    def getDTime(self, i):
        return self.V[i].dTime

    def setDTime(self, i, value):
        self.V[i].dTime = value

    def getFTime(self, i):
        return self.V[i].fTime

    def setFTime(self, i, value):
        self.V[i].fTime = value

    def getParent(self, i):
        return self.V[i].parent

    def setParent(self, i, j):
        self.V[i].parent = j

    def getPriority(self, i):
        return self.V[i].priority

    def setPriority(self, i, value):
        self.V[i].priority = value

    def existE(self, i, j):
        """是否存在顶点i和顶点j的边(i, j)"""
        if not (0 <= i and i < self.n and 0 <= j and j < self.n):
            return False
        for edge in self.E[i]:
            if edge.data.jVertex == j:
                return True
        return False

    def findE(self, i, j):
        """查找边对象"""
        if not (0 <= i and i < self.n and 0 <= j and j < self.n):
            return
        for edge in self.E[i]:
            if edge.data.jVertex == j:
                return edge

    def getEIndex(self, i, j):
        """查找边所在列表索引"""
        if not (0 <= i and i < self.n and 0 <= j and j < self.n):
            return
        for eIndex, edge in enumerate(self.E[i]):
            if edge.jVertex == j:
                return eIndex

    def insertE(self, i, j, d=0, w=0, double=False):
        """
        d: 数据
        i: 第i顶点
        j: 第j顶点
        w: 权重
        """
        edge = Edge(j, d, w)
        self.E[i].insertAsLast(edge)
        self.V[i].outDegree += 1
        self.V[i].inDegree += 1
        self.e += 1
        if double:
            edge1 = Edge(i, d, w)
            self.E[j].insertAsLast(edge1)
            self.V[j].outDegree += 1
            self.V[j].inDegree += 1
            self.e += 1
        return edge

    def removeE(self, i, j):
        edge = self.findE(i, j)
        if edge is not None:
            self.V[i].outDegree -= 1
            self.V[i].inDegree -= 1
            self.e -= 1
            return self.E[i].remove(edge)

    def getEType(self, i, j):
        return self.findE(i, j).data.type

    def setEType(self, i, j, value):
        self.findE(i, j).data.type = value

    def getEdge(self, i, j):
        """获取边的数据"""
        return self.findE(i, j).data.data

    def setEdge(self, i, j, value):
        self.findE(i, j).data.data = value

    def getWeight(self, i, j):
        return self.findE(i, j).data.weight

    def setWeight(self, i, j, w):
        self.findE(i, j).data.weight = w

    # 算法=================================================

    def reset(self):
        """重置状态"""
        for i in range(self.n):
            self.setStatus(i, VStatus.UNDISCOVERED.value)
            self.setDTime(i, -1)
            self.setFTime(i, -1)
            for j in range(self.n):
                if self.existE(i, j):
                    self.setEType(i, j, EType.UNDETERMINED.value)

    def bfs(self, s: int):
        """广度优先搜索算法, 对于不连通的图
            g = Graph()
            A = g.insertV('A')
            B = g.insertV('B')
            C = g.insertV('C')
            D = g.insertV('D')
            E = g.insertV('E')
            F = g.insertV('F')
            G = g.insertV('G')
            S = g.insertV('S')

            g.insertE(A, E)
            g.insertE(A, C)
            g.insertE(S, A)
            g.insertE(S, D)
            g.insertE(S, C)
            g.insertE(E, F)
            g.insertE(E, G)
            g.insertE(D, B)
            g.insertE(C, B)
            g.insertE(F, G)
            g.insertE(G, B)

            g.bfs(S)
            =====================
            S
            A
            D
            C
            E
            B
            F
            G
        """
        self.reset()
        clock = 0
        v = s
        self.BFS(v, clock)
        v = (v + 1) % self.n
        while s != v:
            if self.getStatus(v) == VStatus.UNDISCOVERED.value:  # 直到所有顶点都被发现
                self.BFS(v, clock)
            v = (v + 1) % self.n  # 循环顶点（直至再次碰到s)

    def BFS(self, v, clock):
        """（连通域）广度优先搜索算法"""
        Q = Queue()
        Q.enqueue(v)
        self.setStatus(v, VStatus.DISCOVERED.value)
        while not Q.empty():
            v = Q.dequeue()
            clock += 1
            self.setDTime(v, clock)
            u = self.getFirstNbr(v)
            while u != -1:
                if self.getStatus(u) == VStatus.UNDISCOVERED.value:
                    self.setStatus(u, VStatus.DISCOVERED.value)
                    Q.enqueue(u)
                    self.setEType(v, u, EType.TREE.value)
                    self.setParent(u, v)
                else:
                    self.setEType(v, u, EType.CROSS.value)
                u = self.getNextNbr(v, u)
            print(self.V[v].data)
            self.setStatus(v, VStatus.VISITED.value)

    def dfs(self, s: int):
        """深度优先搜索算法
            g = Graph()
            A = g.insertV('A')
            B = g.insertV('B')
            C = g.insertV('C')
            D = g.insertV('D')
            E = g.insertV('E')
            F = g.insertV('F')
            G = g.insertV('G')

            g.insertE(A, B)
            g.insertE(A, C)
            g.insertE(A, F)
            g.insertE(B, C)
            g.insertE(D, A)
            g.insertE(D, F)
            g.insertE(E, F)
            g.insertE(F, G)
            g.insertE(G, A)
            g.insertE(G, C)

            g.dfs(A)
            ================================
            A
            B
            C
            F
            G
            D
            E
        """
        self.reset()
        clock = 0
        v = s
        self.BFS(v, clock)
        v = (v + 1) % self.n
        while s != v:
            if self.getStatus(v) == VStatus.UNDISCOVERED.value:  # 直到所有顶点都被发现
                self.DFS(v, clock)
            v = (v + 1) % self.n  # 循环顶点（直至再次碰到s)

    def DFS(self, v, clock):
        """（连通域）深度优先搜索算法"""
        clock += 1
        self.setDTime(v, clock)
        self.setStatus(v, VStatus.DISCOVERED.value)
        print(self.V[v].data)

        u = self.getFirstNbr(v)
        while u != -1:
            uStatus = self.getStatus(u)
            if uStatus == VStatus.UNDISCOVERED.value:
                self.setEType(v, u, EType.TREE.value)
                self.setParent(u, v)
                self.DFS(u, clock)
            elif uStatus == VStatus.DISCOVERED.value:
                self.setEType(v, u, EType.BACKWARD.value)
            else:
                self.setEType(v, u, EType.FORWARD.value if self.getDTime(
                    v) < self.getDTime(u) else EType.CROSS.value)
            u = self.getNextNbr(v, u)
        self.setStatus(v, VStatus.VISITED.value)
        clock += 1
        self.setFTime(v, clock)

    def TSort(self, v, clock, S: Stack):
        """（连通域）基于DFS的拓扑排序算法"""
        clock += 1
        self.setDTime(v, clock)
        self.setStatus(v, VStatus.DISCOVERED.value)
        u = self.getFirstNbr(v)
        while u != -1:
            uStatus = self.getStatus(u)
            if uStatus == VStatus.UNDISCOVERED.value:
                if not self.TSort(u, clock, S):
                    return False
            elif uStatus == VStatus.DISCOVERED.value:
                self.setEType(v, u, EType.BACKWARD.value)
                return False
            else:
                self.setEType(v, u, EType.FORWARD.value if self.getDTime(
                    v) < self.getDTime(u) else EType.CROSS.value)
            u = self.getNextNbr(v, u)
        self.setStatus(v, VStatus.VISITED.value)
        S.push(v)
        return True

    def tSort(self, s):
        """基于DFS的拓扑排序算法"""
        self.reset()
        clock = 0
        S = Stack()  # 记录顶点（不像遍历，只记录有效的顶点)
        v = s
        if not self.TSort(v, clock, S):
            print('Not DAG!')
            while not S.empty():
                print(S.pop())
        v = (v + 1) % self.n
        while s != v:
            # 直到所有顶点都被发现, 发现了的顶点应该存在栈中(递归中)
            if self.getStatus(v) == VStatus.UNDISCOVERED.value:
                if not self.TSort(v, clock, S):
                    print('Not DAG!')
                    while not S.empty():
                        print(S.pop())
                    break
            v = (v + 1) % self.n
        while not S.empty():
            print(S.pop())

    def PFS(self, v, prioUpdater):
        """（连通域）优先级搜索框架"""
        self.setPriority(v, 0)
        self.setStatus(v, VStatus.VISITED.value)
        self.setParent(v, -1)
        while True:
            print(self.V[v].data)
            u = self.getFirstNbr(v)
            while u != -1:
                prioUpdater(v, u)
                u = self.getNextNbr(v, u)
            shortest = 100000000  # 优先级数值越高， 优先级越低
            for i in range(self.n):  # 遍历所有顶点， 取优先级最高的有效顶点
                if self.getStatus(i) == VStatus.UNDISCOVERED.value:
                    iPriority = self.getPriority(i)
                    if shortest > iPriority:
                        shortest = iPriority
                        v = i
            if self.getStatus(v) == VStatus.VISITED.value:  # 这里代表所有顶点已加入
                break
            self.setStatus(v, VStatus.VISITED.value)
            self.setEType(self.getParent(v), v, EType.TREE.value)

    def pfs(self, s, prioUpdater):
        """优先级搜索框架"""
        self.reset()
        v = s
        self.PFS(v, prioUpdater)
        v = (v + 1) % self.n
        while s != v:
            if self.getStatus(v) == VStatus.UNDISCOVERED.value:
                self.PFS(v, prioUpdater)
            v = (v + 1) % self.n

    def prim(self, v, u):
        """基于优先级搜索框架的prim算法， 找出最小支撑树。
        找出已搜索顶点和未搜索顶点之间所有边中的最小边。
        1. 找出当前顶点的所有邻接顶点， 更新这些邻接顶点的优先级和父节点（用于辨别是那两个点连接成的边；有可能之前也更新过；数值为邻接边权重）。顶点默认优先级数值无限大.
        2. 遍历所有的顶点，找出还没发现的优先级数值最低的.
        3. 将最低的顶点作为当前顶点，并添加为已搜索。
        =====================================
        g = Graph()
        A = g.insertV('A')
        B = g.insertV('B')
        C = g.insertV('C')
        D = g.insertV('D')
        E = g.insertV('E')
        F = g.insertV('F')
        G = g.insertV('G')
        H = g.insertV('H')

        g.insertE(A, B, w=4, double=True)
        g.insertE(A, D, w=6, double=True)
        g.insertE(A, G, w=7, double=True)
        g.insertE(B, C, w=12, double=True)
        g.insertE(C, D, w=9, double=True)
        g.insertE(C, E, w=1, double=True)
        g.insertE(C, F, w=2, double=True)
        g.insertE(C, H, w=10, double=True)
        g.insertE(D, E, w=13, double=True)
        g.insertE(D, G, w=2, double=True)
        g.insertE(E, F, w=5, double=True)
        g.insertE(E, G, w=11, double=True)
        g.insertE(E, H, w=8, double=True)
        g.insertE(F, H, w=7, double=True)
        g.insertE(G, H, w=14, double=True)

        g.pfs(A, g.prim)
        ==========================
        A
        B
        D
        G
        C
        E
        F
        H
        """
        if self.getStatus(u) == VStatus.UNDISCOVERED.value:
            eWeight = self.getWeight(v, u)
            if self.getPriority(u) > eWeight:
                self.setPriority(u, eWeight)
                self.setParent(u, v)

    def dijkstra(self, v, u):
        """基于优先级框架的dijkstra算法，求其他顶点与顶点s（指定顶点）各自对应的的最短路径
        - 找出与当前顶点邻接的顶点， 更新其优先级和父节点
        - 优先级数值为邻接边的权值加上当前顶点的优先级， 因为是假设通过这邻接边， 以及当前顶点的（与顶点s的）最短路径， 邻接顶点连接到顶点s所经过的边总的权值
        - 第一次已经得出与顶点s邻接的顶点的权值
        ===================================
        g = Graph()
        A = g.insertV('A')
        B = g.insertV('B')
        C = g.insertV('C')
        D = g.insertV('D')
        E = g.insertV('E')
        F = g.insertV('F')
        G = g.insertV('G')
        H = g.insertV('H')

        g.insertE(A, B, w=4, double=True)
        g.insertE(A, D, w=6, double=True)
        g.insertE(A, G, w=7, double=True)
        g.insertE(B, C, w=12, double=True)
        g.insertE(C, D, w=9, double=True)
        g.insertE(C, E, w=1, double=True)
        g.insertE(C, F, w=2, double=True)
        g.insertE(C, H, w=10, double=True)
        g.insertE(D, E, w=13, double=True)
        g.insertE(D, G, w=2, double=True)
        g.insertE(E, F, w=5, double=True)
        g.insertE(E, G, w=11, double=True)
        g.insertE(E, H, w=8, double=True)
        g.insertE(F, H, w=7, double=True)
        g.insertE(G, H, w=14, double=True)

        g.pfs(A, g.dijkstra)
        for v in g.V:
            u = v
            path = str(v.data)
            while u.parent != -1:
                path += str(g.V[u.parent].data)
                u = g.V[u.parent]
            print(v.data, ':', v.priority, ':', '->'.join(path[::-1]))
        ===========================================
        A
        B
        D
        G
        C
        E
        F
        H
        A : 0 : A
        B : 4 : A->B
        C : 15 : A->D->C
        D : 6 : A->D
        E : 16 : A->D->C->E
        F : 17 : A->D->C->F
        G : 7 : A->G
        H : 21 : A->G->H
        """
        if self.getStatus(u) == VStatus.UNDISCOVERED.value:
            uPriority = self.getPriority(v) + self.getWeight(v, u)
            if self.getPriority(u) > uPriority:
                self.setPriority(u, uPriority)
                self.setParent(u, v)
