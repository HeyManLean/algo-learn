# coding=utf-8


def threesum_smaller(nums: list, target: int):
    """Triplets with Smaller Sum (medium)

    ```js
    Given an array of n integers nums and a target,
    find the number of index triplets i, j, k with 0 <= i < j < k < n
    that satisfy the condition nums[i] + nums[j] + nums[k] < target.

    For example, given nums = [-2, 0, 1, 3], and target = 2.

    Return 2. Because there are two triplets which sums are less than 2:

    [-2, 0, 1]
    [-2, 0, 3]
    ```
    """
    n = len(nums)
    res = 0

    for i in range(nums - 2):
        L = i + 1
        R = n - 1

        while L < R:
            s = nums[i] + nums[L] + nums[R]
            if s < target:
                res += R - L
                L += 1
            else:
                R -= 1

    return res
