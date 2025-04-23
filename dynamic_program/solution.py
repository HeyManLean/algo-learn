# -*- coding: utf-8 -*-
"""

解决穷举求最值的问题

动态规划是数学归纳法，假设前面n-1个数已经得到答案，基于这些答案算出第 n 个数
维护 dp 数组，dp[i] 表示第 i 位的状态，可以提供给后面使用

"""


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """322. 零钱兑换
        给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
        计算并返回可以凑成总金额所需的 最少的硬币个数 。

        输入：coins = [1, 2, 5], amount = 11
        输出：3
        """
        memo = [-2] * (amount + 1)

        def dp(coins, amount):
            # 终止条件
            if amount < 0:
                return -1
            if amount == 0:
                return 0

            # 备忘录避免重复子问题
            if memo[amount] != -2:
                return memo[amount]

            res = float("inf")
            # 选择项
            for coin in coins:
                # 独立子结构
                sub_count = dp(coins, amount - coin)
                if sub_count == -1:
                    continue
                res = min(1 + sub_count, res)

            memo[amount] = res if res != float("inf") else -1
            return memo[amount]

        return dp(coins, amount)

    def lengthOfLIS(self, nums: list[int]) -> int:
        """300. 最长递增子序列
        给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
        子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。

        输入：nums = [10,9,2,5,3,7,101,18]
        输出：4
        解释：最长递增子序列是 [2,3,7,101]，因此长度为 4

        输入：nums = [0,1,0,3,2,3]
        输出：4

        输入：nums = [7,7,7,7,7,7,7]
        输出：1
        """
        # 1. dp 每个元素代表一个状态，需要找到状态是什么
        # 状态：dp[i] 为包含 nums[i] 的最长严格递增子序列
        # 2. 找到子问题，算出当前问题值

        dp = [1] * len(nums)
        for i, num in enumerate(nums):
            for j in range(i):
                if num > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)

    def bi_length_of_lis(self, nums):
        top = [0] * len(nums)
        # 牌堆数初始化为 0
        piles = 0
        # 要处理的扑克牌
        for poker in nums:
            # 搜索左侧边界的二分查找
            left, right = 0, piles
            while left < right:
                mid = left + (right - left) // 2
                if top[mid] > poker:
                    right = mid
                elif top[mid] < poker:
                    left = mid + 1
                else:
                    right = mid

            # 没找到合适的牌堆，新建一堆
            if left == piles:
                piles += 1
            # 把这张牌放到牌堆顶
            top[left] = poker
        # 牌堆数就是 LIS 长度
        return piles

    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        """354. 俄罗斯套娃信封问题
        给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。
        当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
        请计算 最多能有多少个 信封能组成一组 "俄罗斯套娃" 信封。

        注意：不允许旋转信封。

        输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
        输出：3
        解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。

        输入：envelopes = [[1,1],[1,1],[1,1]]
        输出：1
        """
        # 先排序
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        piles = 0
        top = [0] * len(envelopes)
        for env in envelopes:
            left, right = 0, piles
            while left < right:
                mid = left + (right - left) // 2
                if env[1] < top[mid]:
                    right = mid
                elif env[1] > top[mid]:
                    left = mid + 1
                else:
                    right = mid

            if left == piles:
                piles += 1
            top[left] = env[1]
        return piles

    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        """931. 下降路径最小和

        给你一个 n x n 的 方形 整数数组 matrix ，请你找出并返回通过 matrix 的下降路径 的 最小和 。

        下降路径 可以从第一行中的任何元素开始，并从每一行中选择一个元素。
        在下一行选择的元素和当前行所选元素最多相隔一列（即位于正下方或者沿对角线向左或者向右的第一个元素）。
        具体来说，位置 (row, col) 的下一个元素应当是 (row + 1, col - 1)、(row + 1, col) 或者 (row + 1, col + 1) 。

        输入：matrix = [[2,1,3],[6,5,4],[7,8,9]]
        输出：13

        输入：matrix = [[-19,57],[-40,-5]]
        输出：-59
        """
        # 最后一行每个元素的最小和，为上一行左右中元素的最小和加上自己
        # dp 二维数组，dp[i][j] 指包含 i,j 元素的最小和
        # 第一行最小和是元素本身
        # base case, 遍历最后一行结束
        m = len(matrix)
        n = len(matrix[0])

        dp = [[float("inf") for _ in range(n)] for _ in range(m)]
        for col, num in enumerate(matrix[0]):
            dp[0][col] = num

        for row in range(1, m):
            for col in range(n):
                dp[row][col] = min(dp[row][col], matrix[row][col] + dp[row - 1][col])
                if col > 0:
                    dp[row][col] = min(
                        dp[row][col], matrix[row][col] + dp[row - 1][col - 1]
                    )
                if col < n - 1:
                    dp[row][col] = min(
                        dp[row][col], matrix[row][col] + dp[row - 1][col + 1]
                    )

        # 最后一行的最小值就是结果
        return min(dp[-1])

    def minDistance(self, word1: str, word2: str) -> int:
        """72. 编辑距离

        给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。
        你可以对一个单词进行如下三种操作：
        插入一个字符
        删除一个字符
        替换一个字符

        输入：word1 = "horse", word2 = "ros"
        输出：3
        解释：
        horse -> rorse (将 'h' 替换为 'r')
        rorse -> rose (删除 'r')
        rose -> ros (删除 'e')
        示例 2：

        输入：word1 = "intention", word2 = "execution"
        输出：5
        """
        # 状态转换方程，n 的结果由 n-1 n-2 得出

        # 优化
        # 站在 word1 的角度，要不要跟 word2 字符匹配，或者选择 word2 的哪个操作跟 word2 匹配
        memo = {}

        def dp(word1, i, word2, j) -> int:
            if j >= len(word2):
                return len(word1[i:])
            if i >= len(word1):
                return len(word2[j:])

            if (i, j) in memo:
                return memo[(i, j)]

            # 字符相同，什么都不做是最小操作
            if word1[i] == word2[j]:
                res = dp(word1, i + 1, word2, j + 1)
            else:
                res = min(
                    # 删除
                    1 + dp(word1, i + 1, word2, j),
                    # 替换
                    1 + dp(word1, i + 1, word2, j + 1),
                    # 新增
                    1 + dp(word1, i, word2, j + 1),
                )
            memo[(i, j)] = res
            return res

        return dp(word1, 0, word2, 0)

    def numDistinct(self, s: str, t: str) -> int:
        """115. 不同的子序列
        给你两个字符串 s 和 t ，统计并返回在 s 的 子序列 中 t 出现的个数。

        测试用例保证结果在 32 位有符号整数范围内。

        输入：s = "rabbbit", t = "rabbit"
        输出：3 (前两个bb, 后两个bb，第一和第三个bb)

        输入：s = "babgbag", t = "bag"
        输出：5
        """
        memo = {}

        def dp(s, i, t, j) -> int:
            # base case: t 匹配完成
            if j == len(t):
                return 1
            # base case: s < t
            if len(s[i:]) < len(t[j:]):
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            # 如果字符相等，则考虑匹配或不匹配该字符
            if s[i] == t[j]:
                # 匹配 + 不匹配该字符
                res = dp(s, i + 1, t, j + 1) + dp(s, i + 1, t, j)
            else:
                # 跳过该字符（不匹配）
                res = dp(s, i + 1, t, j)

            memo[(i, j)] = res
            return res

        return dp(s, 0, t, 0)

    def maxSubArray(self, nums: list[int]) -> int:
        """53. 最大子数组和
        给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
        子数组是数组中的一个连续部分。

        输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
        输出：6
        解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

        输入：nums = [1]
        输出：1

        输入：nums = [5,4,-1,7,8]
        输出：23
        """
        # 连续
        # dp[i] 表示包含 nums[i] 的最大和连续数组
        # dp[i] 的选择，与 nums[i - 1] 连接，或不与 nums[i - 1] 连接

        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            if dp[i - 1] > 0:
                dp[i] = nums[i] + dp[i - 1]
            else:
                dp[i] = nums[i]

        return max(dp)

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """1143. 最长公共子序列
        给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。
        如果不存在 公共子序列 ，返回 0 。

        一个字符串的 子序列 是指这样一个新的字符串：
        它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

        例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
        两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

        输入：text1 = "abcde", text2 = "ace"
        输出：3
        解释：最长公共子序列是 "ace" ，它的长度为 3 。

        输入：text1 = "abc", text2 = "abc"
        输出：3
        输入：text1 = "abc", text2 = "def"
        输出：0
        """
        # 维护二维数组
        # dp[i][j] 表示子问题：text1[:i] 和 text2[:j] 的最长公共子序列

        # 如果 text[i] = text2[j]，那么
        #   dp[i][j] 等于 1 + dp[i-1][j-1]
        # 否则
        #   dp[i][j] 等于 dp[i][j - 1]、dp[i - 1][j] 的子序列最大值
        # basecase， i=0,j=0，如果相等则为1，否则为0

        # 从0开始，0,0代表没有字符
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(
                        dp[i][j - 1],
                        dp[i - 1][j],
                    )
        return dp[m][n]

    def longestCommonSubsequence_Reverse(self, text1: str, text2: str) -> int:
        """递归函数版本"""
        memo = [[-1 for _ in text2] for _ in text1]

        def dp(text1, i, text2, j):
            if i < 0 or j < 0:
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            if text1[i] == text2[j]:
                memo[i][j] = 1 + dp(text1, i - 1, text2, j - 1)
            else:
                memo[i][j] = max(
                    dp(text1, i, text2, j - 1),
                    dp(text1, i - 1, text2, j),
                )
            return memo[i][j]

        return dp(text1, len(text1) - 1, text2, len(text2) - 1)

    def minDistance2(self, word1: str, word2: str) -> int:
        """583. 两个字符串的删除操作

        给定两个单词 word1 和 word2 ，返回使得 word1 和  word2 相同所需的最小步数。
        每步 可以删除任意一个字符串中的一个字符。

        输入: word1 = "sea", word2 = "eat"
        输出: 2
        解释: 第一步将 "sea" 变为 "ea" ，第二步将 "eat "变为 "ea"

        输入：word1 = "leetcode", word2 = "etco"
        输出：4
        """
        # 穷举+最值：动态规划

        # 当 word1[i] == word2[j] 时，则不需要删除，继续处理 word1[i+1:] 和 word2[j+1:]
        # 即使遇到当前字符，删除一下也是+1，跟删除当前一样，则不需要重复处理
        # 否则删除word1[i] 或删除 word2[j]，继续穷举
        memo = {}

        def dp(word1, i, word2, j):
            # 到达最后一个字符后，删除另一个word的剩余字符
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i

            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                # 相同则跳过，继续处理剩余部分
                res = dp(word1, i + 1, word2, j + 1)
            else:
                # 选其中一个word删除字符，继续处理，取两者最小值
                res = 1 + min(dp(word1, i + 1, word2, j), dp(word1, i, word2, j + 1))
            memo[(i, j)] = res
            return memo[(i, j)]

        return dp(word1, 0, word2, 0)

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """712. 两个字符串的最小ASCII删除和
        给定两个字符串s1 和 s2，返回 使两个字符串相等所需删除字符的 ASCII 值的最小和 。

        输入: s1 = "sea", s2 = "eat"
        输出: 231
        解释: 在 "sea" 中删除 "s" 并将 "s" 的值(115)加入总和。
        在 "eat" 中删除 "t" 并将 116 加入总和。
        结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。

        输入: s1 = "delete", s2 = "leet"
        输出: 403
        """
        memo = {}

        def dp(word1, i, word2, j):
            # 到达最后一个字符后，删除另一个word的剩余字符
            if i == len(word1):
                return sum(ord(c) for c in word2[j:])
            if j == len(word2):
                return sum(ord(c) for c in word1[i:])

            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                # 相同则跳过，继续处理剩余部分
                res = dp(word1, i + 1, word2, j + 1)
            else:
                # 选其中一个word删除字符，继续处理，取两者最小值
                res = min(
                    ord(word1[i]) + dp(word1, i + 1, word2, j),
                    ord(word2[j]) + dp(word1, i, word2, j + 1),
                )
            memo[(i, j)] = res
            return memo[(i, j)]

        return dp(s1, 0, s2, 0)

    def knapsack(self, W: int, N: int, wt: list[int], val: list[int]) -> int:
        """0-1背包问题
        给你一个可装载重量为 W 的背包和 N 个物品，每个物品有重量和价值两个属性。
        其中第 i 个物品的重量为 wt[i]，价值为 val[i]。
        现在让你用这个背包装物品，每个物品只能用一次，
        在不超过背包容量的前提下，最多能装的价值是多少？
        """
        # 如果 wt[i] 和 val[i] 都不超过 W 和 N，则考虑将该物品加入或不加入，计算后面的最大价值并返回
        # 状态，随着子问题规模而变化的变量，背包重量、背包价值、物品数量
        # 选择：放进背包或不放进去
        # 限制：重量和数量不超过背包最大值

        dp = [[0] * (N + 1) for _ in range(W + 1)]

        for w in range(1, W + 1):
            for i in range(1, N + 1):
                # 超过重量，则跳过
                if w - wt[i - 1] < 0:
                    dp[w][i] = dp[w][i - 1]
                else:
                    dp[w][i] = max(dp[w][i - 1], val[i - 1] + dp[w - wt[i - 1]][i - 1])

        return dp[W][N]

        # def dp(w, n, i):
        #     if w < 0 or n < 0:
        #         return 0

        #     if i >= n:
        #         return 0

        #     if w >= wt[i] and n >= 1:
        #         res = max(val[i] + dp(w - wt[i], n - 1, i + 1), dp(w, n, i + 1))
        #     else:
        #         res = dp(w, n, i + 1)

        #     return res

        # return dp(W, N, 0)

    def canPartition(self, nums: list[int]) -> bool:
        """416. 分割等和子集
        给你一个 只包含正整数 的 非空 数组 nums 。
        请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

        输入：nums = [1,5,11,5]
        输出：true
        解释：数组可以分割成 [1, 5, 5] 和 [11] 。

        输入：nums = [1,2,3,5]
        输出：false
        解释：数组不能分割成两个元素和相等的子集。
        """
        # 穷举问题可以使用动态规划提高性能

        # 两个数组一样，则变成背包问题，最大数目是 nums 数量，最大重量是 sum(nums) // 2
        if sum(nums) % 2 != 0:
            return False

        N = len(nums)
        W = sum(nums) // 2
        dp = [[False] * (W + 1) for _ in range(N + 1)]
        dp[0][0] = True

        for i in range(1, N + 1):
            for w in range(1, W + 1):
                # 选择是否加入背包

                # 不加入
                if w - nums[i - 1] < 0:
                    dp[i][w] = dp[i - 1][w]
                else:
                    # 加入或不加入其中一个成立即可
                    dp[i][w] = dp[i - 1][w] or dp[i - 1][w - nums[i - 1]]

        return dp[N][W]

    def change(self, amount: int, coins: list[int]) -> int:
        """518. 零钱兑换 II

        给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。
        请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。
        假设每一种面额的硬币有无限个。

        输入：amount = 5, coins = [1, 2, 5]
        输出：4
        解释：有四种方式可以凑成总金额：
        5=5
        5=2+2+1
        5=2+1+1+1
        5=1+1+1+1+1
        示例 2：

        输入：amount = 3, coins = [2]
        输出：0

        输入：amount = 10, coins = [10]
        输出：1
        """
        # 状态：总金额
        # 选择：选择该coin，或不选择该coin，算出组合数

        # 每个金额的组合数
        n = len(coins)
        dp = [
            [0] * (amount + 1)
            for _ in range(n + 1)
        ]
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for w in range(1, amount + 1):
                # 不选择
                if w - coins[i - 1] < 0:
                    dp[i][w] = dp[i - 1][w]
                else:
                    dp[i][w] = dp[i - 1][w] + dp[i][w - coins[i - 1]]

        return dp[n][amount]



if __name__ == "__main__":
    assert Solution().coinChange([1, 2, 5], 11) == 3
    assert Solution().coinChange([2], 3) == -1
    assert Solution().coinChange([1], 0) == 0
    assert Solution().coinChange([186, 419, 83, 408], 6249) == 20

    assert Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
    assert Solution().lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1
    assert Solution().lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6

    assert Solution().maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]) == 3
    assert Solution().maxEnvelopes([[1, 1], [1, 1], [1, 1]]) == 1
    assert (
        Solution().maxEnvelopes(
            [
                [1, 15],
                [7, 18],
                [7, 6],
                [7, 100],
                [2, 200],
                [17, 30],
                [17, 45],
                [3, 5],
                [7, 8],
                [3, 6],
                [3, 10],
                [7, 20],
                [17, 3],
                [17, 45],
            ]
        )
        == 3
    )

    assert Solution().minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]) == 13
    assert Solution().minFallingPathSum([[-19, 57], [-40, -5]]) == -59

    assert Solution().minDistance("horse", "ros") == 3
    assert Solution().minDistance("intention", "execution") == 5
    assert Solution().minDistance("", "a") == 1

    assert Solution().numDistinct("rabbbit", "rabbit") == 3
    assert Solution().numDistinct("babgbag", "bag") == 5

    assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert Solution().maxSubArray([1]) == 1
    assert Solution().maxSubArray([5, 4, -1, 7, 8]) == 23

    assert Solution().longestCommonSubsequence("abcde", "ace") == 3
    assert Solution().longestCommonSubsequence("abc", "abc") == 3
    assert Solution().longestCommonSubsequence("abc", "def") == 0

    assert Solution().minimumDeleteSum("sea", "eat") == 231
    assert Solution().minimumDeleteSum("delete", "leet") == 403

    assert Solution().knapsack(N=3, W=4, wt=[2, 1, 3], val=[4, 2, 3]) == 6

    assert Solution().canPartition([1, 5, 11, 5])
    assert not Solution().canPartition([1, 2, 3, 5])
    assert Solution().change(5, [1, 2, 5]) == 4
    assert Solution().change(3, [2]) == 0
    assert Solution().change(10, [10]) == 1

    print("OK")
