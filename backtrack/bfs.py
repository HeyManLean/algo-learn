# -*- coding: utf-8 -*-


class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        """773. 滑动谜题

        在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示,
        以及一块空缺用 0 来表示。一次 移动 定义为选择 0 与一个相邻的数字（上下左右）进行交换.

        最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。

        给出一个谜板的初始状态 board ，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。
        输入：board = [[1,2,3],[4,0,5]]
        输出：1

        输入：board = [[1,2,3],[5,4,0]]
        输出：-1

        输入：board = [[4,1,2],[5,0,3]]
        输出：5
        """
        # 使用bfs，先到达终点，则返回ok
        # 使用 visited 判断是否走过
        m = len(board)
        n = len(board[0])

        def get_neigbor(s: str):
            zero = s.index("0")

            res = []
            zero_x = zero // n
            zero_y = zero % n

            neighbors = []
            if zero_x >= 1:
                neighbors.append((zero_x - 1) * n + zero_y)
            if zero_x < m - 1:
                neighbors.append((zero_x + 1) * n + zero_y)
            if zero_y >= 1:
                neighbors.append(zero_x * n + zero_y - 1)
            if zero_y < n - 1:
                neighbors.append(zero_x * n + zero_y + 1)

            for j in neighbors:
                res.append(swap(s, zero, j))
            return res

        def swap(s, i, j):
            cl = list(s)
            cl[i], cl[j] = cl[j], cl[i]
            return "".join(cl)

        visited = set()
        target = "123450"
        start = ""
        for i in range(m):
            for j in range(n):
                start += str(board[i][j])

        q = [start]
        visited.add(start)
        step = 0
        while q:
            for _ in range(len(q)):
                cur = q.pop(0)
                if cur == target:
                    return step

                for neighbor in get_neigbor(cur):
                    if neighbor in visited:
                        continue

                    visited.add(neighbor)
                    q.append(neighbor)

            step += 1

        return -1

    def openLock2(self, deadends: list[str], target: str) -> int:
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
            return [s for s in res if s not in deadends]

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
                    visited.add(s)
                    new_q1.add(s)

            q1 = new_q1
            if len(q1) > len(q2):
                q1, q2 = q2, q1

        return -1

    def openLock(self, deadends: list[str], target: str) -> int:
        """752. 打开转盘锁
        你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字：
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。
        每个拨轮可以自由旋转：例如把 '9' 变为 '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。

        锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。

        列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，
        这个锁将会被永久锁定，无法再被旋转。
        字符串 target 代表可以解锁的数字，你需要给出解锁需要的最小旋转次数，
        如果无论如何不能解锁，返回 -1 。

        输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
        输出：6

        输入: deadends = ["8888"], target = "0009"
        输出：1

        输入: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
        输出：-1"""

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
            return [s for s in res if s not in deadends]

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
                    visited.add(s)
                    q.append(s)

            step += 1

        return -1

    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        """841. 钥匙和房间

        有 n 个房间，房间按从 0 到 n - 1 编号。最初，除 0 号房间外的其余所有房间都被锁住。
        你的目标是进入所有的房间。然而，你不能在没有获得钥匙的时候进入锁住的房间。

        当你进入一个房间，你可能会在里面找到一套 不同的钥匙，每把钥匙上都有对应的房间号，
        即表示钥匙可以打开的房间。你可以拿上所有钥匙去解锁其他房间。

        给你一个数组 rooms 其中 rooms[i] 是你进入 i 号房间可以获得的钥匙集合。
        如果能进入 所有 房间返回 true，否则返回 false。

        输入：rooms = [[1],[2],[3],[]]
        输出：true

        输入：rooms = [[1,3],[3,0,1],[2],[0]]
        输出：false
        """
        # 通过 visited 记录
        # 到达一个房间，可以找到通往其他房间的钥匙，类似于bfs比那里
        visited = [0] * len(rooms)
        visited[0] = 1

        q = list(rooms[0])
        while q:
            i = q.pop(0)
            if visited[i]:
                continue
            visited[i] = 1

            for j in rooms[i]:
                q.append(j)

        return sum(visited) == len(rooms)

    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        """433. 最小基因变化

        基因序列可以表示为一条由 8 个字符组成的字符串，其中每个字符都是 'A'、'C'、'G' 和 'T' 之一。

        假设我们需要调查从基因序列 start 变为 end 所发生的基因变化。
        一次基因变化就意味着这个基因序列中的一个字符发生了变化。

        例如，"AACCGGTT" --> "AACCGGTA" 就是一次基因变化。
        另有一个基因库 bank 记录了所有有效的基因变化，只有基因库中的基因才是有效的基因序列。（变化后的基因必须位于基因库 bank 中）

        给你两个基因序列 start 和 end ，以及一个基因库 bank ，
        请你找出并返回能够使 start 变化为 end 所需的最少变化次数。如果无法完成此基因变化，返回 -1 。

        注意：起始基因序列 start 默认是有效的，但是它并不一定会出现在基因库中。

        输入：start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
        输出：1

        输入：start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
        输出：2

        输入：start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
        输出：3
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

    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        """1926. 迷宫中离入口最近的出口
        给你一个 m x n 的迷宫矩阵 maze （下标从 0 开始），矩阵中有空格子（用 '.' 表示）和墙（用 '+' 表示）。
        同时给你迷宫的入口 entrance ，用 entrance = [entrancerow, entrancecol] 表示你一开始所在格子的行和列。

        每一步操作，你可以往 上，下，左 或者 右 移动一个格子。你不能进入墙所在的格子，你也不能离开迷宫。
        你的目标是找到离 entrance 最近 的出口。出口 的含义是 maze 边界 上的 空格子。entrance 格子 不算 出口。

        请你返回从 entrance 到最近出口的最短路径的 步数 ，如果不存在这样的路径，请你返回 -1
        """
        if maze[entrance[0]][entrance[1]] == "+":
            return -1
        # bfs 只需要提前找到终点即可，dfs 需要遍历找到最优的结果
        q = [entrance]
        m = len(maze)
        n = len(maze[0])

        # 将经过的地方变成墙
        maze[entrance[0]][entrance[1]] = "+"
        visited = [0] * m * n
        step = 0

        while q:
            for _ in range(len(q)):
                i, j = q.pop(0)

                # 到达边界就是出口了
                if maze[i][j] == ".":
                    if i == 0 or i == m - 1:
                        return step
                    if j == 0 or j == n - 1:
                        return step

                if visited[i * n + j]:
                    continue
                visited[i * n + j] = 1

                if i > 0 and maze[i - 1][j] == ".":
                    q.append([i - 1, j])
                if i < m - 1 and maze[i + 1][j] == ".":
                    q.append([i + 1, j])
                if j > 0 and maze[i][j - 1] == ".":
                    q.append([i, j - 1])
                if j < n - 1 and maze[i][j + 1] == ".":
                    q.append([i, j + 1])

            step += 1

        return -1

    def orangesRotting(self, grid: list[list[int]]) -> int:
        """994. 腐烂的橘子
        在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：

        值 0 代表空单元格；
        值 1 代表新鲜橘子；
        值 2 代表腐烂的橘子。
        每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。

        返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。
        """
        # 从腐烂的橘子开始，每轮遍历，将其周围橘子都变成腐烂，如果当前腐烂橘子等于橘子总数则结束
        m = len(grid)
        n = len(grid[0])

        total = 0
        rotted = 0
        q = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotted += 1
                    q.append((i, j))
                if grid[i][j] != 0:
                    total += 1

        if total == rotted:
            return 0

        def get_next_freshes(i, j):
            freshes = []
            for diff in [
                [-1, 0],
                [1, 0],
                [0, -1],
                [0, 1],
            ]:
                if i + diff[0] < 0 or i + diff[0] >= m:
                    continue
                if j + diff[1] < 0 or j + diff[1] >= n:
                    continue
                freshes.append((i + diff[0], j + diff[1]))
            return freshes

        step = 0
        visited = [0] * m * n
        while q:
            for _ in range(len(q)):
                i, j = q.pop(0)
                if grid[i][j] == 1:
                    rotted += 1
                    grid[i][j] = 2

                if rotted == total:
                    return step

                if visited[i * n + j]:
                    continue
                visited[i * n + j] = 1

                for next_i, next_j in get_next_freshes(i, j):
                    if grid[next_i][next_j] == 1:
                        q.append((next_i, next_j))

            step += 1

        return -1

    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        """127. 单词接龙
        字典 wordList 中从单词 beginWord 到 endWord 的 转换序列 是一个按下述规格形成的序列 beginWord -> s1 -> s2 -> ... -> sk：

        每一对相邻的单词只差一个字母。
        对于 1 <= i <= k 时，每个 si 都在 wordList 中。注意， beginWord 不需要在 wordList 中。
        sk == endWord
        给你两个单词 beginWord 和 endWord 和一个字典 wordList ，返回 从 beginWord 到 endWord 的 最短转换序列 中的 单词数目 。如果不存在这样的转换序列，返回 0 。

        输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
        输出：5

        输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
        输出：0
        """
        # 需要使用双向bfs解决超时问题
        if endWord not in wordList:
            return 0

        def diff_count(s1, s2):
            count = 0
            for i, c in enumerate(s1):
                if s2[i] != c:
                    count += 1
            return count

        q1 = [beginWord]
        q2 = [endWord]
        visited = set()
        step = 0
        while q1:
            step += 1
            for _ in range(len(q1)):
                s = q1.pop(0)
                if s in q2:
                    return step

                if s in visited:
                    continue
                visited.add(s)

                for word in wordList:
                    if diff_count(s, word) == 1:
                        q1.append(word)

            if len(q1) > len(q2):
                q1, q2 = q2, q1

        return 0

    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        """365. 水壶问题

        有两个水壶，容量分别为 x 和 y 升。水的供应是无限的。确定是否有可能使用这两个壶准确得到 target 升。

        你可以：
        装满任意一个水壶
        清空任意一个水壶
        将水从一个水壶倒入另一个水壶，直到接水壶已满，或倒水壶已空。


        示例 1:

        输入: x = 3,y = 5,target = 4
        输出: true
        解释：
        按照以下步骤操作，以达到总共 4 升水：
        1. 装满 5 升的水壶(0, 5)。
        2. 把 5 升的水壶倒进 3 升的水壶，留下 2 升(3, 2)。
        3. 倒空 3 升的水壶(0, 2)。
        4. 把 2 升水从 5 升的水壶转移到 3 升的水壶(2, 0)。
        5. 再次加满 5 升的水壶(2, 5)。
        6. 从 5 升的水壶向 3 升的水壶倒水直到 3 升的水壶倒满。5 升的水壶里留下了 4 升水(3, 4)。
        7. 倒空 3 升的水壶。现在，5 升的水壶里正好有 4 升水(0, 4)。
        参考：来自著名的 "Die Hard"
        示例 2:

        输入: x = 2, y = 6, target = 5
        输出: false
        示例 3:

        输入: x = 1, y = 2, target = 3
        输出: true
        """
        # 每轮有6个选择：
        # 1. 装满x；2. 清空x；3. 装满y; 4. 清空y; 5. x 倒进 y; 6. y 倒进 x
        # 避免重复

        visited = set()
        q = [(0, 0)]
        while q:
            for _ in range(len(q)):
                i, j = q.pop(0)
                if i + j == target:
                    return True

                if f"{i}:{j}" in visited:
                    continue
                visited.add(f"{i}:{j}")

                # 装满x
                if i < x:
                    q.append((x, j))
                # 清空x
                if i > 0:
                    q.append((0, j))
                # 装满y
                if j < y:
                    q.append((i, y))
                # 清空y
                if j > 0:
                    q.append((i, 0))
                # x倒入y
                if i > 0 and j < y:
                    if y - j >= i:
                        q.append((0, j + i))
                    else:
                        q.append((i - (y - j), y))
                # y倒入x
                if j > 0 and i < x:
                    if x - i >= j:
                        q.append((i + j, 0))
                    else:
                        q.append((x, j - (x - i)))

        return False


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:
    """919. 完全二叉树插入器
    完全二叉树 是每一层（除最后一层外）都是完全填充（即，节点数达到最大）的，并且所有的节点都尽可能地集中在左侧。

    设计一种算法，将一个新节点插入到一棵完全二叉树中，并在插入后保持其完整。

    实现 CBTInserter 类:

    CBTInserter(TreeNode root) 使用头节点为 root 的给定树初始化该数据结构；
    CBTInserter.insert(int v)  向树中插入一个值为 Node.val == val的新节点 TreeNode。使树保持完全二叉树的状态，并返回插入节点 TreeNode 的父节点的值；
    CBTInserter.get_root() 将返回树的头节点。
    """

    def __init__(self, root: TreeNode):
        self.root = root

    def insert(self, val: int) -> int:
        q = [self.root]
        # bfs遍历，找到第一个左或有节点为空的节点，将该值加入其中
        while q:
            node = q.pop(0)
            if not node.left:
                node.left = TreeNode(val)
                return node.val
            if not node.right:
                node.right = TreeNode(val)
                return node.val

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return -1

    def get_root(self) -> TreeNode:
        return self.root


if __name__ == "__main__":
    assert Solution().slidingPuzzle([[1, 2, 3], [4, 0, 5]]) == 1
    assert Solution().slidingPuzzle([[1, 2, 3], [5, 4, 0]]) == -1
    assert Solution().slidingPuzzle([[4, 1, 2], [5, 0, 3]]) == 5
    assert Solution().slidingPuzzle([[3, 2, 4], [1, 5, 0]]) == 14
    assert Solution().openLock(["0201", "0101", "0102", "1212", "2002"], "0202") == 6
    assert Solution().openLock(["8888"], "0009") == 1
    assert (
        Solution().openLock(
            ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888"
        )
        == -1
    )
    assert Solution().openLock(["0000"], "8888") == -1
    assert Solution().openLock2(["0201", "0101", "0102", "1212", "2002"], "0202") == 6
    assert Solution().openLock2(["8888"], "0009") == 1
    assert (
        Solution().openLock(
            ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888"
        )
        == -1
    )
    assert Solution().openLock2(["0000"], "8888") == -1

    cBTInserter = CBTInserter(TreeNode(1, left=TreeNode(2)))
    assert cBTInserter.insert(3) == 1
    assert cBTInserter.insert(4) == 2
    root = cBTInserter.get_root()
    assert root.val == 1
    assert root.left.val == 2
    assert root.right.val == 3
    assert root.left.left.val == 4

    assert Solution().canVisitAllRooms([[1], [2], [3], []])
    assert not Solution().canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]])

    assert Solution().minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]) == 1
    assert (
        Solution().minMutation(
            "AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
        )
        == 2
    )
    assert (
        Solution().minMutation(
            "AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
        )
        == 3
    )
    assert (
        Solution().minMutation(
            "AACCTTGG", "AATTCCGG", ["AATTCCGG", "AACCTGGG", "AACCCCGG", "AACCTACC"]
        )
        == -1
    )
    assert (
        Solution().minMutation(
            "AACCGGTT", "AAACGGTA", ["AACCGATT", "AACCGATA", "AAACGATA", "AAACGGTA"]
        )
        == 4
    )
    assert (
        Solution().nearestExit(
            [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], [1, 2]
        )
        == 1
    )
    assert (
        Solution().nearestExit(
            [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], [1, 0]
        )
        == 2
    )
    assert Solution().nearestExit([[".", "+"]], [0, 0]) == -1

    assert Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert Solution().orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert Solution().orangesRotting([[0, 2]]) == 0

    assert (
        Solution().ladderLength(
            beginWord="hit",
            endWord="cog",
            wordList=["hot", "dot", "dog", "lot", "log", "cog"],
        )
        == 5
    )
    assert (
        Solution().ladderLength(
            beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log"]
        )
        == 0
    )
    assert Solution().canMeasureWater(3, 5, 4)
    assert not Solution().canMeasureWater(2, 6, 5)
    assert Solution().canMeasureWater(1, 2, 3)
    print("OK")
