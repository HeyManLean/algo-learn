# -*- coding: utf-8 -*-


# 单调队列，找出某个区域的最值，队列是单调递减的
class MonotonicQueue:
    def __init__(self):
        self.queue = []

    # 在队尾添加元素 n
    def push(self, n: int):
        # 将尾部小于n的数值移除
        while self.queue and n > self.queue[-1]:
            self.queue.pop()

        self.queue.append(n)

    # 返回当前队列中的最大值
    def max(self) -> int:
        return self.queue[0]

    # 队头元素如果是 n，删除它
    def pop(self, n: int):
        if self.queue[0] == n:
            self.queue.pop(0)


class Solution(object):

    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # 找出按k为size的每个滑动窗口的最大值
        res = []

        i = 0
        n = len(nums)
        mq = MonotonicQueue()

        while i < n:
            # 先让队列达到k个数
            if i < k - 1:
                mq.push(nums[i])
            else:
                mq.push(nums[i])
                res.append(mq.max())
                mq.pop(nums[i - k + 1])  # 移除左边的值

            i += 1

        return res


assert Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]