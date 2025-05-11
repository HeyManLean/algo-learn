# coding=utf-8


def merge_intervals(intervals: list) -> list:
    """Merge Intervals (medium)

    ```js
    合并区间
    给出一个区间的集合，请合并所有重叠的区间。

    示例 1:

    输入: [[1,3],[2,6],[8,10],[15,18]]
    输出: [[1,6],[8,10],[15,18]]
    解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
    示例 2:

    输入: [[1,4],[4,5]]
    输出: [[1,5]]
    解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
    ```
    """
    if not intervals:
        return []

    intervals.sort(key=lambda item: item[0])

    res = []
    n = len(intervals)
    temp_interval = intervals[0]

    for i in range(1, n):
        cur_interval = intervals[i]

        if cur_interval[0] <= temp_interval[1]:
            if cur_interval[1] >= temp_interval[1]:
                temp_interval[1] = cur_interval[1]
        else:
            res.append(temp_interval)
            temp_interval = cur_interval

    res.append(temp_interval)

    return res
