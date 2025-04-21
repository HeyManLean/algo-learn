# -*- coding: utf-8 -*-


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        """200. 岛屿数量
        给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

        岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
        """
        m = len(grid)
        n = len(grid[0])

        WATER = '0'
        LAND = '1'

        # dfs，识别一个岛屿，计数后，将其连通的所有单元格都变成水
        def dfs(grid, row, col):
            # 叶子节点
            if row < 0 or row >= m or col < 0 or col >= n:
                return

            # 限制条件
            if grid[row][col] == WATER:
                return

            # 做出选择
            grid[row][col] = WATER

            dfs(grid, row - 1, col)
            dfs(grid, row + 1, col)
            dfs(grid, row, col - 1)
            dfs(grid, row, col + 1)

        island_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == LAND:
                    island_count += 1
                    dfs(grid, i, j)

        return island_count
        

    def closedIsland(self, grid: list[list[int]]) -> int:
        """1254. 统计封闭岛屿的数目
        二维矩阵 grid 由 0 （土地）和 1 （水）组成。
        岛是由最大的4个方向连通的 0 组成的群，
        封闭岛是一个 完全 由1包围（左、上、右、下）的岛。

        请返回 封闭岛屿 的数目。

        https://assets.leetcode.com/uploads/2019/10/31/sample_3_1610.png
        输入：grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
        输出：2

        https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/07/sample_4_1610.png
        输入：grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
        输出：1

        输入：grid = [[1,1,1,1,1,1,1],
                    [1,0,0,0,0,0,1],
                    [1,0,1,1,1,0,1],
                    [1,0,1,0,1,0,1],
                    [1,0,1,1,1,0,1],
                    [1,0,0,0,0,0,1],
                    [1,1,1,1,1,1,1]]
        输出：2
        """
        # 将四周的岛屿都淹没，四周岛屿认为不是封闭岛屿，
        # 通过dfs淹没，将四周相连的岛屿去掉，变成水
        # 之后退化为计算岛屿数量的算法
        m = len(grid)
        n = len(grid[0])

        WATER = 1
        LAND = 0

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return

            if grid[i][j] == WATER:
                return

            grid[i][j] = WATER
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)

        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)

        res = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == LAND:
                    res += 1
                    dfs(i, j)
        return res

    def numEnclaves(self, grid: list[list[int]]) -> int:
        """1020. 飞地的数量
        给你一个大小为 m x n 的二进制矩阵 grid ，其中 0 表示一个海洋单元格、1 表示一个陆地单元格。

        一次 移动 是指从一个陆地单元格走到另一个相邻（上、下、左、右）的陆地单元格或跨过 grid 的边界。

        返回网格中 无法 在任意次数的移动中离开网格边界的陆地单元格的数量。

        输入：grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
        输出：3

        输入：grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
        输出：0
        """
        # 实际是求，不跟边界相连的岛屿的个数
        m = len(grid)
        n = len(grid[0])

        WATER = 0
        LAND = 1

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return

            if grid[i][j] == WATER:
                return

            grid[i][j] = WATER
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)

        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)

        res = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == LAND:
                    res += 1
        return res

    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        """695. 岛屿的最大面积

        给你一个大小为 m x n 的二进制矩阵 grid 。

        岛屿 是由一些相邻的 1 (代表土地) 构成的组合，
        这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。
        你可以假设 grid 的四个边缘都被 0（代表水）包围着。

        岛屿的面积是岛上值为 1 的单元格的数目。

        计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。

        输入：grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
        输出：6

        输入：grid = [[0,0,0,0,0,0,0,0]]
        输出：0
        """
        # 找到一个岛屿，进行整个岛淹没的时候，记录实际淹没的单元格，并返回
        m = len(grid)
        n = len(grid[0])

        WATER = 0
        LAND = 1

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0

            if grid[i][j] == WATER:
                return 0

            grid[i][j] = WATER

            return 1 + sum(
                [
                    dfs(i - 1, j),
                    dfs(i + 1, j),
                    dfs(i, j - 1),
                    dfs(i, j + 1),
                ]
            )

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == LAND:
                    res = max(res, dfs(i, j))

        return res

    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        """1905. 统计子岛屿
        给你两个 m x n 的二进制矩阵 grid1 和 grid2 ，它们只包含 0 （表示水域）和 1 （表示陆地）。
        一个 岛屿 是由 四个方向 （水平或者竖直）上相邻的 1 组成的区域。任何矩阵以外的区域都视为水域。

        如果 grid2 的一个岛屿，被 grid1 的一个岛屿 完全 包含，
        也就是说 grid2 中该岛屿的每一个格子都被 grid1 中同一个岛屿完全包含，
        那么我们称 grid2 中的这个岛屿为 子岛屿 。

        请你返回 grid2 中 子岛屿 的 数目 。

        输入：grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
        输出：3

        输入：grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
        输出：2
        """
        m = len(grid1)
        n = len(grid1[0])

        WATER = 0
        LAND = 1

        # dfs，识别一个岛屿，计数后，将其连通的所有单元格都变成水
        def dfs(grid, row, col):
            # 叶子节点
            if row < 0 or row >= m or col < 0 or col >= n:
                return

            # 限制条件
            if grid[row][col] == WATER:
                return

            # 做出选择
            grid[row][col] = WATER

            dfs(grid, row - 1, col)
            dfs(grid, row + 1, col)
            dfs(grid, row, col - 1)
            dfs(grid, row, col + 1)

        # 将非子岛屿淹没
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == LAND and grid1[i][j] == WATER:
                    dfs(grid2, i, j)

        island_count = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == LAND:
                    island_count += 1
                    dfs(grid2, i, j)

        return island_count

    def numDistinctIslands(self, grid: list[list[int]]) -> int:
        """694. 不同的岛屿数量

        输入一个二维矩阵，0 表示海水，1 表示陆地

        计算 不同的 (distinct) 岛屿数量

        比如题目输入下面这个二维矩阵：
        https://labuladong.online/algo/images/island/5.jpg
        [
            [1, 1, 0, 1, 1],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [1, 1, 0, 1, 1]
        ]

        其中有四个岛屿，但是左下角和右上角的岛屿形状相同，所以不同的岛屿共有三个，算法返回 3。
        """
        # 通过遍历的顺序，进行序列化记录，最后去重
        # 需要结合回溯的原理，记录当前递归的顺序，前序和后序都需要作为元素加进去，保证顺序
        res = set()

        m = len(grid)
        n = len(grid[0])
        LAND = 1
        WATER = 0
        path = []

        def dfs(i, j, base=0):
            if i < 0 or j < 0 or i >= m or j >= n:
                return

            if grid[i][j] == WATER:
                return

            grid[i][j] = WATER

            # 将当前遍历的所以加入 path
            # 需要记录的是从基础点位置的偏移值...
            cur = i * m + j - base
            path.append(cur)
            dfs(i - 1, j, base)
            dfs(i + 1, j, base)
            dfs(i, j - 1, base)
            dfs(i, j + 1, base)
            path.append(-cur)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == LAND:
                    path = []
                    dfs(i, j, i * m + j)
                    res.add(",".join(map(str, path)))
                    print(res)
                    path = []

        return len(res)

    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
        """967. 连续差相同的数字
        返回所有长度为 n 且满足其每两个连续位上的数字之间的差的绝对值为 k 的 非负整数 。

        请注意，除了 数字 0 本身之外，答案中的每个数字都 不能 有前导零。例如，01 有一个前导零，所以是无效的；但 0 是有效的。

        输入：n = 3, k = 7
        输出：[181,292,707,818,929]

        输入：n = 2, k = 1
        输出：[10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

        输入：n = 2, k = 0
        输出：[11,22,33,44,55,66,77,88,99]

        输入：n = 2, k = 2
        输出：[13,20,24,31,35,42,46,53,57,64,68,75,79,86,97]
        """
        # 组合数字，无重可复选
        # 选择项是当前数字 -k 或 +k 且在 0-9 之间
        # 需要对结果去重
        self.num = 0
        res = set()

        def backtrack(n, k):
            # base
            if n == 0:
                res.add(self.num)
                return

            for v in [self.num % 10 - k, self.num % 10 + k]:
                if 0 <= v < 10:
                    # 做选择
                    self.num = self.num * 10 + v
                    backtrack(n - 1, k)
                    # 撤销选择
                    self.num = int(self.num // 10)

        for i in range(1, 10):
            self.num = i
            backtrack(n - 1, k)

        return sorted(list(res))

    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        """491. 非递减子序列
        给你一个整数数组 nums ，找出并返回所有该数组中不同的递增子序列，递增子序列中 至少有两个元素 。你可以按 任意顺序 返回答案。

        数组中可能含有重复元素，如出现两个整数相等，也可以视作递增序列的一种特殊情况。

        输入：nums = [4,6,7,7]
        输出：[[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

        输入：nums = [4,4,3,2,1]
        输出：[[4,4]]
        """
        path = []
        res = []

        # 有重不可复选，需要剪枝
        def backtrack(nums, start):
            if len(path) >= 2:
                res.append(path.copy())

            # 同一层去重
            used = set()
            for i in range(start, len(nums)):
                # 剪枝，start后面元素，前面相同元素已经包含了当前的组合
                if nums[i] in used:
                    continue

                # 递增序列，比 path 最后元素小的不需要加入 path，但需要
                if path and nums[i] < path[-1]:
                    continue

                used.add(nums[i])
                path.append(nums[i])
                backtrack(nums, i + 1)
                path.pop()

        backtrack(nums, 0)
        return res
    
    def exist(self, board: list[list[str]], word: str) -> bool:
        """79. 单词搜索
        给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

        单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

        输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
        输出：true

        输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
        输出：true

        输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
        输出：false
        """
        # 岛屿问题

        m = len(board)
        n = len(board[0])

        def dfs(i, j, k):
            """基于i，j的位置，找跟 work[k] 相等的位置"""
            # i,j 表示访问的元素位置，k表示需要匹配的 word 的索引
            # 避免重复查找
            if i < 0 or j < 0 or i >= m or j >= n:
                return False

            if board[i][j] != word[k]:
                return False

            if k == len(word) - 1:
                return True

            board[i][j] = ''

            res = any([
                dfs(i - 1, j, k + 1),
                dfs(i + 1, j, k + 1),
                dfs(i, j - 1, k + 1),
                dfs(i, j + 1, k + 1),
            ])
            board[i][j] = word[k]
            return res

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False


if __name__ == "__main__":
    assert (
        Solution().numIslands(
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ]
        )
        == 1
    )
    assert (
        Solution().numIslands(
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ]
        )
        == 3
    )

    assert (
        Solution().closedIsland(
            [
                [1, 1, 1, 1, 1, 1, 1, 0],
                [1, 0, 0, 0, 0, 1, 1, 0],
                [1, 0, 1, 0, 1, 1, 1, 0],
                [1, 0, 0, 0, 0, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 0],
            ]
        )
        == 2
    )
    assert (
        Solution().closedIsland([[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]])
        == 1
    )
    assert (
        Solution().closedIsland(
            [
                [1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 1, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 1, 1, 0, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1],
            ]
        )
        == 2
    )

    assert (
        Solution().numEnclaves([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]])
        == 3
    )
    assert (
        Solution().numEnclaves([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]])
        == 0
    )

    assert (
        Solution().maxAreaOfIsland(
            [
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            ]
        )
        == 6
    )
    assert Solution().maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]) == 0
    assert (
        Solution().countSubIslands(
            [
                [1, 1, 1, 0, 0],
                [0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 1, 1],
            ],
            [
                [1, 1, 1, 0, 0],
                [0, 0, 1, 1, 1],
                [0, 1, 0, 0, 0],
                [1, 0, 1, 1, 0],
                [0, 1, 0, 1, 0],
            ],
        )
        == 3
    )
    assert (
        Solution().countSubIslands(
            [
                [1, 0, 1, 0, 1],
                [1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1],
                [1, 0, 1, 0, 1],
            ],
            [
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1],
                [0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0],
                [1, 0, 0, 0, 1],
            ],
        )
        == 2
    )

    assert (
        Solution().numDistinctIslands(
            [[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]
        )
        == 3
    )
    assert Solution().exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="ABCCED",
    )
    assert Solution().exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="SEE",
    )
    assert not Solution().exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="ABCB",
    )
    assert Solution().exist([["a"]], "a")
    assert Solution().exist([["a", "b"]], "ba")
    print("OK")
