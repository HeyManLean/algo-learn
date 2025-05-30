# coding=utf-8


def interval_intersection(A: list, B: list) -> list:
    """Intervals Intersection (medium)

    ```js
    区间列表的交集
    给定两个由一些 闭区间 组成的列表，每个区间列表都是成对不相交的，并且已经排序。

    返回这两个区间列表的交集。

    （形式上，闭区间 [a, b]（其中 a <= b）表示实数 x 的集合，而 a <= x <= b。两个闭区间的交集是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3]。）

    

    示例：



    输入：A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
    输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    

    提示：

    0 <= A.length < 1000
    0 <= B.length < 1000
    0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
    ```
    """
    i = j = 0
    n = len(A)
    m = len(B)
    res = []

    while i < n and j < m:
        a_interval = A[i]
        b_interval = B[j]

        if a_interval[1] < b_interval[1]:
            i += 1
        elif a_interval[1] > b_interval[1]:
            j += 1
        else:
            i += 1
            j += 1

        if a_interval[1] < b_interval[0] or b_interval[1] < a_interval[0]:
            continue

        start = max(a_interval[0], b_interval[0])
        end = min(a_interval[1], b_interval[1])
        res.append([start, end])

    return res
