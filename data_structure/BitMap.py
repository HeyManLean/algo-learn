# coding=utf-8


class BitMap:
    """
    可理解成一个二进制串， 每个 bit 所在索引 key 就是实际的值 value， 而 bit 的值（0或1) 代表 value 是否存在（或者是二叉树的左右节点）。
    而为了方便存储， 将这个串拆分成很多段存储， 下面每段拆成 8 bit。
    """
    DEFAULT_CNT = 1600
    BITMASK = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]

    def __init__(self, n=32):
        self.N = 0
        self.M = None
        self.init(n)

    def init(self, n):
        self.N = (n + 7) // 8
        self.M = [0 for _ in range(self.N)]

    def set(self, k):
        self.expand(k)
        self.M[k >> 3] |= (0x80 >> (k & 0x07))
    
    def clear(self, k):
        self.M[k >> 3] &= ~(0x80 >> (k & 0x07))
    
    def test(self, k):
        return self.M[k >> 3] & (0x80 >> (k & 0x07))

    def expand(self, k):
        if k < 8 < self.N:
            return
        oldN = self.N
        oldM = self.M
        self.init(2 * k)
        self.M[:oldN] = oldM
        del oldM

    def toString(self, length=16):
        result = ''
        i = 0
        while length >= 0:
            code = self.M[i]
            if length > 8:
                result += bin(code)[2:].zfill(8)
            else:
                result += bin(code)[2:].zfill(8)[:length]
                return result
            i += 1
            length -= 8
