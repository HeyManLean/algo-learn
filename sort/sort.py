# -*- coding: utf-8 -*-

def choice_sort(nums: list[int]):
    """选择排序

    每次从中选择其中最小值，交换放在数组前面，直到最后一个元素结束

    - 遇到排序好的数组，还是需要O(n²）时间复杂度
    - 可能改变元素相对位置
    """
    for i in range(len(nums) - 1):
        min_index = 0
        min_val = float('inf')
        for j in range(i, len(nums)):
            if nums[j] < min_val:
                min_index = j
                min_val = nums[j]

        nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums


def bubble_sort(nums: list[int]):
    """冒泡排序

    每次遍历，将较大值往后挪，直到最后一个元素排序结束

    - 遇到排序好的数组，只需O(n)时间复杂度
    - 元素相对顺序能否保证
    """
    hi = len(nums) - 1
    while hi > 0:
        swap_flag = False  # 是否交换，没有交换则提前结束
        for i in range(hi):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swap_flag = True

        if not swap_flag:
            break
    return nums


def insert_sort(nums: list[int]):
    """插入排序

    从0开始，假设左侧数组进行排序，后续将新的元素跟左侧元素比较，进行冒泡

    - 对排好序的数组，接近O(n)时间复杂度
    - 对于逆序的数组，小于 n²/2，比冒泡排序稍微优一些
    """
    start = 0
    while start < len(nums):
        for i in range(start, 0, -1):
            if nums[i] < nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
            else:
                # 已经排好序，不需要继续冒泡
                break

        start += 1
    return nums


def shell_sort(nums: list[int]):
    """希尔排序

    按照 h 步长，对相同步长间隔形成的子数组，进行插入排序
    逐步将 h 减少，直到 h 为 1，排序结束
    """
    n = len(nums)
    h = 1
    while h * 2 < n:
        h *= 2

    while h >= 1:
        for nxt in range(h):
            # 按照步长进行插入排序
            start = nxt
            while start < len(nums):
                for i in range(start, 0, -1):
                    if nums[i] < nums[i - 1]:
                        nums[i], nums[i - 1] = nums[i - 1], nums[i]
                    else:
                        # 已经排好序，不需要继续冒泡
                        break
                start += h
        h //= 2
    return nums


def quick_sort(arr: list[int]):
    """快速排序
    取一个基准点（一般是第一个数），左右指针移动&交换
    - 将小于基准数的值放在基准数左边，将大于基准数的值放在基准数右边

    最后分别对基准值左边区间、右边区间进行递归快速排序
    """
    _quick_sort(arr, 0, len(arr) - 1)
    return arr


def _quick_sort(arr: list[int], low, high):
    # 左闭右闭
    if low >= high:
        return

    # 第一个值作为基准值
    base = arr[low]
    i = low
    j = high

    while i < j:
        # 右边找到小于基准值的数，覆盖到当前左边位置
        while i < j and arr[j] >= base:
            j -= 1

        if i < j:
            arr[i] = arr[j]

        # 左边找到大于基准值的数，覆盖到左右为止
        while i < j and arr[i] < base:
            i += 1

        if i < j:
            arr[j] = arr[i]

    arr[i] = base  # i 已经找好位置了
    _quick_sort(arr, low, i - 1)
    _quick_sort(arr, i + 1, high)


def merge_sort(arr: list[int]):
    """归并排序
    二分法，先对数组左边区域进行排序，再对右边区域排序，最后将两个有序数组进行合并排序
    """
    _merge_sort(arr, 0, len(arr) - 1)
    return arr


def _merge_sort(arr: list[int], low, high):
    # 左闭右闭
    if low >= high:
        return

    mid = low + (high - low) // 2

    _merge_sort(arr, low, mid)
    _merge_sort(arr, mid + 1, high)

    # 将最大值先覆盖到数组最后
    temp_arr = arr[mid+1:high+1]
    temp_pos = len(temp_arr) - 1
    while mid >= low and temp_pos >= 0:
        if arr[mid] > temp_arr[temp_pos]:
            arr[high] = arr[mid]
            mid -= 1
        else:
            arr[high] = temp_arr[temp_pos]
            temp_pos -= 1

        high -= 1

    while temp_pos >= 0:
        arr[high] = temp_arr[temp_pos]
        temp_pos -= 1
        high -= 1

    while mid >= low:
        arr[high] = arr[mid]
        mid -= 1
        high -= 1



if __name__ == '__main__':
    for sort in [
        choice_sort,
        bubble_sort,
        insert_sort,
        shell_sort,
        quick_sort,
        merge_sort,
    ]:
        assert sort([4, 3, 1, 5, 2, 6]) == [1, 2, 3, 4, 5, 6]
        print(sort.__name__, 'ok')

    print('OK')
