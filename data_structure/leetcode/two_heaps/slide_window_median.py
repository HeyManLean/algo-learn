# coding=utf-8
import heapq


class Solution:
    def medianSlidingWindow(self, nums: list, k: int) -> list:
        """Sliding Window Median (hard)

        ```js
        滑动窗口中位数
        中位数是有序序列最中间的那个数。如果序列的大小是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。

        例如：

        [2,3,4]，中位数是 3
        [2,3]，中位数是 (2 + 3) / 2 = 2.5
        给你一个数组 nums，有一个大小为 k 的窗口从最左端滑动到最右端。窗口中有 k 个数，每次窗口向右移动 1 位。你的任务是找出每次窗口移动后得到的新窗口中元素的中位数，并输出由它们组成的数组。



        示例：

        给出 nums = [1,3,-1,-3,5,3,6,7]，以及 k = 3。

        窗口位置                      中位数
        ---------------               -----
        [1  3  -1] -3  5  3  6  7       1
        1 [3  -1  -3] 5  3  6  7      -1
        1  3 [-1  -3  5] 3  6  7      -1
        1  3  -1 [-3  5  3] 6  7       3
        1  3  -1  -3 [5  3  6] 7       5
        1  3  -1  -3  5 [3  6  7]      6
        因此，返回该滑动窗口的中位数数组 [1,-1,-1,3,5,6]。



        提示：

        你可以假设 k 始终有效，即：k 始终小于输入的非空数组的元素个数。
        与真实值误差在 10 ^ -5 以内的答案将被视作正确答案。
        ```
        """
        if not (nums and k):
            return []

        small = []  # 存放较小一半元素, 大根堆, 最大值在顶部, python heapq (默认是小根堆) 需要 * -1
        for i in range(k):
            heapq.heappush(small, -nums[i])

        big = []  # 存放较大一半元素, 小根堆, 最小值在顶部
        for _ in range(k // 2):
            heapq.heappush(big, -heapq.heappop(small))

        # small 比 big 最多多于1个元素

        medians = []
        is_even = k % 2 == 0
        i = k
        n = len(nums)
        remove_table = {}

        while True:
            if is_even:
                median = (-small[0] + big[0]) * 0.5
            else:
                median = -small[0]
            medians.append(median)

            if i >= n:
                break

            balance = 0  # small 相对于 big 是增加还是减少

            out_num = nums[i - k]
            remove_table[out_num] = remove_table.get(out_num, 0) + 1
            if out_num <= -small[0]:
                balance -= 1
            else:
                balance += 1

            in_num = nums[i]
            i += 1
            if in_num <= -small[0]:
                heapq.heappush(small, -in_num)
                balance += 1
            else:
                heapq.heappush(big, in_num)
                balance -= 1

            if balance < 0:
                heapq.heappush(small, -heapq.heappop(big))
                balance += 1
            
            if balance > 0:
                heapq.heappush(big, -heapq.heappop(small))
                balance -= 1

            while remove_table.get(-small[0]):
                remove_table[-small[0]] -= 1
                heapq.heappop(small)

            while big and remove_table.get(big[0]):
                remove_table[big[0]] -= 1
                heapq.heappop(big)

        return medians


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 4
    Solution().medianSlidingWindow(nums, k)
