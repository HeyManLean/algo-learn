# -*- coding: utf-8 -*-

"""
实现计算器功能
"""

class Solution:
    def calculate(self, s: str) -> int:
        """224. 基本计算器
        给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。

        输入：s = "(1+(4+5+2)-3)+(6+8)"
        输出：23

        # 递归计算

        # 基础运算
        1. 遇到加和减数，将数值带符号加入栈中
        2. 遇到乘法或除法，将栈中最后一个数跟下一个数相乘除后重新加入栈中，栈中只维护加减数

        # 括号运算
        1. 遇到一个开括号 ( 则进入递归运算，将 () 的值计算出来加入栈中后，再对当前数值继续遍历
        2. 一开始需要记录开括号和对应闭括号的位置对应

        # 最后，将栈中的数值全部求和得出结果
        """

        # 先移除空格
        s = s.replace(' ', '')

        # index_map 继续每个开闭括号的位置映射
        left_index = []
        index_map = {}
        for idx, c in enumerate(s):
            if c == '(':
                left_index.append(idx)
            elif c == ')':
                index_map[left_index.pop()] = idx

        def _caculate(s: str, left, right):
            # [left, right) 左闭右开
            stk = []

            num = 0
            sign = "+"

            while left < right:
                c = s[left]

                # 遇到数字则加到当前数字
                if c.isdigit():
                    num = num * 10 + int(c)

                # 这个num可能是两个括号算出的新 num
                # 遇到一个开括号 ( 则进入递归运算，将 () 的值计算出来加入栈中后，再对当前数值继续遍历
                if c == '(':
                    right_index = index_map[left]
                    num = _caculate(s, left + 1, right_index)
                    left = right_index  # 跳到闭括号

                # 遇到新的符号，将之前的数字和符号进行运算
                # 处理最后一个字符结果后，需要将num加入栈中
                if c in "+-*/" or left + 1 == right:
                    if sign == '+':
                        stk.append(num)
                    elif sign == '-':
                        stk.append(-num)
                    elif sign == '*':
                        stk[-1] *= num
                    elif sign == '/':
                        stk[-1] = int(stk[-1] / num)
                    sign = c
                    num = 0  # 重置数字

                left += 1

            return sum(stk)

        return _caculate(s, 0, len(s))


if __name__ == '__main__':
    # assert Solution().calculate("1 + 1") == 2
    # assert Solution().calculate("(1+(4+5+2)-3)+(6+8)") == 23
    assert Solution().calculate(" 3/2 ") == 1
    assert Solution().calculate(" 3+5 / 2 ") == 5
    assert Solution().calculate("14-3/2") == 13
    print("OK")
