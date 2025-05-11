# coding=utf-8


def find_disppeared_numbers(nums: list) -> list:
    """Find all Missing Numbers (easy)

    ```js
    找到所有数组中消失的数字
    给定一个范围在 1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

    找到所有在 [1, n] 范围之间没有出现在数组中的数字。

    您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

    示例:

    输入:
    [4,3,2,7,8,2,3,1]

    输出:
    [5,6]
    ```
    """
    n = len(nums)

    for i in range(n):
        new_index = abs(nums[i]) - 1

        if nums[new_index] > 0:
            nums[new_index] *= -1

    res = []

    for i in range(1, n + 1):
        if nums[i - 1] > 0:
            res.append(i)

    return res
