# coding=utf-8


def ones_subarray(A: list, K: int):
    """Longest Subarray with Ones after Replacement

    ```js
    1004. 最大连续1的个数 III
    给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。

    返回仅包含 1 的最长（连续）子数组的长度。

    

    示例 1：

    输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
    输出：6
    解释：
    [1,1,1,0,0,1,1,1,1,1,1]
    粗体数字从 0 翻转到 1，最长的子数组长度为 6。
    示例 2：

    输入：A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
    输出：10
    解释：
    [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
    粗体数字从 0 翻转到 1，最长的子数组长度为 10。

    链接: https://leetcode-cn.com/problems/max-consecutive-ones-iii/?utm_source=LCUS&utm_medium=ip_redirect_q_uns&utm_campaign=transfer2china
    ```
    """
    n = len(A)
    left = zero_cnt = res = 0

    for i in range(n):
        num = A[i]

        if num == 0:
            zero_cnt += 1

        while zero_cnt > K:
            left_num = A[left]
            if left_num == 0:
                zero_cnt -= 1

            left += 1

        res = max(res, i - left + 1)

    return res


def ones_subarray_v2(A: list, K: int):
    """网上答案, 没必要缩小窗口, 不合适保持原来大小即可"""
    n = len(A)
    left = zero_cnt = i = 0

    for i in range(n):
        num = A[i]

        if num == 0:
            zero_cnt += 1

        if zero_cnt > K:
            left_num = A[left]
            if left_num == 0:
                zero_cnt -= 1

            left += 1

    return i - left + 1
