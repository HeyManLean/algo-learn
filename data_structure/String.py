# coding=utf-8


class String:
    @staticmethod
    def bruteForceMatch(P: str, T: str):
        """字符串蛮力匹配O(n * m)
        P: 模式字符串
        T: 文本字符串
        >>> ============================
        P = 'aabb'
        T = '1234aab1234aabb1'
        r = String.bruteForceMatch('aabb', '1234aab1234aabb1')
        print(r)
        if r != -1:
            print(T[r:r+len(P)])
        =================================
        11
        aabb
        =================================
        """
        n = len(T)
        m = len(P)
        for i in range(0, n - m + 1):
            for j in range(0, m):
                if P[j] != T[i + j]:
                    break
            else:
                return i
        return -1

    @classmethod
    def KMPMatch(cls, P: str, T: str):
        """KMP算法 O(n + m)
        >>> ============================
        P = 'aabb'
        T = '1234aab1234aabb1'
        r = String.KMPMatch('aabb', '1234aab1234aabb1')
        print(r)
        if r != -1:
            print(T[r:r+len(P)])
        =================================
        11
        aabb
        =================================
        """
        pNext = cls.buildNext(P)
        n = len(T)
        m = len(P)
        i = 0
        j = 0
        while i < n and j < m:
            if j < 0 or T[i] == P[j]:
                i += 1
                j += 1
            else:
                j = pNext[j]
        if i == n:
            return -1
        return i - j

    @classmethod
    def buildNext(cls, P: str):
        """生成 KMP next 数组, 快速后移 O(m)
        当 j 处匹配不成功时, 移到 t 处继续匹配, 以此类推. t 应该尽可能的大, 才安全.
            pNext[j] = max( { 0 <= t < j | P[0, t) = P[j - t, j) } )
        T: ^==================| T[i] |========================$
        P:           ^========| P[j] |=====$
        T[i] != P[j] 时, 需要回溯到 t = pNext[j], 用 P[t] 跟 T[i] 继续匹配.
        -1 代表前面的 T 和 P 都匹配不成功, 需要 T 前进一步, P 重新匹配.
        ********************************************************
        pNext 例子:
        ---------------------------------------------
        rank | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
        ---------------------------------------------
         P[] | C | H | I | N | C | H | I | L | L | A
        ---------------------------------------------
        pNext| -1| 0 | 0 | 0 | 0 | 1 | 2 | 3 | 0 | 0
        ---------------------------------------------

        也可将 pNext 理解为有 t 个字符匹配, 0到t-1, 则下一个需要从t继续匹配.
        1. t = pNext[j]
        2. pNext[j + 1] <= t + 1, 当 P[j] = P[t] 取等号
            pNext[j] 表示 [0, t-1] ==> [j - t, j - 1]
            pNext[j + 1] 表示 [0, t] ==> [j - t, j] 即 P[j] = P[t], P[j - 1] = P[t - 1]....
        """
        m = len(P)
        pNext = [0 for _ in range(m)]
        pNext[0] = -1

        j = 0
        t = -1

        # 求 j + 1 的 pNext 值
        while j < m - 1:
            if t < 0 or P[j] == P[t]:
                t += 1
                j += 1
                # pNext[j] = t  # pNext[j + 1] = t + 1, 当 t 为 -1 时, 将 pNext[j + 1] 设为 0 既可以
                if P[j] != P[t]:  # 下一个匹配字符不能与 j 字符相等
                    pNext[j] = t
                else:  # 否则, 从 pNext[t] 匹配, 即 t 不匹配, 查找 t 的回溯.
                    pNext[j] = pNext[t]
            else:
                t = pNext[t]
        return pNext
