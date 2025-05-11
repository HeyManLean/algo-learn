# coding=utf-8

from List import List
from Vector import Vector


class Stack(Vector):
    """
        >>> s = Stack()
        >>> s.push(1)
        >>> s.push(2)
        >>> s.push(3)
        >>> s.pop()
        3
        >>> s.size()
        2
        >>> print(s)
        <Vector([1, 2])>
        >>> s.top
        2
    """

    def push(self, e):
        self.insert(self.size(), e)

    def pop(self):
        return self.remove(self.size() - 1)

    @property
    def top(self):
        return self[self.size() - 1]

    def __repr__(self):
        return '<Stack({})>'.format(','.join([str(i) for i in self]))


def convert_recursive(S: Stack, n: int, base: int):
    """
        递归， 将正整数 n 转成 base 进制数。
        S: Stack
        n: Positive Integer
        base: (1, 16)
    """
    digit = ['0', '1', '2', '3', '4', '5', '6',
             '7', '8', '9', 'A', 'B', 'C', 'D', 'E']
    if 0 < n:
        S.push(digit[n % base])
        convert_recursive(S, n // base, base)


def convert_interation(S: Stack, n: int, base: int):
    """
        迭代， 将正整数 n 转成 base 进制数。
        S: Stack
        n: Positive Integer
        base: (1, 16)
    """
    digit = ['0', '1', '2', '3', '4', '5', '6',
             '7', '8', '9', 'A', 'B', 'C', 'D', 'E']
    while n > 0:
        S.push(digit[n % base])
        n //= base


# 逆序输出
def convert(n, base):
    """十进制转其他
        >>> convert(1000, 2)
        recursive
        '1111101000'
        >>> convert(1000, 3)
        recursive
        '1101001'
        >>> convert(1000, 4)
        iteration
        '33220'
        >>> convert(1000, 8)
        iteration
        '1750'
        >>> convert(1000, 16)
        iteration
        '3E8'
    """
    S = Stack()
    import random
    i = random.randint(0, 1)
    if i == 0:
        print('recursive')
        convert_recursive(S, n, base)
    else:
        print('iteration')
        convert_interation(S, n, base)
    result = ''
    for _ in range(S.size()):
        result += S.pop()
    return result


# 递归嵌套
def paren(exp: str, lo=0, hi=None):
    """检查表达式里面的括号是否一一匹配（开合）
        >>> paren('[(4+5) * 5 - (5 - 2) * (6-8)] * 2 + 2 * 3')
        True
    """
    if hi is None:
        hi = len(exp)
    S = Stack()
    for char in exp[lo: hi]:
        if char == '(' or char == '[' or char == '{':
            S.push(char)
            continue
        elif char == ']':
            if S.empty() or S.pop() != '[':
                return False
        elif char == ')':
            if S.empty() or S.pop() != '(':
                return False
        elif char == '}':
            if S.empty() or S.pop() != '{':
                return False
    return S.empty()


# 延迟缓冲
class ExpToRPN:
    N_OPTR = 9
    pri_order = {
        '+': 0,
        '-': 1,
        '*': 2,
        '/': 3,
        '^': 4,
        '!': 5,
        '(': 6,
        ')': 7,
        '$': 8
    }
    pri = [  # 栈顶： 当前
        # 当前 +    -    *    /    ^    !    (    )    $     # 栈顶
        ['>', '>', '<', '<', '<', '<', '<', '>', '>'],  # +
        ['>', '>', '<', '<', '<', '<', '<', '>', '>'],  # -
        ['>', '>', '>', '>', '<', '<', '<', '>', '>'],  # *
        ['>', '>', '>', '>', '<', '<', '<', '>', '>'],  # /
        ['>', '>', '>', '>', '>', '<', '<', '>', '>'],  # ^
        ['>', '>', '>', '>', '>', '>', ' ', '>', '>'],  # !
        ['<', '<', '<', '<', '<', '<', '<', '=', ' '],  # (
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # )
        ['<', '<', '<', '<', '<', '<', '<', ' ', '=']   # $
    ]

    def __init__(self, exp: str):
        self.RPN = []
        self.exp = exp.replace(' ', '') + '$'

    def evaluate(self):
        opnd = Stack()
        optr = Stack()
        optr.push('$')
        i = 0
        while not optr.empty():
            char = self.exp[i]
            if char.isdigit():
                endpos = self.readNumber(self.exp, i)
                opnd.push(self.exp[i: endpos])
                self.RPN.append(opnd.top)
                i = endpos
            else:
                order = self.orderBetween(optr.top, char)
                if order == '<':
                    optr.push(char)
                    i += 1
                elif order == '=':
                    optr.pop()
                    i += 1
                # 如果栈顶优先级高，则先执行栈顶（前面的）运算。
                elif order == '>':
                    op = optr.pop()
                    self.RPN.append(op)
                    if op == '!':
                        pOpnd = opnd.pop()
                        opnd.push(self.calcu(pOpnd, op))
                    else:
                        pOpnd2 = opnd.pop()
                        pOpnd1 = opnd.pop()
                        opnd.push(self.calcu(pOpnd1, op, pOpnd2))
                        # 不必 i += 1, 直到不是 >
                else:
                    raise TypeError('Exp is not correct for evaluating!')
        return opnd

    @staticmethod
    def readNumber(exp: str, lo):
        import re
        pattern = re.compile(r'\d+(\.\d+)?')
        result = pattern.match(exp[lo:])
        if result is None:
            return lo
        return lo + result.end()

    @classmethod
    def orderBetween(cls, optr1, optr2):
        tr1_index = cls.pri_order[optr1]
        tr2_index = cls.pri_order[optr2]
        return cls.pri[tr1_index][tr2_index]

    @classmethod
    def calcu(cls, opnd1, op, opnd2=None):
        if op == '!':
            return int(bool(opnd1))
        return str(eval(opnd1 + op + opnd2))


def evaluate(exp: str):
    """将表达式转成逆波兰表达式
        >>> evaluate('(4+5) * 5 - (5 - 2) * (6-8) * 2 + 2 * 3')
        <Vector(['63'])>
        ['4', '5', '+', '5', '*', '5', '2', '-', '6', '8', '-', '*', '2', '*', '-', '2', '3', '*', '+']
    """
    exp2rpn = ExpToRPN(exp)
    print(exp2rpn.evaluate())
    print(exp2rpn.RPN)


# 试探回溯（八皇后)
class Queen:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, q):
        return self.x == q.x or self.y == q.y or self.x + self.y == q.x + q.y or self.x - self.y == q.x - q.y

    def __repr__(self):
        return '<Queen({0}, {1})>'.format(self.x, self.y)


def placeQueens(n: int):
    """N皇后
        >>> print(placeQueens(4))
        <Stack()>
        <Stack(<Queen(0, 0)>)>
        <Stack(<Queen(0, 0)>,<Queen(1, 2)>)>
        <Stack(<Queen(0, 0)>,<Queen(1, 2)>)>
        <Stack(<Queen(0, 0)>)>
        <Stack(<Queen(0, 0)>,<Queen(1, 3)>)>
        <Stack(<Queen(0, 0)>,<Queen(1, 3)>,<Queen(2, 1)>)>
        <Stack(<Queen(0, 0)>,<Queen(1, 3)>,<Queen(2, 1)>)>
        <Stack(<Queen(0, 0)>,<Queen(1, 3)>)>
        <Stack(<Queen(0, 0)>,<Queen(1, 3)>)>
        <Stack(<Queen(0, 0)>)>
        <Stack()>
        <Stack(<Queen(0, 1)>)>
        <Stack(<Queen(0, 1)>,<Queen(1, 3)>)>
        <Stack(<Queen(0, 1)>,<Queen(1, 3)>,<Queen(2, 0)>)>
        <Stack(<Queen(0, 1)>,<Queen(1, 3)>,<Queen(2, 0)>,<Queen(3, 2)>)>
    """
    solu = Stack()
    q = Queen(0, 0)
    while (q.x > 0 or q.y < n) and q.x < n:
        print(solu)
        if n <= solu.size() or n <= q.y:
            q = solu.pop()
            q.y += 1
        else:
            while q.y < n and 0 <= solu.find(q):
                q.y += 1
            if q.y < n:
                solu.push(q)
                q = Queen(q.x + 1, 0)
    return solu
