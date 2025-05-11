# coding=utf-8


def threesumcloset(nums: list, target: int) -> int:
    """Triplet Sum Close to Target (medium)

    ```js
    最接近的三数之和
    给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

    

    示例：

    输入：nums = [-1,2,1,-4], target = 1
    输出：2
    解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
    

    提示：

    3 <= nums.length <= 10^3
    -10^3 <= nums[i] <= 10^3
    -10^4 <= target <= 10^4
    ```
    """
    n = len(nums)

    nums.sort()
    res = 0
    diff = float('inf')

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        L = i + 1
        R = n - 1

        while L < R:
            s = nums[i] + nums[L] + nums[R]
            if s == target:
                return s

            if abs(s - target) < diff:
                res = s
                diff = abs(s - target)

            # 要不增加, 要么减少, 左右指针只能选一个
            if s > target:
                R -= 1
            else:
                L += 1

    return res
