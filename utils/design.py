class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """130. 被围绕的区域

        给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' 组成，捕获 所有 被围绕的区域：

        连接：一个单元格与水平或垂直方向上相邻的单元格连接。
        区域：连接所有 'O' 的单元格来形成一个区域。
        围绕：如果您可以用 'X' 单元格 连接这个区域，并且区域中没有任何单元格位于 board 边缘，则该区域被 'X' 单元格围绕。
        通过 原地 将输入矩阵中的所有 'O' 替换为 'X' 来 捕获被围绕的区域。你不需要返回任何值。


        输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
        输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
        https://pic.leetcode.cn/1718167191-XNjUTG-image.png

        类似下围棋，将被四周（包括边缘）都被 X 包围的 O 改成 X
        """
        # 找到四周为 O 的位置，dfs 遍历其四周是否也有 O，将周围连通的 O 改为 A
        # 最后将所有单元格，如果是 A 改成 O，即不进行覆盖，如果是 O 则改为 X

        m = len(board)
        n = len(board[0])

        def dfs(x, y):
            if not (
                0 <= x < m and
                0 <= y < n and
                board[x][y] == 'O'
            ):
                return
            
            board[x][y] = 'A'
            
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)

        for i in range(n):
            dfs(0, i)
            dfs(m - 1, i)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
