# coding=utf-8
import random


class ListNode:
    def __init__(self, e=None, p=None, s=None):
        self.data = e
        self.pred = p
        self.succ = s

    def insertAsSucc(self, e):
        x = ListNode(e, self, self.succ)
        self.succ.pred = x
        self.succ = x
        return x

    def insertAsPred(self, e):
        x = ListNode(e, self.pred, self)
        self.pred.succ = x
        self.pred = x
        return x

    def __repr__(self):
        return '<ListNode data={}>'.format(self.data)


class List:
    """
        >>> from List import List
        >>> l = List()
        >>> l.size()
        0
        >>> l.insertAsFirst(1)
        <List.ListNode object at 0x7fe12eaf8fd0>
        >>> l.size()
        1
        >>> l.first()
        <List.ListNode object at 0x7fe12eaf8fd0>
        >>> l.first().data
        1
        >>> l.find(1)
        <List.ListNode object at 0x7fe12eaf8fd0>
        >>> a = l.find(1)
        >>> a.data
        1
        >>>
    """
    def __init__(self, L = None, p: ListNode = None, r=0, n=None):
        """双链表
        - 实现单个结点的(有序无序)增删查改基本方法
        - 之后利用这些基本方法实现更复杂的去重，排序等
        """
        # 初始化必须有首尾两个隐藏结点
        self.header = ListNode()
        self.trailer = ListNode()

        self.header.succ = self.trailer
        self.trailer.pred = self.header

        self._size = 0

        # (L, ) 和 (L, r, n)
        if L is not None:
            n = n or L.size()
            self._copyNodes(L[r], L.size())

        # (p, n)
        if p is not None and n is not None:
            self._copyNodes(p, n)

    def __del__(self):
        self._clear()
        del self.header
        del self.trailer

    # protected
    def _clear(self):
        """清除除首尾结点外的所有结点"""
        oldSize = self._size
        while 0 < self._size:
            self.remove(self.header.succ)
            self._size -= 1
        return oldSize

    def _copyNodes(self, p: ListNode, n):
        while 0 < n:
            self.insertAsLast(p.data)
            p = p.succ
            n -= 1

    # public
    # 只读
    def size(self):
        return self._size

    def __len__(self):
        return self._size

    def empty(self):
        return self._size <= 0

    def __getitem__(self, r):
        p = self.first()
        while 0 < r:
            p = p.succ
            r += 1
        return p.data

    def first(self):
        return self.header.succ

    def last(self):
        return self.trailer.pred

    def valid(self, p: ListNode):
        return p and self.trailer != p and self.header != p

    def disorder(self):
        pass

    def find(self, e, n=None, p: ListNode = None):
        """无序查找， p 前面 n 个前驱值(不包括 p)为 e 的结点"""
        if n is None:
            n = self._size
        if p is None:
            p = self.trailer
        while 0 < n:
            p = p.pred
            if p.data == e:
                return p
            n -= 1
        return None

    def search(self, e, n=None, p: ListNode = None):
        if n is None:
            n = self._size
        if p is None:
            p = self.trailer
        while 0 <= n:
            p = p.pred
            if p.data <= e:
                break
            n -= 1
        return p

    # 可写
    def insertAsFirst(self, e):
        self._size += 1
        return self.header.insertAsSucc(e)

    def insertAsLast(self, e):
        self._size += 1
        return self.trailer.insertAsPred(e)

    def insertA(self, p: ListNode, e):
        self._size += 1
        return p.insertAsSucc(e)

    def insertB(self, p: ListNode, e):
        self._size += 1
        return p.insertAsPred(e)

    def remove(self, p: ListNode):
        e = p.data
        p.pred.succ = p.succ
        p.succ.pred = p.pred
        self._size -= 1
        del p
        return e

    def merge(self, L):
        return self._merge(self.first(), self._size, L, L.first(), L.size())

    def _merge(self, p: ListNode, n, L, q: ListNode, m):
        pp = p.pred
        while 0 < m:
            if 0 < n and p.data <= q.data:
                p = p.succ
                n -= 1
            else:
                self.insertB(p, q.data)
                q = q.succ
                L.remove(q.pred)
                m -= 1
        p = pp.succ


    def _mergeSort(self, p: ListNode, n):
        if n < 2:
            return
        m = n // 2
        q = p
        for _ in range(m):
            q = q.succ
        self._mergeSort(p, m)
        self._mergeSort(q, n - m)
        self._merge(p, m, self, q, n - m)
    
    def selectMax(self, p: ListNode = None, n=None):
        if n is None:
            n = self._size
        if p is None:
            p = self.header.succ
        max_ = p
        cur = p  # p 是可变变量(mutable)
        while 1 < n: # n-1次比较
            cur = cur.succ
            if max_.data < cur.data:
                max_ = cur
            n -= 1
        return max_

    def _selectionSort(self, p: ListNode, n):
        head = p
        tail = p
        for _ in range(n):
            tail = tail.succ
        while 1 < n: # 选择 n - 1 次
            max_ = self.selectMax(head, n)
            self.insertB(tail, self.remove(max_))
            n -= 1

    def _insertionSort(self, p: ListNode, n):
        """前面为有序，后面是无序"""
        for r in range(n):
            self.insertA(self.search(p.data, r, p), p.data)
            p = p.succ
            self.remove(p.pred)

    def sort(self, p: ListNode = None, n=None):
        """起始于p的n个结点"""
        if n is None:
            n = self._size
        if p is None:
            p = self.first()
        rand = random.randint(0, 2)
        if rand == 0:
            self._insertionSort(p, n)
        elif rand == 1:
            self._selectionSort(p, n)
        else:
            self._mergeSort(p, n)

    def deduplicate(self):
        if self._size < 2:
            return 0
        oldSize = self._size
        r = 0
        p = self.first()
        while p != self.trailer:
            q = self.find(p.data, r, p)
            if q is not None:
                self.remove(q)
            else:
                r += 1
        return oldSize - self._size

    def uniquify(self):
        if self._size < 2:
            return 0
        oldSize = self._size
        p = self.first()
        q = p.succ
        while q != self.trailer:
            if q.data != p.data:
                p = q
            else:
                self.remove(q)
            q = p.succ
        return oldSize - self._size

    def reverse(self):
        pass

    def traverse(self, func):
        for p in self:
            func(p.data)

    def __iter__(self):
        p = self.header.succ
        while p != self.trailer:
            yield p
            p = p.succ

