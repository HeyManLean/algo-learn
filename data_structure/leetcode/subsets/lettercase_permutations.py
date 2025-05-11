# coding=utf-8


class Solution:
    def letterCasePermutation(self, S: str) -> list:
        """String Permutations by changing case (medium)

        ```js
        字母大小写全排列
        给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。



        示例：
        输入：S = "a1b2"
        输出：["a1b2", "a1B2", "A1b2", "A1B2"]

        输入：S = "3z4"
        输出：["3z4", "3Z4"]

        输入：S = "12345"
        输出：["12345"]


        提示：

        S 的长度不超过12。
        S 仅由数字和字母组成。
        ```
        """
        n = len(S)
        chars = [c for c in S]
        res = []

        def backtrack(first=0):
            if first == n:
                res.append(''.join(chars))
                return

            lower = chars[first].lower()
            upper = chars[first].upper()

            chars[first] = lower
            backtrack(first + 1)

            if lower != upper:
                chars[first] = upper
                backtrack(first + 1)

        backtrack()
        return res
