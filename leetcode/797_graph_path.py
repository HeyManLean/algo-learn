# -*- coding: utf-8 -*-
"""给你一个有 n 个节点的 有向无环图（DAG），请你找出所有从节点 0 到节点 n-1 的路径并输出（不要求按特定顺序）"""

class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        res = []
        path = []
        n = len(graph)
        visited = {}

        def traverse(v):
            path.append(v)

            if v == n - 1:  # 全路径
                res.append(list(path))
                path.pop()
                return

            # # 避免环
            # if visited.get(v):
            #     return
            # visited[v] = True

            for i in graph[v]:
                traverse(i)

            path.pop()

        traverse(0)

        print(res)

        return res


if __name__ == '__main__':
    assert Solution().allPathsSourceTarget([[1,2],[3],[3],[]]) == [[0,1,3],[0,2,3]]
    assert Solution().allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]) == [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]