# coding=utf-8


def norepeat_substring(s: str):
    """longest-substring-without-repeating-characters 无重复字符的最长子串

    ```js
    给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

    示例 1:

    输入: "abcabcbb"
    输出: 3
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
    示例 2:

    输入: "bbbbb"
    输出: 1
    解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
    示例 3:

    输入: "pwwkew"
    输出: 3
    解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
         请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
    链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
    """
    count_dict = {}
    temp_dict = {}
    n = len(s)
    left = 0
    res = 0

    for i in range(n):
        c = s[i]
        count_dict[c] = count_dict.get(c, 0) + 1

        if count_dict[c] > 1:
            last = temp_dict[c]

            while left <= last:
                count_dict[s[left]] -= 1
                if count_dict[s[left]] == 0:
                    temp_dict.pop(s[left])

                left += 1

        temp_dict[c] = i

        res = max(res, i - left + 1)

    return res


def norepeat_substring_v2(s: str):
    """网上答案
    左指针遍历, 右指针做判断
    """
    occ = set()
    n = len(s)

    right, res = -1, 0

    for i in range(n):
        if i != 0:
            occ.remove(s[i - 1])

        while right + 1 < n and s[right + 1] not in occ:
            occ.add(s[right + 1])
            right += 1

        res = max(res, right - i + 1)

    return res
