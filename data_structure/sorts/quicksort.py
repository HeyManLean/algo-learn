# coding=utf-8
"""
快速排序
- 针对所有数组 (无序和有序)
"""


def quicksort(arr: list, lo: int = None, hi: int = None):
    lo = lo or 0
    hi = hi if hi is not None else len(arr) - 1

    if hi - lo < 1:
        return

    mi = _partition(arr, lo, hi)
    quicksort(arr, lo, mi)
    quicksort(arr, mi + 1, hi)

    return arr


def _partition(arr: list, lo: int, hi: int):
    """
    取值范围： [lo, hi]
        选取 lo 对应元素 m = elem[lo] 作为候选轴点， 最终达到：
            - lo = hi = index(m)
            - 0 < x < index(m), elem[x] <= m, 左边元素都小于 m
            - index(m) < x < elem.size, elem[x] > m， 右边元素都大于 m
        步骤：
            m = elem[lo]， 此时 elem[lo] 腾出， 用于其他元素调整
            进入循环
            - hi-- 向中间靠拢， 直到遇到小于 m 的值（不满足要求）
                - elem[lo] = elem[hi]
            - lo++ 向中间靠拢， 直到遇到大于 m 的值（不满足要求）
                - elem[hi] = elem[lo]， 那么lo 和 hi 都又满足要求了（相当于借助腾出的单元用于交换元素）
            - 以此类推， 循环上面步骤， 直到 lo = hi 时退出循环
            将 m 值放回腾出的单元中
            返回 lo
    """
    ref = arr[lo]

    while lo < hi:
        while lo < hi:
            if arr[hi] >= ref:
                hi -= 1
            else:
                arr[lo] = arr[hi]
                lo += 1
                break

        while lo < hi:
            if arr[lo] <= ref:
                lo += 1
            else:
                arr[hi] = arr[lo]
                hi -= 1
                break

    arr[lo] = ref

    return lo
