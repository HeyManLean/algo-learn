# -*- coding: utf-8 -*-


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        # 每次push数值，如果该值比最小值更小或相等，则加入 min_stack，该栈顶维护当前栈中最小值
        # 每次pop，如果跟当前最小值一直，最小栈也要移除

    def push(self, val: int) -> None:
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        


class FreqStack:
    """最大频次栈，每次pop出当前频率最高的那个值，如果频率相同，pop出离栈顶最近那个值"""

    def __init__(self):
        self.max_freq = 0
        self.freq_to_vals = {}
        self.val_to_freq = {}

    def push(self, val: int) -> None:
        freq = self.val_to_freq.get(val, 0) + 1
        self.val_to_freq[val] = freq
        
        # 保留该值旧的freq映射
        self.freq_to_vals.setdefault(freq, []).append(val)
        self.max_freq = max(self.max_freq, freq)

    def pop(self) -> int:
        val = self.freq_to_vals[self.max_freq].pop()
        if not self.freq_to_vals[self.max_freq]:
            self.max_freq -= 1

        self.val_to_freq[val] -= 1
        return val
