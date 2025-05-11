# coding=utf-8


def k_substring(string: str, k: int) -> int:
    """Given a string, find the length of the longest substring T that contains at most k distinct characters.

    Example 1:

    Input: s = "eceba", k = 2
    Output: 3
    Explanation: T is "ece" which its length is 3.
    Example 2:

    Input: s = "aa", k = 1
    Output: 2
    Explanation: T is "aa" which its length is 2.
    """
    cmap = {}
    n = len(string)

    left = 0

    res = 0

    for i in range(n):
        cmap[string[i]] = i

        while len(cmap) > k:
            # 记录每个字符最后出现的位置, 如果相等, 则字符不再存在
            if cmap[string[left]] == left:
                cmap.pop(string[left])

            left += 1

        res = max(res, i - left + 1)

    return res
