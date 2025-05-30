# coding=utf-8


def multi_k_subarry(nums: list, k: int) -> int:
    """Subarrays with Product Less than a Target (medium)

    ```js
    乘积小于K的子数组
    给定一个正整数数组 nums。

    找出该数组内乘积小于 k 的连续的子数组的个数。

    示例 1:

    输入: nums = [10,5,2,6], k = 100
    输出: 8
    解释: 8个乘积小于100的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
    需要注意的是 [10,5,2] 并不是乘积小于100的子数组。
    说明:

    0 < nums.length <= 50000
    0 < nums[i] < 1000
    0 <= k < 10^6
    ```
    """
    # 小于 k
    if k <= 1:
        return 0

    n = len(nums)
    left = 0
    res = 0
    multi = 1

    for i in range(n):
        multi *= nums[i]

        while multi >= k:
            multi /= nums[left]
            left += 1

        res += i - left + 1

    return res
