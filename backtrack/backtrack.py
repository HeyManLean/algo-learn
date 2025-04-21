# -*- coding: utf-8 -*-


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """46. 全排列
        给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

        输入：nums = [1,2,3]
        输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

        输入：nums = [0,1]
        输出：[[0,1],[1,0]]

        输入：nums = [1]
        输出：[[1]]
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

    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        """47. 全排列 II
        给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

        输入：nums = [1,1,2]
        输出：[[1,1,2],[1,2,1],[2,1,1]]

        输入：nums = [1,2,3]
        输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        """
        res = []
        path = []
        visited = [0] * len(nums)

        nums.sort()  # 保持大小顺序

        def backtrack(nums):
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for i, num in enumerate(nums):
                if visited[i]:
                    continue

                # 剪枝，如果元素相同，需要保障两个元素访问顺序固定，先访问前面再访问后面
                if i > 0 and num == nums[i - 1] and not visited[i - 1]:
                    continue

                visited[i] = 1
                path.append(num)
                backtrack(nums)
                path.pop()
                visited[i] = 0

        backtrack(nums)
        return res

    def solveSudoku(self, board: list[list[str]]) -> None:
        """37. 解数独
        编写一个程序，通过填充空格来解决数独问题。

        数独的解法需 遵循如下规则：

        数字 1-9 在每一行只能出现一次。
        数字 1-9 在每一列只能出现一次。
        数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
        数独部分空格内已填入了数字，空白格用 '.' 表示。

        https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/04/12/250px-sudoku-by-l2g-20050714svg.png

        https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/04/12/250px-sudoku-by-l2g-20050714_solutionsvg.png
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

    def solve_n_queens(self, n: int) -> list[list[str]]:
        """使用标准的回溯写法实现N皇后"""
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

    def solveNQueens(self, n: int) -> list[list[str]]:
        """51. N 皇后
        按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。

        n 皇后问题 研究的是如何将 n 个皇后放置在 n*n 的棋盘上，并且使皇后彼此之间不能相互攻击。
        给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
        每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

        输入：n = 4
        输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

        输入：n = 1
        输出：[["Q"]]
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

    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        """216. 组合总和 III
        找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：

        只使用数字1到9
        每个数字 最多使用一次
        返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。

        输入: k = 3, n = 7
        输出: [[1,2,4]]

        输入: k = 3, n = 9
        输出: [[1,2,6], [1,3,5], [2,3,4]]

        输入: k = 4, n = 1
        输出: []
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
                path.pop()

        backtrack(k, n, 0)
        return res

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        """39. 组合总和
        给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，
        找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，
        并以列表形式返回。你可以按 任意顺序 返回这些组合。

        candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。

        对于给定的输入，保证和为 target 的不同组合数少于 150 个。

        输入：candidates = [2,3,6,7], target = 7
        输出：[[2,2,3],[7]]

        输入: candidates = [2,3,5], target = 8
        输出: [[2,2,2,2],[2,3,3],[3,5]]

        输入: candidates = [2], target = 1
        输出: []
        """
        path = []
        res = []

        def backtrack(target, start):
            if target == 0:
                res.append(path.copy())
            if target <= 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(target - candidates[i], i)  # 可以重复选取，不需要递增 i
                path.pop()

        backtrack(target, 0)
        return res

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        """40. 组合总和 II
        给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

        candidates 中的每个数字在每个组合中只能使用 一次 。

        注意：解集不能包含重复的组合。

        输入: candidates = [10,1,2,7,6,1,5], target = 8,
        输出:[[1,1,6],[1,2,5],[1,7],[2,6]]

        输入: candidates = [2,5,2,1,2], target = 5,
        输出:[[1,2,2],[5]]
        """
        path = []
        res = []
        # 数字只能使用一次，按照索引向前取值
        candidates.sort()

        def backtrack(target, start):
            if target == 0:
                res.append(path.copy())
            if target <= 0:
                return

            # 同一层元素不能复选，# 剪枝，如果前面的相同数值已经处理过，说明一定会包含了下一个相同数值的处理结果
            used = set()
            for i in range(start, len(candidates)):
                if candidates[i] in used:
                    continue

                used.add(candidates[i])
                path.append(candidates[i])
                backtrack(target - candidates[i], i + 1)
                path.pop()

        backtrack(target, 0)
        return res

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
        # 一般需要排序后操作，保证递增
        # 但是循环里面会保证递增，且需要保证顺序
        path = []
        res = []

        # 有重不可复选，需要剪枝
        def backtrack(nums, start):
            if len(path) >= 2:
                res.append(path.copy())

            # 同一层去重
            used = set()
            for i in range(start, len(nums)):
                # 剪枝，前面同元素，已经可以包含后面同元素的所有子集，不需要重复遍历
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

    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        """980. 不同路径 III
        在二维网格 grid 上，有 4 种类型的方格：

        1 表示起始方格。且只有一个起始方格。
        2 表示结束方格，且只有一个结束方格。
        0 表示我们可以走过的空方格。
        -1 表示我们无法跨越的障碍。
        返回在四个方向（上、下、左、右）上行走时，从起始方格到结束方格的不同路径的数目。

        每一个无障碍方格都要通过一次，但是一条路径中不能重复通过同一个方格。

        输入：[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
        输出：2

        输入：[[1,0,0,0],[0,0,0,0],[0,0,0,2]]
        输出：4

        输入：[[0,1],[2,0]]
        输出：0
        """
        # 记录已经经过的路径
        # 每次做出选择上下左右四个且为空格、未走过的方格，直到无路可用
        # 如果访问的节点和总空格数一致，则结果+1
        m = len(grid)
        n = len(grid[0])

        empty_num = 0
        start_i = 0
        start_j = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    empty_num += 1
                elif grid[i][j] == 1:
                    start_i = i
                    start_j = j

        self.count = 0
        self.res = 0

        def dfs(grid, i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return

            # 该路径走到了终点，判断是否走完了全部空格
            if grid[i][j] == 2:
                if self.count == empty_num:
                    self.res += 1

            if grid[i][j] != 0:
                return

            grid[i][j] = 1
            self.count += 1

            dfs(grid, i - 1, j)
            dfs(grid, i + 1, j)
            dfs(grid, i, j - 1)
            dfs(grid, i, j + 1)

            self.count -= 1
            grid[i][j] = 0

        dfs(grid, start_i - 1, start_j)
        dfs(grid, start_i + 1, start_j)
        dfs(grid, start_i, start_j - 1)
        dfs(grid, start_i, start_j + 1)
        return self.res

    def partition(self, s: str) -> list[list[str]]:
        """131. 分割回文串
        给你一个字符串 s，请你将 s 分割成一些 子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。

        输入：s = "aab"
        输出：[["a","a","b"],["aa","b"]]

        输入：s = "a"
        输出：[["a"]]
        """

        def is_palindromic(s: str):
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        # 回溯或dfs，主要定义选择项
        # 该题主要选择在于，每访问一个元素，是否需要对该元素进行切割两个选择
        # 选择切换的前提是前面的子串是回文

        # 记录当前切割的子串列表
        path = []
        # 最后有效的 path 结果列表
        res = []

        # start 表示上次切割的位置下一个元素，i表示当前位置
        def dfs(s, start, i):
            if i == len(s):
                # 最后一个元素访问后且也加入了path，如果path有值，则加入结果中
                if path and i == start:
                    res.append(path.copy())
                return

            # 找到一个回文子串，做两个选择，1. 切割加到path，2. 继续遍历
            if is_palindromic(s[start : i + 1]):
                path.append(s[start : i + 1])
                dfs(s, i + 1, i + 1)
                path.pop()

            dfs(s, start, i + 1)

        dfs(s, 0, 0)
        return res

    def restoreIpAddresses(self, s: str) -> list[str]:
        """93. 复原 IP 地址

        有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

        例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，
        但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。
        给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，
        这些地址可以通过在 s 中插入 '.' 来形成。你 不能 重新排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。

        输入：s = "25525511135"
        输出：["255.255.11.135","255.255.111.35"]

        输入：s = "0000"
        输出：["0.0.0.0"]

        输入：s = "101023"
        输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
        """

        def validate_part(part: str):
            if part.startswith("0") and len(part) > 1:
                return False
            return 0 <= int(part) < 256

        path = []
        res = []

        # 如果partok，做切割选择并回撤
        # 后面继续进行dfs
        def dfs(s, start, i):
            if i == len(s):
                if len(path) == 4 and start == i:
                    res.append(".".join(path))
                return

            if validate_part(s[start : i + 1]):
                path.append(s[start : i + 1])
                dfs(s, i + 1, i + 1)
                path.pop()

            dfs(s, start, i + 1)

        dfs(s, 0, 0)
        return res

    def letterCombinations(self, digits: str) -> list[str]:
        """17. 电话号码的字母组合
        给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

        给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

        https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/11/09/200px-telephone-keypad2svg.png

        输入：digits = "23"
        输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]

        输入：digits = ""
        输出：[]

        输入：digits = "2"
        输出：["a","b","c"]
        """
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        path = []
        res = []

        # 第 i 轮，从第 i 个数字对应的字母，取任意一个数，接着进行 i + 1 的 dfs
        def dfs(digits, i):
            # 最后一个数字，则加入结果中
            if i == len(digits):
                if path:
                    res.append("".join(path))
                return

            for c in mapping[digits[i]]:
                path.append(c)
                dfs(digits, i + 1)
                path.pop()

        dfs(digits, 0)
        return res




if __name__ == "__main__":
    assert Solution().permute([1, 2, 3]) == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]
    assert Solution().permute([0, 1]) == [[0, 1], [1, 0]]
    assert Solution().permute([1]) == [[1]]
    assert Solution().permuteUnique([1, 1, 2]) == [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    assert Solution().permuteUnique([1, 2, 3]) == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    Solution().solveSudoku(board)
    assert board == [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
    ]
    assert Solution().solveNQueens(4) == [
        [".Q..", "...Q", "Q...", "..Q."],
        ["..Q.", "Q...", "...Q", ".Q.."],
    ]
    assert Solution().solveNQueens(1) == [["Q"]]

    assert Solution().combinationSum3(k=3, n=7) == [[1, 2, 4]]
    assert Solution().combinationSum3(k=3, n=9) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
    assert Solution().combinationSum3(k=4, n=1) == []

    assert Solution().combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert Solution().combinationSum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert Solution().combinationSum([2], 1) == []

    assert Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8) == [
        [1, 1, 6],
        [1, 2, 5],
        [1, 7],
        [2, 6],
    ]
    assert Solution().combinationSum2([2, 5, 2, 1, 2], 5) == [[1, 2, 2], [5]]
    assert (
        Solution().combinationSum2(
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            27,
        )
        == []
    )
    assert Solution().numsSameConsecDiff(3, 7) == [181, 292, 707, 818, 929]
    assert Solution().numsSameConsecDiff(2, 1) == [
        10,
        12,
        21,
        23,
        32,
        34,
        43,
        45,
        54,
        56,
        65,
        67,
        76,
        78,
        87,
        89,
        98,
    ]
    assert Solution().numsSameConsecDiff(2, 0) == [11, 22, 33, 44, 55, 66, 77, 88, 99]
    assert Solution().numsSameConsecDiff(2, 2) == [
        13,
        20,
        24,
        31,
        35,
        42,
        46,
        53,
        57,
        64,
        68,
        75,
        79,
        86,
        97,
    ]
    assert Solution().findSubsequences([4, 6, 7, 7]) == [
        [4, 6],
        [4, 6, 7],
        [4, 6, 7, 7],
        [4, 7],
        [4, 7, 7],
        [6, 7],
        [6, 7, 7],
        [7, 7],
    ]
    assert Solution().findSubsequences([4, 4, 3, 2, 1]) == [[4, 4]]
    assert Solution().uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]) == 2
    assert Solution().uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]) == 4
    assert Solution().uniquePathsIII([[0, 1], [2, 0]]) == 0

    assert Solution().partition(s="aab") == [["a", "a", "b"], ["aa", "b"]]
    assert Solution().partition(s="a") == [["a"]]

    assert Solution().restoreIpAddresses("25525511135") == [
        "255.255.11.135",
        "255.255.111.35",
    ]
    assert Solution().restoreIpAddresses("101023") == [
        "1.0.10.23",
        "1.0.102.3",
        "10.1.0.23",
        "10.10.2.3",
        "101.0.2.3",
    ]
    assert Solution().restoreIpAddresses("0000") == ["0.0.0.0"]

    assert Solution().letterCombinations("23") == [
        "ad",
        "ae",
        "af",
        "bd",
        "be",
        "bf",
        "cd",
        "ce",
        "cf",
    ]
    assert Solution().letterCombinations("") == []
    assert Solution().letterCombinations("2") == ["a", "b", "c"]

    print("OK")
