# coding=utf-8


def threesum(nums: list) -> list:
    """Triplet Sum to Zero (medium)

    ```js
    三数之和
    给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
    使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

    注意：答案中不可以包含重复的三元组。

    示例：

    给定数组 nums = [-1, 0, 1, 2, -1, -4]，

    满足要求的三元组集合为：
    [
        [-1, 0, 1],
        [-1, -1, 2]
    ]
    ```

    以当前两个值为准, 找出第三个值
    """
    res = []

    nums_dict = {}
    for num in nums:
        nums_dict[num] = nums_dict.get(num, 0) + 1

    if nums_dict.get(0, 0) > 2:
        res.append([0, 0, 0])

    pos = []
    neg = []
    for num in nums_dict:
        if num >= 0:
            pos.append(num)
        else:
            neg.append(num)

    for i in neg:
        for j in pos:
            need = - i - j

            if need not in nums_dict:
                continue

            if i < need < j:
                res.append([i, j, need])
            elif (need == i or need == j) and nums_dict[need] > 1:
                res.append([i, j, need])

    return res


def threesum_v2(nums: list) -> list:
    """双指针方式, 以当前值为基准, 找出其他两个值

    以 i 对应的值为最小值, L 为中间值, R 为最大值
    """
    n = len(nums)
    if not nums or n < 3:
        return []

    # 排序
    nums.sort()

    res = []

    for i in range(n):
        if nums[i] > 0:
            return res

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        L = i + 1
        R = n - 1

        while L < R:
            if nums[i] + nums[L] + nums[R] == 0:
                res.append([nums[i], nums[L], nums[R]])

                while L < R and nums[L] == nums[L + 1]:
                    L += 1

                while L < R and nums[R] == nums[R - 1]:
                    R -= 1

                L += 1
                R -= 1

            elif nums[i] + nums[L] + nums[R] > 0:
                R -= 1
            else:
                L += 1

    return res
