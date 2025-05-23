# coding=utf-8


def insert_intervals(intervals: list, newInterval: list):
    """ Insert Interval (hard)

    ```js
    插入区间
    给出一个无重叠的 ，按照区间起始端点排序的区间列表。

    在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。



    示例 1：

    输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
    输出：[[1,5],[6,9]]
    示例 2：

    输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    输出：[[1,2],[3,10],[12,16]]
    解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
    ```
    """
    res = []
    inserted = 0

    for interval in intervals:
        if inserted:
            res.append(interval)
            continue

        if newInterval[1] < interval[0]:
            res.append(newInterval)
            res.append(interval)
            inserted = 1
        else:
            if newInterval[0] <= interval[0]:
                if newInterval[1] <= interval[1]:
                    newInterval[1] = interval[1]
                else:
                    continue
            else:
                if newInterval[1] <= interval[1]:
                    res.append(interval)
                    inserted = 1
                else:
                    if newInterval[0] <= interval[1]:
                        newInterval[0] = interval[0]
                    else:
                        res.append(interval)

    if not inserted:
        res.append(newInterval)

    return res


def insert_intervals_v2(intervals: list, newInterval: list) -> list:
    """贪心算法"""
    new_start, new_end = newInterval
    n = len(intervals)
    i = 0

    res = []

    while i < n and intervals[i][0] < new_start:
        res.append(intervals[i])
        i += 1

    if not res or res[-1][1] < new_start:
        res.append(newInterval)
    else:
        res[-1][1] = max(res[-1][1], new_end)

    while i < n:
        interval = intervals[i]

        if interval[0] > res[-1][1]:
            res.append(interval)
        else:
            res[-1][1] = max(interval[1], res[-1][1])

        i += 1

    return res
