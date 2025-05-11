# coding=utf-8


class Solution:
    def permute(self, nums: list) -> list:
        """Permutations (medium)

        ```js
        全排列
        给定一个 没有重复 数字的序列，返回其所有可能的全排列。

        示例:

        输入: [1,2,3]
        输出:
        [
            [1,2,3],
            [1,3,2],
            [2,1,3],
            [2,3,1],
            [3,1,2],
            [3,2,1]
        ]
        ```
        """
        res = []
        n = len(nums)

        def backtrack(first=0):
            if first == n:
                res.append(nums[:])

            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        backtrack()
        return res


class Solution2:
    def permuteUnique2(self, nums: list) -> list:
        """全排列 II
        给定一个可包含重复数字的序列，返回所有不重复的全排列。

        示例:

        输入: [1,1,2]
        输出:
        [
            [1,1,2],
            [1,2,1],
            [2,1,1]
        ]
        """
        nums.sort()

        res = []
        n = len(nums)
        check = [0 for _ in range(n)]

        def backtrack(sol):
            if len(sol) == n:
                res.append(sol)
            
            for i in range(n):
                if check[i] == 1:
                    continue

                if i > 0 and nums[i] == nums[i - 1] and check[i - 1] == 0:
                    continue

                check[i] = 1
                backtrack(sol + nums[i])
                check[i] = 0

        backtrack([])
        return res
