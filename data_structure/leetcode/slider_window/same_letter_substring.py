# coding=utf-8


def same_letter_substring(s: str, k: int):
    """Longest Substring with Same Letters after Replacement 替换后的最长重复字符

    ```js
    给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。在执行上述操作后，找到包含重复字母的最长子串的长度。

    注意:
    字符串长度 和 k 不会超过 10^4。

    示例 1:

    输入:
    s = "ABAB", k = 2

    输出:
    4

    解释:
    用两个'A'替换为两个'B',反之亦然。
    示例 2:

    输入:
    s = "AABABBA", k = 1

    输出:
    4

    解释:
    将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
    子串 "BBBB" 有最长重复字母, 答案为 4。

    链接: https://leetcode-cn.com/problems/longest-repeating-character-replacement/
    """
    n = len(s)
    count_dict = {}
    maxcount = left = res = 0

    for i in range(n):
        c = s[i]
        count_dict[c] = count_dict.get(c, 0) + 1

        maxcount = max(maxcount, count_dict[c])

        while i - left + 1 - maxcount > k:
            left_c = s[left]
            count_dict[left_c] -= 1

            maxcount = max(maxcount, count_dict[left_c])

            left += 1

        res = max(res, i - left + 1)

    return res


if __name__ == "__main__":
    s = "BAAA"
    k = 0
    res = same_letter_substring(s, k)
    print(res)
