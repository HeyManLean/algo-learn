# 回溯算法&DFS

相当于遍历一颗决策树的过程
- 每个节点会做出多种不同选择，会形成不同的路径
- 到了每个叶子节点，会获得其中一个答案

特点：
- 多层选择
- 每层选择项，有限制条件

## 回溯算法（基本框架）

主要处理排列、组合、子集问题，关键词
1. 叶子节点：也就是结束时的时机；
2. 选择列表：在每一层识别出 **选择列表**；
3. 限制条件：选择列表中，部分不能选，如同一路径不能重复访问同一节点，撤销选择后可以再次访问


```py
result = []
def backtrack(路径，选择列表):
    if 叶子节点：
        result.add(路径)
        return

    for 选择 in 选择列表:
        限制条件判断
        做选择
        backtrack(路径，选择列表)
        撤销选择
```

### 全排列（46）

1. 叶子节点：路径长度跟数组一样时；
2. 选择列表：在数组中，该路径未访问过的数字
3. visited 数组判断同一路径是否重复，撤销选择时，移除节点

```py
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """给定一个不含重复数字的数组 nums ，返回所有可能的全排列"""
        visited = [0] * len(nums)
        path = []
        res = []

        def backtrack(nums):
            # 满足条件，加入结果
            if len(nums) == len(path):
                res.append(list(path))
                return

            # 选择列表
            for i, num in enumerate(nums):
                if visited[i]:
                    continue
                # 做选择
                visited[i] = 1
                path.append(num)
                # 进入下一层决策树
                backtrack(nums)
                # 撤销选择
                visited[i] = 0
                path.pop()

        backtrack(nums)
        return res
```

### N 皇后问题（51）

要求是：同一行、同一列、同一条对角线，只能放一个皇后，共有 N 个皇后；
- 叶子节点：N个皇后都放置成功，即最后一行放置成功，每一层就是一行
- 选择列表：选择 N 列填入
- 限制条件：满足同一列没有皇后，左上和右上斜角线没有皇后

```py
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        """51. N 皇后
        将 n 个皇后放置在 n*n 的棋盘上，并且使皇后彼此之间不能相互攻击。
        
        给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
        每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
        """
        res = []
        board = []
        base = '.' * n

        used_cols = [0] * n

        def can_queen(row, col):
            # 左上斜线
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            # 右上斜线
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            return True

        def backtrack(row: int):
            # 到达最后一行
            if row == n:
                res.append(board.copy())
                return

            for col in range(n):
                if used_cols[col]:
                    continue

                if not can_queen(row, col):
                    continue

                # 做出选择，加入路径
                used_cols[col] = 1
                board.append(base[:col] + 'Q' + base[col+1:])

                # 回溯下一层
                backtrack(row + 1)

                # 撤销选择, 移除路径
                used_cols[col] = 0
                board.pop()

        backtrack(0)
        return res
```

### 解数独（37）

- 叶子结点：矩阵最后一个元素填入结束
- 每层选择列表：数组1-9
- 限制条件：同一列同一行同一个九宫格不能重复

```py
class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """37. 解数独
        编写一个程序，通过填充空格来解决数独问题。

        数独的解法需 遵循如下规则：
        数字 1-9 在每一行只能出现一次。
        数字 1-9 在每一列只能出现一次。
        数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
        数独部分空格内已填入了数字，空白格用 '.' 表示。
        """
        # 叶子结点：矩阵最后一个元素填入结束
        # 每层选择列表：数组1-9，同一列同一行同一个九宫格不能重复
        n = len(board)
        choices = "123456789"

        used_rows = [set() for _ in range(n)]
        used_cols = [set() for _ in range(n)]
        used_boxes = [set() for _ in range(n)]

        def get_box_index(row, col):
            return row // 3 * 3 + col // 3

        for row in range(n):
            for col in range(n):
                if board[row][col] != '.':
                    used_rows[row].add(board[row][col])
                    used_cols[col].add(board[row][col])
                    used_boxes[get_box_index(row, col)].add(board[row][col])

        def is_valid(row, col, val):
            # 同一行不能重复
            if val in used_rows[row]:
                return False

            # 同一列不能重复
            if val in used_cols[col]:
                return False

            # 同一个九宫格
            if val in used_boxes[get_box_index(row, col)]:
                return False
            return True

        def backtrack(board, pos):
            if pos >= n * n:
                return True
            row, col = divmod(pos, n)

            if board[row][col] != '.':
                return backtrack(board, pos + 1)

            # 选择列表
            for val in choices:
                # 限制条件
                if not is_valid(row, col, val):
                    continue

                # 做出选择，加入路径
                used_rows[row].add(val)
                used_cols[col].add(val)
                used_boxes[get_box_index(row, col)].add(val)
                board[row][col] = val

                # 下一层决策
                if backtrack(board, pos + 1):
                    return True

                # 撤销选择
                board[row][col] = '.'
                used_rows[row].remove(val)
                used_cols[col].remove(val)
                used_boxes[get_box_index(row, col)].remove(val)

            return False

        backtrack(board, 0)
```

## 回溯算法（排列、组合、子集问题）

给定一个数组，按照规则得出所需排列、组合或子集

分为三种变体：
1. 无重复元素，不可复选
2. 有重复元素，不可复选
3. 无重复元素，可复选

组合和子集：不要求元素顺序，可能重复结果
1. 限制：通过 start 记录下一个选择的开始位置，避免回头选择
2. 剪枝：同一层，相同元素只需要回溯一次
- 选择第一个元素包含了后面元素所有子集和组合

排列：支持回头选择，但是可能存在重复排列
1. 限制：使用 visited 维护路径已经访问过的元素，同一路径不能重复选择
2. 剪枝：同一路径，同一个元素访问顺序全局一致
- 后面一个同元素访问，必须要保证前一个同元素已经访问（在visited中）

### 组合子集：组合总和3（216）

无重复元素，不可复选
- 使用 start 记录下一个选择开始位置

```py
class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        """216. 组合总和 III
        找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：
        只使用数字1到9，每个数字最多使用一次，返回所有可能的有效组合的列表

        输入: k = 3, n = 7
        输出: [[1,2,4]]
        """
        res = []
        path = []
        nums = [i for i in range(1, 10)]

        def backtrack(k, n, start):
            # 叶子节点
            if k == 0 and n == 0:
                res.append(path.copy())
                return

            # 选择项
            for i in range(start, 9):
                # 限制条件是从上一个数下一个位置开始选择，start

                # 做出选择
                path.append(nums[i])
                backtrack(k - 1, n - nums[i], i + 1)
                # 撤销选择
                path.pop()

        backtrack(k, n, 0)
        return res
```

### 组合子集：子集2（90）

有重复元素不可复选
- 叶子节点：每一层都是
- 选择项：给定数组
- 限制条件：同一层，相同元素只需要回溯一次

```py
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        nums.sort()

        def backtrack(nums, start):
            # 叶子节点，只有要路径就可以添加到子集
            res.append(path.copy())

            # 剪枝：同一层不可复选
            visited = set()
            for i in range(start, len(nums)):
                # 限制条件
                if nums[i] in visited:
                    continue

                # 做出选择
                visited.add(nums[i])
                path.append(nums[i])

                backtrack(nums, i + 1)

                # 撤销选择
                path.pop()

        backtrack(nums, 0)
        return res
```

### 排列：全排列（46）

无重不可复选
- 叶子节点：路径元素跟数组长度一样时
- 选择列表：给定的数组
- 限制条件：同路径元素不能复选

```py
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """46. 全排列
        给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列

        输入：nums = [1,2,3]
        输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        """
        visited = [0] * len(nums)
        path = []
        res = []

        def backtrack(nums):
            # 叶子节点
            if len(nums) == len(path):
                res.append(list(path))
                return

            # 选择列表
            for i, num in enumerate(nums):
                # 限制条件，同路径不同重复访问
                if visited[i]:
                    continue

                # 做出选择
                visited[i] = 1
                path.append(num)

                backtrack(nums)

                # 撤销选择
                visited[i] = 0
                path.pop()

        backtrack(nums)
        return res
```

### 排列：全排列2（47）

- 叶子节点：元素个数跟数组一样
- 选择列表：给定数组
- 限制条件：同元素，必须保证先访问前面才能访问后面

```py
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        visited = [0] * len(nums)

        nums.sort()  # 保持大小顺序

        def backtrack(nums):
            # 叶子节点
            if len(path) == len(nums):
                res.append(path.copy())
                return

            # 选择列表
            for i, num in enumerate(nums):
                # 限制条件：不能重复访问
                if visited[i]:
                    continue

                # 剪枝，如果元素相同，需要保障两个元素访问顺序固定，先访问前面再访问后面
                if i > 0 and num == nums[i - 1] and not visited[i - 1]:
                    continue

                # 做出选择
                visited[i] = 1
                path.append(num)

                backtrack(nums)

                # 撤销选择
                path.pop()
                visited[i] = 0

        backtrack(nums)
        return res
```

## DFS 问题（岛屿）

回溯算法的选择是在每一层子选择项做出，DFS 是在该层遍历前做出
- 限制条件：全局不能重复访问

框架
```py
def dfs(grid: list:list[int], i, j):
    if 叶子节点:
        return

    做出选择

    # 下一层 DFS
    # 限制条件是上下左右是否能访问
    dfs(grid, i - 1, j)
    dfs(grid, i + 1, j)
    dfs(grid, i, j - 1)
    dfs(grid, i, j + 1)

```

### 岛屿数量（200）

遍历整个矩阵，识别一个岛屿时，将该岛屿通过 dfs 进行淹没

```py
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """00. 岛屿数量
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
```

### 统计子岛屿（1905）

- 子岛屿：找到 grid2 的岛屿，该岛屿每个陆地单元格在 grid 1 也是陆地
1. 先将非子岛屿的岛屿全部淹没
2. 剩下就回退到统计岛屿数量的问题


```py
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
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
```


### 不同的岛屿数量（694）

```py
class Solution:
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
                    path = []

        return len(res)
```

### 单次搜索（79）


```py
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        """79. 单词搜索
        给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

        单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

        输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
        输出：true
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
```

## BFS 算法

在多层选择中，找到**最短路径**的结果，使用 BFS 层序遍历
- 叶子节点：满足结果时
- 选择列表：邻居节点
- 限制条件：全局不能重复访问

### 钥匙和房间（841）

- 叶子节点：所有房间都访问过
- 选择列表：当前房间钥匙集合可以打开的房间列表
- 限制条件：不需要重复访问某个房间

```py
class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        """841. 钥匙和房间

        有 n 个房间，房间按从 0 到 n - 1 编号。最初，除 0 号房间外的其余所有房间都被锁住。
        当你进入一个房间，你可能会在里面找到一套 不同的钥匙，每把钥匙上都有对应的房间号，即表示钥匙可以打开的房间。你可以拿上所有钥匙去解锁其他房间。

        给你一个数组 rooms 其中 rooms[i] 是你进入 i 号房间可以获得的钥匙集合。
        如果能进入 所有 房间返回 true，否则返回 false。

        输入：rooms = [[1],[2],[3],[]]
        输出：true
        """
        # 通过 visited 记录
        # 到达一个房间，可以找到通往其他房间的钥匙，类似于bfs比那里
        visited = [0] * len(rooms)
        visited[0] = 1

        q = list(rooms[0])
        while q:
            i = q.pop(0)

            # 限制条件
            if visited[i]:
                continue
            visited[i] = 1

            # 叶子节点
            if sum(visited) == len(rooms):
                return True

            # 选择列表
            for j in rooms[i]:
                q.append(j)

        return False
```

### 打开转盘锁（752）

- 叶子节点：当前数字串跟 target 数字串一致
- 选择列表：数字串，每个数字向上或向下旋转一次，数目为数字串长度*2
- 限制条件：不能重复访问同一数字串；不能在死锁列表中

```py
class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        """752. 打开转盘锁
        你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字：'0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。每个拨轮可以自由旋转：例如把 '9' 变为 '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。

        锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。

        列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。
        字符串 target 代表可以解锁的数字，你需要给出解锁需要的最小旋转次数，如果无论如何不能解锁，返回 -1 。

        输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
        输出：6
        """
        # 每次选择是，四个数字选一个进行旋转，+1 或 -1，且不能再 deadends 中
        # 使用 visited 保证不会重复访问
        def rotate(s: str, i: int, direction=1):
            c = (10 + int(s[i]) + direction) % 10
            return s[:i] + str(c) + s[i + 1 :]

        def get_neighbors(s: str):
            res = []
            for i in range(len(s)):
                res.append(rotate(s, i, 1))
                res.append(rotate(s, i, -1))
            return res

        start = "0000"
        visited = set()
        visited.add(start)
        q = [start]
        step = 0
        while q:
            # 每层代表做出一次选择
            for _ in range(len(q)):
                word = q.pop(0)
                if word in deadends:
                    return -1
                if word == target:
                    return step

                for s in get_neighbors(word):
                    if s in visited:
                        continue
                    if s in deadends:
                        continue
                    visited.add(s)
                    q.append(s)

            step += 1

        return -1
```

### 打开转盘锁（752）（双向BFS）

双向 BFS，从初始状态和目标状态双向 BFS，维护两个队列
1. 每轮只需要BFS遍历第一个队列
- 如果第一个队列比第二个长，则交换
- 维持针对较小队列进行bfs
2. 叶子节点：第一个队列的选择项在第二个队列中，认为结束

```py
class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        # 使用双向bfs，直到target和初始状态
        # 每次只使用 q1 向下遍历，当 q1 长度比 q2大是，交换q1和q2
        # 直到 q1 遍历的邻节点在 q2 中结束
        def rotate(s: str, i: int, direction=1):
            c = (10 + int(s[i]) + direction) % 10
            return s[:i] + str(c) + s[i + 1 :]

        def get_neighbors(s: str):
            res = []
            for i in range(len(s)):
                res.append(rotate(s, i, 1))
                res.append(rotate(s, i, -1))
            return re

        start = "0000"
        if start == target:
            return 0
        q1 = set([start])
        q2 = set([target])
        visited = set([start, target])
        step = 0

        while q1 and q2:
            step += 1
            new_q1 = set()
            for word in q1:
                if word in deadends:
                    continue
                for s in get_neighbors(word):
                    if s in q2:
                        return step
                    if s in visited:
                        continue
                    if s in deadends:
                        continue
                    visited.add(s)
                    new_q1.add(s)

            q1 = new_q1
            if len(q1) > len(q2):
                q1, q2 = q2, q1

        return -1
```


### 最小基因变化（433）

- 叶子节点：到达目标序列
- 选择列表：给定数组
- 限制条件：不能重复访问同一个基因串，选择项跟当前基因串差异个数为1

```py
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        """433. 最小基因变化

        例如，"AACCGGTT" --> "AACCGGTA" 就是一次基因变化。
        另有一个基因库 bank 记录了所有有效的基因变化，只有基因库中的基因才是有效的基因序列。（变化后的基因必须位于基因库 bank 中）

        给你两个基因序列 start 和 end ，以及一个基因库 bank ，
        请你找出并返回能够使 start 变化为 end 所需的最少变化次数。如果无法完成此基因变化，返回 -1 。

        输入：start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
        输出：1
        """
        if endGene not in bank:
            return -1

        # 1. 找出每个有效序列，跟 start 的差异字符数量
        # 2. 维护一个数组，元素 i 表示跟 start 差异字符为 i 的字符数组
        # 3. 进行 bfs 遍历
        def count_diff(gene1, gene2):
            diff_count = 0
            for i, c in enumerate(gene1):
                if c != gene2[i]:
                    diff_count += 1
            return diff_count

        # 每轮只能更换一个，如果该更换次数对应的数组没有，则返回-1
        q = [startGene]
        visited = set()
        step = 0
        while q:
            for _ in range(len(q)):
                gene = q.pop(0)
                if gene == endGene:
                    return step

                if gene in visited:
                    continue
                visited.add(gene)

                for next_gene in bank:
                    if count_diff(next_gene, gene) == 1:
                        q.append(next_gene)

            step += 1

        return -1
```