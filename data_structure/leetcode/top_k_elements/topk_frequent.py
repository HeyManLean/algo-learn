# coding=utf-8
import heapq


class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        """Top ‘K’ Frequent Numbers (medium)

        ```js
        前 K 个高频元素
        给定一个非空的整数数组，返回其中出现频率前 k 高的元素。



        示例 1:

        输入: nums = [1,1,1,2,2,3], k = 2
        输出: [1,2]
        示例 2:

        输入: nums = [1], k = 1
        输出: [1]


        提示：

        你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
        你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
        题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
        你可以按任意顺序返回答案。
        ```
        """
        count_map = {}

        max_count = 0

        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
            max_count = max(max_count, count_map[num])

        # 桶排序法
        """
        bucket = [[] for i in range(max_count + 1)]

        for num, count in count_map.items():
            bucket[count].append(num)

        res = []

        while len(res) < k and max_count >= 0:
            if bucket[max_count]:
                res.extend(bucket[max_count])
            
            max_count -= 1

        return res
        """
        # 最小堆
        n = len(count_map)
        i = 0

        heap = []

        for i, (num, cnt) in enumerate(count_map.items()):
            if i < k:
                heapq.heappush(heap, (cnt, num))
            else:
                heapq.heappushpop(heap, (cnt, num))

        return [x[1] for x in heap]


if __name__ == '__main__':
    nums = [5, 3, 1, 1, 1, 3, 73, 1]
    k = 2
    print(Solution().topKFrequent(nums, k))
