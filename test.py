# -*- coding: utf-8 -*-

import heapq

# @lc code=start
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        heap = [1]
        q = [1]
        visited = {}

        while len(heap) < n and q:
            v = q[0]
            for i in [2, 3, 5]:
                if visited.get(v * i):
                    continue

                visited[v*i] = True
                q.append(v * i)
                heapq.heappush(heap, v*i)

            q = q[1:]

        print(heap)

        for i in range(n - 1):
            heapq.heappop(heap)

        return heapq.heappop(heap)
    

print(Solution().nthUglyNumber(10))