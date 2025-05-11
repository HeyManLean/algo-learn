# coding=utf-8
"""
冒泡排序
"""


def bubblesort(arr: list):
    """冒泡排序
    1. 遍历数组, 对比当前和下一个元素, 将最大的逐步移到最后
    2. 忽略已排序的最大值, 重新遍历前面元素
    """
    n = len(arr)

    while n > 1:
        cur = 0
        is_sorted = True  # 优化: 一旦排序好, 就直接退出

        for i in range(1, n):
            if arr[i] < arr[cur]:
                arr[cur], arr[i] = arr[i], arr[cur]
                is_sorted = False

            cur += 1

        n -= 1
        if is_sorted:
            break

    return arr
