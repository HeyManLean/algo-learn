# coding=utf-8

import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):
            heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -num))
        else:
            heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num))

    def findMedian(self) -> float:
        """Find the Median of a Number Stream (hard)

        ```js
        数据流的中位数
        中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

        例如，

        [2,3,4] 的中位数是 3

        [2,3] 的中位数是 (2 + 3) / 2 = 2.5

        设计一个支持以下两种操作的数据结构：

        void addNum(int num) - 从数据流中添加一个整数到数据结构中。
        double findMedian() - 返回目前所有元素的中位数。
        示例：

        addNum(1)
        addNum(2)
        findMedian() -> 1.5
        addNum(3) 
        findMedian() -> 2
        进阶:

        如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
        如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
        ```
        """
        n = len(self.max_heap) + len(self.min_heap)
        if n % 2 == 0:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return self.min_heap[0]


if __name__ == "__main__":
    heap = []
    finder = MedianFinder()
    for i in range(15):
        finder.addNum(i)
        heapq.heappush(heap, -i)

        print(finder.heap)
        print(list(map(abs, heap)))

    finder.addNum(0)
    heapq.heappush(heap, 0)

    print(finder.heap)
    print(list(map(abs, heap)))