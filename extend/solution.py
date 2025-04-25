# -*- coding: utf-8 -*-


class Solution:
    def minMeetingRooms(self, meetings: list[list[int]]) -> int:
        """253 题「会议室 II」
        给你输入若干形如 [begin, end] 的区间，代表若干会议的开始时间和结束时间，
        请你计算至少需要申请多少间会议室。
        """
        # 类似括号识别一样遍历
        n = len(meetings)
        begin = [0] * n
        end = [0] * n
        for i, m in enumerate(meetings):
            begin[i] = m[0]
            end[i] = m[1]

        begin.sort()
        end.sort()

        i, j = 0, 0
        count = 0
        max_count = 0
        while i < n and j < n:
            if begin[i] < end[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            max_count = max(count, max_count)

        return max_count

    def trap(self, height: list[int]) -> int:
        """42. 接雨水
        给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

        输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
        输出：6

        输入：height = [4,2,0,3,2,5]
        输出：9
        https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/rainwatertrap.png
        """
        # 第i个位置的雨水，等于左边最大柱子和右边最大柱子的最小值 - 第i柱子高度
        n = len(height)
        rain = 0
        l_max = [0] * n
        l_max[0] = height[0]
        r_max = [0] * n
        r_max[n - 1] = height[-1]

        for i, h in enumerate(height):
            l_max[i] = max(h, l_max[i - 1])

        for i in range(n - 2, -1, -1):
            r_max[i] = max(height[i], r_max[i + 1])

        for i in range(1, n - 1):
            rain += min(l_max[i], r_max[i]) - height[i]

        return rain

    def maxArea(self, height: list[int]) -> int:
        """11. 盛最多水的容器
        给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
        找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
        返回容器可以储存的最大水量。

        输入：[1,8,6,2,5,4,8,3,7]
        输出：49

        输入：height = [1,1]
        输出：1
        """
        # 左右双指针，分别向中间靠拢
        # 选择，左前进、右后退，比较大小再做出选择
        # 直到重合
        n = len(height)
        left, right = 0, n - 1
        res = 0

        while left < right:
            res = max(res, min(height[right], height[left]) * (right - left))

            # 收缩较小的边
            # 因为如果移动最大的边，高还是最小边决定的，宽度在缩小，则面积永远比当前小
            # 只有收缩最小的边，才可能找到比当前面积更大的值
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res

    def isUgly(self, n: int) -> bool:
        """263. 丑数
        丑数 就是只包含质因数 2、3 和 5 的 正 整数。

        给你一个整数 n ，请你判断 n 是否为 丑数 。如果是，返回 true ；否则，返回 false 。

        输入：n = 6
        输出：true
        解释：6 = 2 × 3
        示例 2：

        输入：n = 1
        输出：true
        解释：1 没有质因数。
        """
        if n <= 0:
            return False
        while n % 2 == 0:
            n //= 2
        while n % 3 == 0:
            n //= 3
        while n % 5 == 0:
            n //= 5

        return n == 1

    def nthUglyNumber(self, n: int) -> int:
        """264. 丑数 II
        给你一个整数 n ，请你找出并返回第 n 个 丑数 。
        丑数 就是质因子只包含 2、3 和 5 的正整数。

        输入：n = 10
        输出：12
        解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。

        输入：n = 1
        输出：1
        """
        # 后面的丑数实际是前面丑数分别乘以2、3、5
        # 维护2、3、5 当前相乘的位置，每次相乘后比较最小值加入队列中，并将最小值的索引加1， 并按顺序取值
        index2 = 0
        index3 = 0
        index5 = 0

        ugly = [1]

        while len(ugly) < n:
            ugly2 = ugly[index2] * 2
            ugly3 = ugly[index3] * 3
            ugly5 = ugly[index5] * 5
            min_ugly = min(ugly2, ugly3, ugly5)
            ugly.append(min_ugly)

            # 相等则递增，避免重复字符
            if ugly2 == min_ugly:
                index2 += 1
            if ugly3 == min_ugly:
                index3 += 1
            if ugly5 == min_ugly:
                index5 += 1

        return ugly[n - 1]

    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        """313. 超级丑数
        超级丑数 是一个正整数，并满足其所有质因数都出现在质数数组 primes 中。
        给你一个整数 n 和一个整数数组 primes ，返回第 n 个 超级丑数 。

        输入：n = 12, primes = [2,7,13,19]
        输出：32
        解释：给定长度为 4 的质数数组 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。

        输入：n = 1, primes = [2,3,5]
        输出：1
        """
        # 质数较多，每轮取值会重复计算，实际就是为了去每轮的最小值
        # 使用最小二叉堆维护，每轮的数值，取出最小值后，立马将最小值对应的质数下一个值加入最小堆中
        import heapq

        ugly = [1]

        hq = []
        for prime in primes:
            heapq.heappush(hq, (prime * ugly[0], prime, 0))

        while len(ugly) < n:
            num, prime, i = heapq.heappop(hq)
            if num != ugly[-1]:
                ugly.append(num)

            # 将移除的质数下一个数加入队列中
            heapq.heappush(hq, (prime * ugly[i + 1], prime, i + 1))

        return ugly[n - 1]

    def nthUglyNumber3(self, n: int, a: int, b: int, c: int) -> int:
        # 题目说本题结果在 [1, 2 * 10^9] 范围内，
        # 所以就按照这个范围初始化两端都闭的搜索区间
        left, right = 1, int(2e9)
        # 搜索左侧边界的二分搜索
        while left <= right:
            mid = left + (right - left) // 2
            if self.f(mid, a, b, c) < n:
                # [1..mid] 中符合条件的元素个数不足 n，所以目标在右半边
                left = mid + 1
            else:
                # [1..mid] 中符合条件的元素个数大于 n，所以目标在左半边
                right = mid - 1
        return left

    # 计算最大公因数（辗转相除/欧几里得算法）
    def gcd(self, a: int, b: int) -> int:
        if a < b:
            # 保证 a > b
            return self.gcd(b, a)
        if b == 0:
            return a
        return self.gcd(b, a % b)

    # 最小公倍数
    def lcm(self, a: int, b: int) -> int:
        # 最小公倍数就是乘积除以最大公因数
        return a * b // self.gcd(a, b)

    # 计算 [1..num] 之间有多少个能够被 a 或 b 或 c 整除的数字
    def f(self, num: int, a: int, b: int, c: int) -> int:
        setA, setB, setC = num // a, num // b, num // c
        setAB = num // self.lcm(a, b)
        setAC = num // self.lcm(a, c)
        setBC = num // self.lcm(b, c)
        setABC = num // self.lcm(self.lcm(a, b), c)
        # 集合论定理：A + B + C - A ∩ B - A ∩ C - B ∩ C + A ∩ B ∩ C
        return setA + setB + setC - setAB - setAC - setBC + setABC

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """1. 两数之和
        给定一个整数数组 nums 和一个整数目标值 target，
        请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

        输入：nums = [2,7,11,15], target = 9
        输出：[0,1]
        """
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []

    def two_sum_list(self, nums: list[int], target: int):
        nums.sort()
        lo, hi = 0, len(nums) - 1
        res = []

        while lo < hi:
            left = nums[lo]
            right = nums[hi]
            tsum = left + right
            if tsum < target:
                while lo < hi and nums[lo] == left:
                    lo += 1
            elif tsum > target:
                while lo < hi and nums[hi] == right:
                    hi -= 1
            else:
                res.append([nums[lo], nums[hi]])
                while lo < hi and nums[lo] == left:
                    lo += 1
                while lo < hi and nums[hi] == right:
                    hi -= 1

        return res

    def threeSum(self, nums: list[int], target=0) -> list[list[int]]:
        """15. 三数之和
        给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]]
        满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。
        请你返回所有和为 0 且不重复的三元组。

        注意：答案中不可以包含重复的三元组。

        输入：nums = [-1,0,1,2,-1,-4]
        输出：[[-1,-1,2],[-1,0,1]]

        输入：nums = [0,1,1]
        输出：[]

        输入：nums = [0,0,0]
        输出：[[0,0,0]]
        """
        nums.sort()
        lo = 0
        res = []

        while lo < len(nums) - 1:
            two_sums = self.two_sum_list(nums[lo + 1:], target - nums[lo])
            for item in two_sums:
                res.append([nums[lo]] + item)

            # 不需要重复
            left = nums[lo]
            while lo < len(nums) - 1 and nums[lo] == left:
                lo += 1

        return res

    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        """18. 四数之和
        给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。
        请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]]
        （若两个四元组元素一一对应，则认为两个四元组重复）：

        0 <= a, b, c, d < n
        a、b、c 和 d 互不相同
        nums[a] + nums[b] + nums[c] + nums[d] == target
        你可以按 任意顺序 返回答案 。

        输入：nums = [1,0,-1,0,-2,2], target = 0
        输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

        输入：nums = [2,2,2,2,2], target = 8
        输出：[[2,2,2,2]]
        """
        nums.sort()
        lo = 0
        res = []

        while lo < len(nums) - 1:
            three_sums = self.threeSum(nums[lo+1:], target - nums[lo])
            for item in three_sums:
                res.append([nums[lo]] + item)

            # 去掉重复数字
            left = nums[lo]
            while lo < len(nums) - 1 and nums[lo] == left:
                lo += 1

        return res



import random


class PickSolution:
    """528. 按权重随机选择
    给你一个 下标从 0 开始 的正整数数组 w ，其中 w[i] 代表第 i 个下标的权重。

    请你实现一个函数 pickIndex ，它可以 随机地 从范围 [0, w.length - 1] 内（含 0 和 w.length - 1）
    选出并返回一个下标。选取下标 i 的 概率 为 w[i] / sum(w) 。

    例如，对于 w = [1, 3]，挑选下标 0 的概率为 1 / (1 + 3) = 0.25 （即，25%），而选取下标 1 的概率为 3 / (1 + 3) = 0.75（即，75%）。
    """

    def __init__(self, w: list[int]):
        # 维护前缀和，累加后，随机数，按照二分法查询对应位置返回
        self.pre_sum = [0] * (len(w) + 1)  # pre_sum[i] = pre_sum[i-1] + num[i - 1]
        for i in range(1, len(w) + 1):
            self.pre_sum[i] = self.pre_sum[i - 1] + w[i - 1]

    def pickIndex(self) -> int:
        w = random.randint(1, self.pre_sum[-1])
        return self.binary_search(self.pre_sum, 0, len(self.pre_sum), w)

    def binary_search(self, nums, left, right, w):
        while left < right:
            mid = left + (right - left) // 2
            if w > nums[mid]:
                left = mid + 1
            elif w < nums[mid]:
                right = mid
            elif w == nums[mid]:
                # return mid - 1
                right = mid

        return left - 1  # 前缀和比nums多一位


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


if __name__ == "__main__":
    assert (
        Solution().minMeetingRooms([[0, 10], [5, 8], [4, 7], [11, 20], [12, 29]]) == 3
    )
    assert Solution().minMeetingRooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert Solution().minMeetingRooms([(4, 16), (5, 17), (4, 17), (12, 17)]) == 4

    assert Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert Solution().trap([4, 2, 0, 3, 2, 5]) == 9
    assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert Solution().maxArea([1, 1]) == 1

    assert Solution().isUgly(6)
    assert Solution().isUgly(1)
    assert not Solution().isUgly(14)

    assert Solution().nthUglyNumber(10) == 12
    assert Solution().nthUglyNumber(1) == 1

    assert Solution().nthSuperUglyNumber(12, [2, 7, 13, 19]) == 32
    assert Solution().nthSuperUglyNumber(1, [2, 3, 5]) == 1

    # assert Solution().nthUglyNumber3(3, 2, 3, 5) == 4
    # assert Solution().nthUglyNumber3(4, 2, 3, 4) == 6
    # assert Solution().nthUglyNumber3(5, 2, 11, 13) == 10

    assert Solution().threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert Solution().threeSum([0, 1, 1]) == []
    assert Solution().threeSum([0, 0, 0]) == [[0, 0, 0]]

    assert Solution().fourSum([1, 0, -1, 0, -2, 2], 0) == [
        [-2, -1, 1, 2],
        [-2, 0, 0, 2],
        [-1, 0, 0, 1],
    ]
    assert Solution().fourSum([2, 2, 2, 2, 2], 8) == [[2, 2, 2, 2]]

    print("OK")
