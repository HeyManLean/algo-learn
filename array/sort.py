# -*- coding: utf-8 -*-



class Solution:
    def quick_sort(self, arr: list[int]):
        """
        取一个基准点（一般是第一个数），左右指针移动&交换
        - 将小于基准数的值放在基准数左边，将大于基准数的值放在基准数右边

        最后分别对基准值左边区间、右边区间进行递归快速排序
        """
        self._quick_sort(arr, 0, len(arr) - 1)

        print(arr)

    def _quick_sort(self, arr: list[int], low, high):
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
        self._quick_sort(arr, low, i - 1)
        self._quick_sort(arr, i + 1, high)

    def merge_sort(self, arr: list[int]):
        """
        二分法，先对数组左边区域进行排序，再对右边区域排序，最后将两个有序数组进行合并排序
        """
        self._merge_sort(arr, 0, len(arr) - 1)
        print(arr)

    def _merge_sort(self, arr: list[int], low, high):
        # 左闭右闭
        if low >= high:
            return

        mid = low + (high - low) // 2

        self._merge_sort(arr, low, mid)
        self._merge_sort(arr, mid + 1, high)

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
    nums = [3, 2, 4, 5, 6, 1]
    Solution().quick_sort(nums)
    assert nums == [1, 2, 3, 4, 5, 6]

    nums = [3, 2, 4, 5, 6, 1]
    Solution().merge_sort(nums)
    assert nums == [1, 2, 3, 4, 5, 6]

    print("ok")
