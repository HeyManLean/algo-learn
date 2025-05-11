# coding=utf-8

import math

from BitMap import BitMap


class Dictionary:
    def __init__(self):
        self.N = 0

    def size(self):
        return self.N

    def put(self, k, V):
        return 0

    def get(self, k):
        return 0

    def remove(self, k):
        return 0


def isPrime(x):
    """验证是否为素数
    如果 m 能被 2 ~ m-1 之间任一整数整除，其二个因子必定有一个小于或等于 sqrt(m)，另一个大于或等于 sqrt(m), 所以整除左边即可。
    """
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def primeNLT(c: int, n: int):
    """获取 [c, n) 范围内的首个素数"""
    while c < n:
        if isPrime(c):
            return c
        c += 1
    return c


def hashCode(x):
    """将对象 x 转成hash数字索引"""
    try:
        d = int(x)
    except:
        if not isinstance(x, str):
            raise TypeError("KEY must be a integer or a string!")
        if len(x) == 0:
            raise KeyError("KEY can not be a empty string!")
        if len(x) == 1:
            return ord(x)
        d = 0
        for c in x:
            d = d << 8
            d += ord(c)
    return d


class Entry:
    """词条对象"""

    def __init__(self, k, v=None):
        self.key = k
        self.value = v

    def __repr__(self):
        return '<Entry (key={}, value={})>'.format(self.key, self.value)


class HashTable(Dictionary):
    """散列表
    开辟物理地址连续的桶数组 ht， 借助散列函数 hash(), 
    将词条关键码 key 映射为桶地址 hash(key), 从而快速地确定待操作词条的物理位置.

    h = HashTable()
    h.put(1, 2)
    h.put(100, 5)
    h.put('haha', 100)
    print(h.get(100), h.get('haha'))

    for i in h:
        print(i)

    print(h[100])
    print(h['haha1'])

    =============================================
    5 100
    100
    1
    haha
    5
    Traceback (most recent call last):
    File "HashTable.py", line 187, in <module>
        print(h['haha1'])
    File "HashTable.py", line 174, in __getitem__
        raise KeyError('KEY does not exist!')
    KeyError: 'KEY does not exist!'
    """

    def __init__(self, c=5):
        """创建一个容量不小于5的散列表"""
        # 桶数组容量
        self.M = primeNLT(c, 1048576)

        # 词条数量
        self.N = 0

        # 桶数组
        self.ht = [None for i in range(self.M)]

        self.lazyRemoval = BitMap(self.M)

    def lazilyRemoved(self, x):
        return self.lazyRemoval.test(x)

    def markAsRemoved(self, x):
        self.lazyRemoval.set(x)

    def probe4Hit(self, k):
        """找到词条匹配的桶
        hashCode 得到 hash地址后， 针对桶对应位置
        1. 成功匹配: 桶非空且桶保存的关键码等于k，直接返回。
        2. 没有成功匹配: 桶为空且不带懒惰删除标志时， 查找失败, 返回桶的地址。
        3. 没有成功匹配时: 桶非空且桶保存的关键码不等于k 或者 带懒惰删除标识时， 沿着查找链继续查找。
        需要继续查找：
        1. 桶非空 且 桶保存的关键码不等于k
        2. 桶为空 且 带懒惰删除标识
        其余情况直接返回。
        """
        r = hashCode(k) % self.M  # 除余法， 让地址索引值在桶数量范围内
        while (self.ht[r] is not None and k != self.ht[r].key) or\
                (self.ht[r] is None and self.lazilyRemoved(r)):
            r = (r + 1) % self.M  # 也可以通过平方， 闭散列策略
        return r

    def probe4Free(self, k):
        """找到首个可用的桶
        hashCode找到地址， 对应桶为空即可
        """
        r = hashCode(k) % self.M
        while self.ht[r] is not None:
            r = (r + 1) % self.M
        return r

    def rehash(self):
        """重散列算法，扩充桶数组"""
        oldHt = self.ht
        self.__init__(self.M * 2)
        for e in oldHt:
            if e is not None:
                self.put(e.key, e.value)
        del oldHt

    def size(self):
        return self.N

    def put(self, k, V):
        r = self.probe4Hit(k)
        if self.ht[r] is not None:
            return False
        r = self.probe4Free(k)
        self.ht[r] = Entry(k, V)
        self.N += 1
        if (self.N * 2 > self.M):  # 装填因子高于 50% 需要重散列（扩容）
            self.rehash()
        return True

    def get(self, k):
        r = self.probe4Hit(k)
        if self.ht[r] is not None:
            return self.ht[r].value
        else:
            return None

    def remove(self, k):
        r = self.probe4Hit(k)
        if self.ht[r] is None:
            return False
        self.ht[r] = None
        self.markAsRemoved(r)
        self.N -= 1
        return True

    def __iter__(self):
        # for e in self.ht:
        #     if e is not None:
        #         yield e.key
        yield from (e.key for e in self.ht if e is not None)

    def __getitem__(self, k):
        value = self.get(k)
        if value is not None:
            return value
        else:
            raise KeyError('KEY does not exist!')
