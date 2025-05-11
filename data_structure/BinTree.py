# coding=utf-8


from enum import Enum
import random

from Stack import Stack
from Queue import Queue
from Vector import Vector
from List import List
from BitMap import BitMap


class RBColor(Enum):
    RB_RED = 1
    RB_BLACK = 2


class BinNode:
    """
          lc | parent | rc
        --------------------
                data
        --------------------
        height | npl | color
    """

    def __init__(self, e=None, p=None, lc=None, rc=None, h=0, l=1, c=RBColor.RB_RED.value):
        self.data = e
        self.parent = p
        self.lc = lc
        self.rc = rc
        self.height = h
        self.npl = l  # Null Path Length 左式堆
        self.color = c

    # def __lt__(self, bn):
    #     return self.data < bn.data

    # def __eq__(self, bn):
    #     return self.data == bn.data

    def insertAsLC(self, e):
        lc = BinNode(e, self)
        self.lc = lc
        return lc

    def insertAsRC(self, e):
        rc = BinNode(e, self)
        self.rc = rc
        return rc


BinNodePosi = BinNode


def stature(p: BinNode):
    if p is not None:
        return p.height
    return -1


def IsRoot(x):
    return x.parent is None if x is not None else False


def IsLChild(x):
    return not IsRoot(x) and x.parent.lc == x


def IsRChild(x):
    return not IsRoot(x) and x.parent.rc == x


def HasParent(x):
    return not IsRoot(x)


def HasLChild(x):
    return x.lc is not None


def HasRChild(x):
    return x.rc is not None


def HasChild(x):
    return HasLChild(x) or HasRChild(x)


def HasBothChild(x):
    return HasLChild(x) and HasRChild(x)


def IsLeaf(x):
    return not HasChild(x)


def sibling(p):
    if IsLChild(p):
        return p.parent.rc
    return p.parent.lc


def uncle(x):
    if x.parent is not None:
        return sibling(x.parent)
    return None


def SetFromParentTo(x, data=None):
    if IsLChild(x):
        x.parent.lc = data
    elif IsRChild(x):
        x.parent.rc = data


def release(x):
    del x


class BinTree:
    def __init__(self, x=None):
        self._size = 0
        self._root = x
        if x is not None:
            self.countSize()

    def countSize(self):
        s = []
        self.travIn_I3(self._root, s.append)
        self._size = len(s)
        del s

    def size(self):
        return self._size

    def empty(self):
        return self._root is None

    def __len__(self):
        return self._size

    def root(self):
        return self._root

    def insertAsRoot(self, e):
        self._root = BinNodePosi(e)
        self._size += 1
        return self._root

    def insertAsLC(self, x: BinNodePosi, e):
        self._size += 1
        x.insertAsLC(e)
        self._updateHeightAbove(x)
        return x.lc

    def insertAsRC(self, x: BinNodePosi, e):
        self._size += 1
        x.insertAsRC(e)
        self._updateHeightAbove(x)
        return x.rc

    def attachAsLC(self, x: BinNodePosi, S):
        """
            S: BinTree
        """
        x.lc = S._root
        x.lc.parent = x
        self._size += S._size
        self._updateHeightAbove(x)

        S._root = None
        release(S)
        S = None
        return x

    def attachAsRC(self, x: BinNodePosi, S):
        x.rc = S._root
        x.rc.parent = x
        self._size += S._size
        self._updateHeightAbove(x)

        release(S)
        S = None
        return x

    def remove(self, x: BinNodePosi):
        """移除x为头的子树"""
        SetFromParentTo(x)
        self._updateHeightAbove(x.parent)
        n = self._removeAt(x)
        self._size -= n
        return n

    def _removeAt(self, x: BinNodePosi):
        if x is None:
            return 0
        n = 1 + self._removeAt(x.rc) + self._removeAt(x.lc)
        release(x)
        return n

    def secede(self, x: BinNodePosi):
        SetFromParentTo(x)
        self._updateHeightAbove(x.parent)
        S = BinTree(x)
        x.parent = None
        self._size -= S._size
        return S

    def travPre_R(self, x, visit):
        if x is None:
            return
        visit(x.data)
        self.travPre_R(x.lc, visit)
        self.travPre_R(x.rc, visit)

    def travIn_R(self, x, visit):
        if x is None:
            return
        self.travPre_R(x.lc, visit)
        visit(x.data)
        self.travPre_R(x.rc, visit)

    def travPost_R(self, x, visit):
        if x is None:
            return
        self.travPre_R(x.lc, visit)
        self.travPre_R(x.rc, visit)
        visit(x.data)

    def travPre_I1(self, x, visit):
        """消除尾递归的一般性方法: 使用while"""
        if x is None:
            return
        S = Stack()
        S.push(x)
        while not S.empty():
            x1 = S.pop()
            visit(x1.data)
            if x1.rc is not None:
                S.push(x1.rc)
            if x1.lc is not None:
                S.push(x1.lc)

    def _visitAlongLeftBranch(self, x, visit, S: Stack):
        while x is not None:
            visit(x.data)
            if x.rc is not None:
                S.push(x.rc)
            x = x.lc

    def travPre_I2(self, x, visit):
        """遍历左侧通道， 栈暂存右侧子树(之后对每个右侧子树重复此操作)"""
        if x is None:
            return
        S = Stack()
        while True:
            self._visitAlongLeftBranch(x, visit, S)
            if S.empty():
                break
            x = S.pop()

    def _goAlongLeftBranch(self, x, S: Stack):
        while x is not None:
            S.push(x)
            x = x.lc

    def travIn_I1(self, x, visit):
        """跟前序不一样的是，前序已经访问了父节点，不需将父节点推入栈，所以需要将右节点推入栈待操作。
        而中序，需要把父节点推入栈，因为可以通过父节点获取右节点，所以右节点没必要入栈。
        """
        S = Stack()
        while True:
            self._goAlongLeftBranch(x, S)
            if S.empty():
                break
            x = S.pop()
            visit(x.data)
            x = x.rc

    def travIn_I2(self, x, visit):
        """重复步骤（travIn_I1的等价形式）
            1. 先获取左侧通道；
            2. 如果左侧到了尽头， 则处理当前节点， 后将当前节点指向其右节点。
            深度遍历： 1. 当前节点, 2. 趋势逐渐往上.
        """
        S = Stack()
        while True:
            if x is not None:
                S.push(x)
                x = x.lc
            elif not S.empty():
                x = S.pop()
                visit(x.data)
                x = x.rc
            else:
                break

    def getSucc(self, s: BinNode):
        """获取中序遍历的直接后继节点"""
        if HasRChild(s):
            s = s.rc
            while HasLChild(s):
                s = s.lc
        else:
            while IsRChild(s):
                s = s.parent
            s = s.parent
        return s

    def travIn_I3(self, x, visit):
        """不使用栈实现"""
        backtrack = False
        while True:
            if not backtrack and HasLChild(x):
                x = x.lc
            else:
                visit(x.data)
                if HasRChild(x):
                    x = x.rc
                    backtrack = False
                else:
                    x = self.getSucc(x)
                    if x is None:
                        break
                    backtrack = True

    def _gotoHLVFL(self, S: Stack):
        x = S.top
        while x is not None:
            if HasLChild(x):
                if HasRChild(x):
                    S.push(x.rc)
                S.push(x.lc)
            else:
                S.push(x.rc)
            x = S.top
        S.pop()

    def travPost_I1(self, x, visit):
        """将所有节点放在栈里面"""
        S = Stack()
        if x is not None:
            S.push(x)
        while not S.empty():
            if S.top != x.parent:  # 不为当前节点的父节点，则为右兄弟节点
                self._gotoHLVFL(S)
            x = S.pop()
            visit(x.data)

    def travLevel(self, x, visit):
        """层级遍历, 使用队列"""
        Q = Queue()
        Q.enqueue(x)
        while not Q.empty():
            x = Q.dequeue()
            visit(x.data)
            if HasLChild(x):
                Q.enqueue(x.lc)
            if HasRChild(x):
                Q.enqueue(x.rc)

    def travPre(self, visit=print):
        rand = random.randint(1, 3)
        if rand % 3 == 0:
            self.travPre_I1(self._root, visit)
        elif rand % 3 == 1:
            self.travPre_I2(self._root, visit)
        else:
            self.travPre_R(self._root, visit)

    def travIn(self, visit=print):
        rand = random.randint(1, 4)
        if rand % 3 == 0:
            self.travIn_I1(self._root, visit)
        elif rand % 3 == 1:
            self.travIn_I2(self._root, visit)
        elif rand % 3 == 2:
            self.travIn_I3(self._root, visit)
        else:
            self.travPre_R(self._root, visit)

    def travPost(self, visit=print):
        rand = random.randint(1, 2)
        if rand % 3 == 0:
            self.travPost_I1(self._root, visit)
        else:
            self.travPost_R(self._root, visit)

    def __lt__(self, t):
        return self._root and t._root and self._root < t._root

    def __eq__(self, t):
        return self._root and t._root and self._root == t._root

    @staticmethod
    def _updateHeight(x: BinNodePosi):
        x.height = 1 + max(stature(x.lc), stature(x.rc))
        return x.height

    def _updateHeightAbove(self, x: BinNodePosi):
        """插入时更新高度, 左右有一边高度没有改变"""
        while x is not None:
            self._updateHeight(x)
            x = x.parent


class PFCCoding:
    """
        1. 由很多有单个节点的树合并成一个树， 且每个叶子都携带字符;
        2. 由树递归遍历并记录路径(01...)记录每个字符对应的编码;
        3. 编码: 将字符串每个字符从 table 找到对应的编码， 连接成一串编码字符串（010101010）；
        4. 解码: 将编码字符串 0 对应左节点， 1 对应右节点查找（目标叶子节点）对应的字符， 连接成原来的字符串。
        >>> PFCCoding.main(['abcd', '0123'])
        a
        b
        c
        d
        0
        1
        2
        3
    """
    N_CHAR = 0x80 - 0x20

    @classmethod
    def initForest(cls):
        forest = Vector()
        for i in range(cls.N_CHAR):
            forest.insert(i, BinTree())
            forest[i].insertAsRoot(chr(0x20 + i))
        return forest

    @classmethod
    def generateTree(cls, forest: Vector):
        """将所有字符随机合并（左右子树）"""
        import random
        while 1 < forest.size():
            S = BinTree()
            S.insertAsRoot('^')
            r1 = random.randint(0, cls.N_CHAR) % forest.size()
            S.attachAsLC(S.root(), forest[r1])
            forest.remove(r1)
            r2 = random.randint(0, cls.N_CHAR) % forest.size()
            S.attachAsRC(S.root(), forest[r2])
            forest.remove(r2)
            forest.insert(forest.size(), S)
        return forest[0]

    @classmethod
    def generateCT(cls, code: BitMap, length: int, table: dict, v: BinNodePosi):
        if IsLeaf(v):
            table[v.data] = code.toString(length)
        if HasLChild(v):
            code.clear(length)
            cls.generateCT(code, length + 1, table, v.lc)
        if HasRChild(v):
            code.set(length)
            cls.generateCT(code, length + 1, table, v.rc)

    @classmethod
    def generateTable(cls, tree: BinTree):
        """生成字符(由其在树的路径)和其编码的映射关系"""
        table = dict()
        code = BitMap()
        cls.generateCT(code, 0, table, tree.root())
        release(code)
        return table

    @classmethod
    def encode(cls, table: dict, codeString: BitMap, s: str):
        n = 0
        for c in s:
            pCharCode = table.get(c)
            if pCharCode is None:
                pCharCode = table.get(chr(ord(c) + ord('A') - ord('a')))
            if pCharCode is None:
                pCharCode = table.get(' ')
            for c in pCharCode:
                if c == '1':
                    codeString.set(n)
                else:
                    codeString.clear(n)
                n += 1
        return n

    @classmethod
    def decode(cls, tree: BinTree, code: BitMap, n: int):
        x = tree.root()
        for i in range(n):
            if code.test(i):
                x = x.rc
            else:
                x = x.lc
            if IsLeaf(x):
                print(x.data)
                x = tree.root()

    @classmethod
    def main(cls, argv: list, argc: int = None):
        argc = argc or len(argv)
        forest = cls.initForest()
        tree = cls.generateTree(forest)
        table = cls.generateTable(tree)

        for i in range(argc):
            codeString = BitMap()
            n = cls.encode(table, codeString, argv[i])
            cls.decode(tree, codeString, n)
        release(table)
        release(tree)
        return 0

    @classmethod
    def testTrav(cls):
        """
            >>> PFCCoding.testTrav()
        """
        forest = cls.initForest()
        tree = cls.generateTree(forest)
        if not isinstance(tree, BinTree):
            tree = BinTree()
        x = tree.root()
        print('travIn_I1=================================================')
        s = []
        tree.travIn_I1(x, s.append)
        print(s)
        print('travIn_I2=================================================')
        s = []
        tree.travIn_I2(x, s.append)
        print(s)
        print('travIn_I3=================================================')
        s = []
        tree.travIn_I3(x, s.append)
        print(s)
        print('travPre_I1=================================================')
        s = []
        tree.travPre_I1(x, s.append)
        print(s)
        print('travPre_I2=================================================')
        s = []
        tree.travPre_I2(x, s.append)
        print(s)
        print('travPost_I=================================================')
        s = []
        tree.travPost_I1(x, s.append)
        print(s)


class HuffChar:
    def __init__(self, c: str = '^', w: int = 0):
        self.ch = c
        self.weight = w

    def __lt__(self, hc):
        return self.weight > hc.weight  # 故意颠倒！

    def __eq__(self, hc):
        return self.weight == hc.weight


class HuffmanCoding:
    """
        >>> HuffmanCoding.main(['abcd', '1234'])
        [94, 102, 88, 111, 124, 131, 126, 109, 112, 104, 91, 107, 107, 120, 104, 110, 113, 123, 118, 99, 106, 110, 111, 104, 101, 101, 115, 107, 130, 118, 111, 112, 115, 113, 114, 104, 110, 116, 100, 110, 134, 106, 126, 117, 108, 94, 112, 107, 120, 115, 109, 130, 110, 136, 113, 115, 85, 128, 110, 115, 136, 117, 110, 130, 111, 91, 111, 122, 113, 107, 110, 108, 102, 107, 94, 110, 112, 103, 103, 118, 87, 106, 114, 106, 109, 114, 90, 143, 110, 115, 0, 0, 0, 0, 0, 0]
        a
        b
        c
        d
        1
        2
        3
        4
    """
    N_CHAR = 0x80 - 0x20

    @classmethod
    def statistics(cls, sample_text_file):
        """根据样本字符统计每个字符出现频率"""
        freq = [0 for i in range(cls.N_CHAR)]
        with open(sample_text_file, 'r') as fp:
            s = fp.read()
            for ch in s:
                ord_ch = ord(ch)
                if ord_ch >= 0x20:
                    freq[ord_ch - 0x20] += 1
        return freq

    @classmethod
    def initForest(cls, freq):
        forest = List()
        for i in range(cls.N_CHAR):
            forest.insertAsLast(BinTree())
            forest.last().data.insertAsRoot(HuffChar(chr(0x20 + i), freq[i]))
        return forest

    @classmethod
    def minHChar(cls, forest):
        p = forest.first()
        minChar = p
        minWeight = p.data.root().data.weight
        p = p.succ
        while forest.valid(p):
            pDataWeight = p.data.root().data.weight
            if minWeight > pDataWeight:
                minWeight = pDataWeight
                minChar = p
            p = p.succ
        return forest.remove(minChar)

    @classmethod
    def generateTree(cls, forest):
        while 1 < forest.size():
            T1 = cls.minHChar(forest)
            T2 = cls.minHChar(forest)
            S = BinTree()
            S.insertAsRoot(
                HuffChar('^', T1.root().data.weight + T2.root().data.weight))
            S.attachAsLC(S.root(), T1)
            S.attachAsRC(S.root(), T2)
            forest.insertAsLast(S)
        return forest.first().data

    @classmethod
    def generateCT(cls, code: BitMap, length: int, table: dict, v: BinNodePosi):
        if IsLeaf(v):
            table[v.data.ch] = code.toString(length)
            return
        if HasLChild(v):
            code.clear(length)
            cls.generateCT(code, length + 1, table, v.lc)
        if HasRChild(v):
            code.set(length)
            cls.generateCT(code, length + 1, table, v.rc)

    @classmethod
    def generateTable(cls, tree):
        table = dict()
        code = BitMap()
        cls.generateCT(code, 0, table, tree.root())
        release(code)
        return table

    @classmethod
    def encode(cls, table: dict, codeString: BitMap, s: str):
        n = 0
        for c in s:
            pCharCode = table.get(c)
            if pCharCode is None:
                pCharCode = table.get(chr(ord(c) + ord('A') - ord('a')))
            if pCharCode is None:
                pCharCode = table.get(' ')
            for c in pCharCode:
                if c == '1':
                    codeString.set(n)
                else:
                    codeString.clear(n)
                n += 1
        return n

    @classmethod
    def decode(cls, tree: BinTree, code: BitMap, n: int):
        x = tree.root()
        for i in range(n):
            if code.test(i):
                x = x.rc
            else:
                x = x.lc
            if IsLeaf(x):
                print(x.data.ch)
                x = tree.root()

    @classmethod
    def main(cls, argv: list, argc: int = 0, filename: str = None):
        filename = cls.generateSample(filename)
        freq = cls.statistics(filename)
        print(freq)
        forest = cls.initForest(freq)
        tree = cls.generateTree(forest)
        table = cls.generateTable(tree)

        argc = argc or len(argv)
        for i in range(argc):
            codeString = BitMap()
            n = cls.encode(table, codeString, argv[i])
            cls.decode(tree, codeString, n)
        release(codeString)
        release(table)
        release(tree)
        return 0

    @classmethod
    def generateSample(cls, filename=None):
        filename = filename or '../data/sampleAscii.txt'
        import os
        if not os.path.isfile(filename):
            with open(filename, 'w+') as fp:
                for _ in range(10000):
                    rand = random.randint(0x20, 0x79)
                    fp.write(chr(rand))
        return filename
