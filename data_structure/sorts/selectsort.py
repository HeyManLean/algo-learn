# coding=utf-8
"""
选择排序
"""


def selectsort(arr: list):
    n = len(arr)

    for i in range(n - 1):
        min_pos = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_pos]:
                min_pos = j

        arr[i], arr[min_pos] = arr[min_pos], arr[i]

    return arr
