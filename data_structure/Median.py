# coding=utf-8

from Vector import Vector


class Median:
    @classmethod
    def majority(cls, A: Vector):
        """求数组的众数, 并检查是否为众数
        众数必为中位数！
        数组中某个元素的个数超过数组长度的一半， 就是众数。
        """
        maj = cls.majEleCandicate(A)
        if cls.majEleCheck(A, maj):
            return maj
        return None

    @classmethod
    def majEleCandicate(cls, A: Vector):
        """获取候选众数
        如果 A 有众数， 则能得到众数， 如果没有， 则返回不是众数。
        数组 A 中长度为 2m 的前缀 P， 若元素 x 在 P 中恰好出现 m 次， 
        则 A 有众数仅当后缀 A-P 拥有众数，且 A-P 的众数就是 A 的众数
        A 有众数 ==> A-P 有众数（必要条件)
        """
        c = 0
        maj = None
        for i in range(A.size()):
            if c == 0:
                maj = A[i]
            else:
                if maj == A[i]:
                    c += 1
                else:
                    c -= 1
        return maj

    @classmethod
    def majEleCheck(self, A: Vector, maj):
        occurence = 0
        for i in range(A.size()):
            if A[i] == maj:
                occurence += 1
        return 2 * occurence > A.size()

    @classmethod
    def trivialMedian(cls, S1: Vector, lo1: int, n1: int, S2: Vector, lo2: int, n2: int):
        """合并两个有序向量， 返回中位数
        S1[lo1, lo1 + n], S2[lo2, lo2 + n] 分别有序
        """
        hi1 = n1 + lo1
        hi2 = n2 + lo2
        S = Vector()
        while lo1 < hi1 and lo2 < hi2:
            while lo1 < hi1 and S1[lo1] <= S2[lo2]:
                S.insert(S.size(), S1[lo1])
                lo1 += 1
            while lo2 < hi2 and S2[lo2] <= S1[lo1]:
                S.insert(S.size(), S2[lo2])
                lo2 += 1
        while lo1 < hi1:
            S.insert(S.size(), S1[lo1])
            lo1 += 1
        while lo2 < hi2:
            S.insert(S.size(), S2[lo2])
            lo2 += 1
        return S[(n1 + n2) // 2]  # 返回中位数

    @classmethod
    def median(cls, S1: Vector, lo1: int, S2: Vector, lo2: int, n: int):
        """求中位数
        S1[lo1, lo1 + n], S2[lo2, lo2 + n] 分别有序
        """
        if n < 3:
            return cls.trivialMedian(S1, lo1, n, S2, lo2, n)
        mi1 = lo1 + n // 2
        mi2 = lo2 + (n - 1) // 2
        if S1[mi1] < S2[mi2]:
            return cls.median(S1, mi1, S2, lo2, n + lo1 - mi1)
        elif S1[mi1] > S2[mi2]:
            return cls.median(S1, lo1, S2, mi2, n + lo2 - mi2)
        else:
            return S1[mi1]
