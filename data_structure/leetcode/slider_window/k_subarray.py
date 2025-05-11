# coding=utf-8


def sum_k_subarray(nums: list, k: int):
    """和为K的子数组
    给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

    示例 1 :

    输入:nums = [1,1,1], k = 2
    输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
    说明 :

    数组的长度为 [1, 20,000]。
    数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
    """
    # 累计和
    n = len(nums)
    res = 0
    sum_temp = 0
    sum_dict = {}

    for i in range(n):
        sum_temp += nums[i]

        if sum_temp == k:
            res += 1

        res += sum_dict.get(sum_temp - k, 0)

        sum_dict.setdefault(sum_temp, 0)
        sum_dict[sum_temp] += 1

    return res


if __name__ == "__main__":
    nums = [1]
    k = 0
    n = sum_k_subarray(nums, k)

    print(n)
