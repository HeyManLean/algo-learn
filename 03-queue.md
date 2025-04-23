# 队列&栈

## 1.单调栈

```py

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        # 每次push数值，如果该值比最小值更小或相等，则加入 min_stack，该栈顶维护当前栈中最小值
        # 每次pop，如果跟当前最小值一直，最小栈也要移除

    def push(self, val: int) -> None:
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        


class FreqStack:
    """最大频次栈，每次pop出当前频率最高的那个值，如果频率相同，pop出离栈顶最近那个值"""

    def __init__(self):
        self.max_freq = 0
        self.freq_to_vals = {}
        self.val_to_freq = {}

    def push(self, val: int) -> None:
        freq = self.val_to_freq.get(val, 0) + 1
        self.val_to_freq[val] = freq
        
        # 保留该值旧的freq映射
        self.freq_to_vals.setdefault(freq, []).append(val)
        self.max_freq = max(self.max_freq, freq)

    def pop(self) -> int:
        val = self.freq_to_vals[self.max_freq].pop()
        if not self.freq_to_vals[self.max_freq]:
            self.max_freq -= 1

        self.val_to_freq[val] -= 1
        return val

```

## 2.单调队列 + 滑动窗口

区间+最值问题

对于需要找出区间内最大和最小值的的场景，可以利用单调队列+滑动窗口来解决
- 单调队列：队列第一个数就是该区域的最值
    - 最大值单调队列：向右添加新的数前，将队列里小于该数的值移除（尾部），保留大于等于的数
    - 最小值单调队列：向右添加新的数前，将队列里大于该数的值移除（尾部），保留小于等于的数
    - 移除最左边的数时，如果该数等于队列第一个数，则将队列第一个数移除，否则不需要处理


### 绝对差不超过限制的最长连续子数组（1438）

- https://leetcode.cn/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

```py
class Solution(object):
    def longestSubarray(self, nums, limit):
        """1438. 绝对差不超过限制的最长连续子数组
        给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于 limit 。

        如果不存在满足条件的子数组，则返回 0 。
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        left = right = 0
        queue = MonotonicQueue()
        max_len = 0

        while right < len(nums):
            queue.push(nums[right])
            right += 1
            while queue.max() - queue.min() > limit:
                queue.pop(nums[left])
                left += 1

            max_len = max(max_len, right - left)

        return max_len
```


### 和至少为K的最短子数组（862）

- https://leetcode.cn/problems/shortest-subarray-with-sum-at-least-k/description/

- 前缀和+单调队列+左右指针


```py
class MonotonicQueue:
    """维护区间内的最大值和最小值，单调队列"""
    def __init__(self):
        self.maxq = []
        self.minq = []

    def push(self, n):
        while self.maxq and n > self.maxq[-1]:
            self.maxq.pop()
        self.maxq.append(n)
        while self.minq and n < self.minq[-1]:
            self.minq.pop()
        self.minq.append(n)

    def pop(self, n):
        if self.max() == n:
            self.maxq.pop(0)
        if self.min() == n:
            self.minq.pop(0)

    def max(self):
        return self.maxq[0]

    def min(self):
        return self.minq[0]
    
    def empty(self):
        return not self.minq


# @lc code=start
class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 左右指针滑动+前缀和数组
        # 用右侧前缀和减窗口内最小和是否大于等于K，判断是否可以继续收缩，不需要找到具体位置
        pre_sum = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]  # 前缀和，第i位前缀和是前 i 个数之和，不包含索引i的数值

        left = right = 0
        q = MonotonicQueue()
        min_len = len(nums) + 1

        while right < len(nums):
            q.push(pre_sum[right])

            # 当前窗口，[left, right] 的和，等于 pre_sum[right+1] - pre_sum[left]
            # 如果当前窗口最大的和 pre_sum[right+1] - min >= k 满足要求，则收缩窗口直到不满足
            while right + 1 < len(pre_sum) and not q.empty() and pre_sum[right + 1] - q.min() >= k:
                min_len = min(right - left + 1, min_len)
                q.pop(pre_sum[left])
                left += 1

            right += 1

        return min_len if min_len <= len(nums) else -1
```