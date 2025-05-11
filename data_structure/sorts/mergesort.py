# coding=utf-8
"""
合并排序
"""


def mergesort(arr: list, lo: int = None, hi: int = None):
    lo = lo or 0
    hi = hi if hi is not None else len(arr)

    if hi - lo < 2:
        return

    mi = (lo + hi) // 2

    mergesort(arr, lo, mi)
    mergesort(arr, mi, hi)
    _merge_arrays(arr, lo, mi, hi)

    return arr


def _merge_arrays(arr, lo, mi, hi):
    """合并两个有序数组"""
    larr = [v for v in arr[lo:mi]]

    i = 0
    n = len(larr)

    while i < n and mi < hi:
        if larr[i] <= arr[mi]:
            arr[lo] = larr[i]
            i += 1
        else:
            arr[lo] = arr[mi]
            mi += 1

        lo += 1

    if i < n:
        for j in range(i, n):
            arr[lo] = larr[j]
            lo += 1
