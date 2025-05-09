# -*- coding: utf-8 -*-

"""
DFA 树，构造敏感词树

暴 -> {
    力 -> {
        美 -> {
            学 -> end
        }
    }
}

"""
class DFANode:
    def __init__(self, children=None):
        self.children = children or {}

    def __repr__(self):
        children = ','.join([f'{k}->{v}' for k, v in self.children.items()])
        if not children:
            children = 'end'
        return children


class DFATree:
    def __init__(self, words):
        self.root = DFANode()
        self.build(words)

    def build(self, words):
        for word in words:
            root = self.root
            for c in word:
                root = root.children.setdefault(c, DFANode())

    def is_sentitive(self, text):
        n = len(text)
        for i in range(n):
            root = self.root
            for j in range(i, n):
                if root.children.get(text[j]):
                    root = root.children.get(text[j])
            if not root.children:
                return True
        return False


t = DFATree(['你有病', '你有毒', '你有神经病'])
assert t.is_sentitive('不是，你有病呀？')
assert not t.is_sentitive('你好？')
assert t.is_sentitive('你好？你有神经病吗？你有毒？')
print(t.root)
print("OK")
