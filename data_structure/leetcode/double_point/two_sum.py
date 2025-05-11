# coding=utf-8


def two_sum(nums: list, target: int) -> list:
    """Pair with Target Sum (easy)

    ```js
    两数之和
    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

    你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

    

    示例:

    给定 nums = [2, 7, 11, 15], target = 9

    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]
    ```
    """
    n = len(nums)
    nums_dict = {}

    for i in range(n):
        diff = target - nums[i]
        if diff in nums_dict:
            return [nums_dict[diff], i]

        nums_dict[nums[i]] = i

    return []


if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 6

    print(two_sum(nums, target))
