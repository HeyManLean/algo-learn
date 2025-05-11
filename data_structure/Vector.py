# coding=utf-8
"""
向量
"""
import array
# import reprlib
import numbers
import random


DEFAULT_CAPACITY = 3


class Vector:
    # protected ========================================================
    def _copyFrom(self, A, lo, hi, type='I'):
        self._capacity = (hi - lo) * 2
        self._elem = [0] * self._capacity
        self._size = 0
        while lo < hi:
            self._elem[self._size] = A[lo]
            self._size += 1
            lo += 1

    def _expand(self):
        # 如果元素个数超过容量， 扩容
        if self._size < self._capacity:
            return
        if self._capacity < DEFAULT_CAPACITY:
            self._capacity = DEFAULT_CAPACITY
        self._capacity *= 2
        oldElem = self._elem
        self._elem = [0] * self._capacity
        for i in range(self._size):
            self._elem[i] = oldElem[i]
        del oldElem

    def _shrink(self):
        # 容量不能少于默认最低容量的一半（缩小时为默认最低容量的1/4)
        if self._capacity < DEFAULT_CAPACITY * 2:
            return
        # 如果元素总数小于容量的1/4，则缩小
        if self._size * 4 > self._capacity:
            return
        self._capacity //= 2
        oldElem = self._elem
        self._elem = [0] * self._capacity
        for i in range(self._size):
            self._elem[i] = oldElem[i]
        del oldElem

    def _partition(self, lo, hi):
        pass

    # public ==========================================================
    def __init__(self, *, c=DEFAULT_CAPACITY, s=0, v=0, A=None, lo=0, hi=None):
        """
        Usage:
            vect = Vector(c=10)
            vect = Vector(c=10, s=2, v=1)
            vect = Vector(A=[1, 2, 3, 4])
            vect = Vector(A=[1, 2, 3, 4], lo=1, hi=3)
            vect = Vector(A=Vector(c=10))
        """
        self._capacity = 0
        self._size = 0
        self._elem = None

        if A is not None:
            if hi is None:
                hi = len(A)
            self._capacity = hi - lo
            self._elem = [0] * self._capacity
            self._copyFrom(A, lo, hi)
        else:
            self._capacity = c
            self._elem = [0] * self._capacity
        while self._size < s:
            self._elem[self._size] = v
            self._size += 1

    def __repr__(self):
        return '<Vector({})>'.format(list(self))

    def __del__(self):
        # Not Required!
        del self._elem

    def __iter__(self):
        return (self._elem[i] for i in range(self._size))

    def __len__(self):
        """执行 setitem 时会先获取 len， 判断 index 是否有效"""
        return self._size

    def __getitem__(self, r):
        cls = type(self)
        if isinstance(r, slice):
            return cls(A=self._elem[r])
        elif isinstance(r, numbers.Integral):
            return self._elem[r]
        else:
            msg = '{cls.__name__} indices must be integers'.format(cls=cls)
            raise TypeError(msg)

    def __setitem__(self, r, e):
        self._elem[r] = e

    def __lt__(self, v):
        """重载 '<' """
        cls = type(self)
        v_cls = type(v)
        if cls != v_cls:
            msg = 'unorderable types: {cls.__name__}() < {v_cls.__name__}()'.format(
                cls=cls, v_cls=v_cls)
            raise TypeError(msg)
        i = self._size
        j = len(v)
        k = 0
        while k < i and k < j:
            if self._elem[k] > v[k]:
                return False
            elif self._elem[k] < v[k]:
                return True
            else:
                continue
        return i < j

    #
    # TODO operator:=
    #

    def size(self):
        return self._size

    def empty(self):
        return self._size == 0

    def disordered(self):
        """判断是否有序, 返回相邻逆序数目"""
        n = 0
        for i in range(1, self._size):
            if self._elem[i] < self._elem[i - 1]:
                n += 1
        return n

    def find(self, e, lo=0, hi=None):
        """无序查找"""
        if hi is None:
            hi = self._size
        while hi > lo:
            hi -= 1
            if self._elem[hi] == e:
                return hi
        return hi - 1

    def _binSearch1(self, e, lo, hi):
        while lo < hi:
            mi = (hi + lo) // 2
            if e < self._elem[mi]:
                hi = mi
            elif self._elem[mi] > e:
                lo = mi + 1
            else:
                return mi
        return -1

    def _binSearch2(self, e, lo, hi):
        """如果e在位置0, hi > lo 会死循环"""
        while 1 < hi - lo:
            mi = (hi + lo) // 2
            if e < self._elem[mi]:
                hi = mi
            else:
                lo = mi
        return lo if e == self._elem[lo] else -1

    def _binSearch3(self, e, lo, hi):
        while lo < hi:
            mi = (hi + lo) // 2
            if e < self._elem[mi]:
                hi = mi
            else:
                lo = mi + 1
        lo -= 1
        return lo

    def search(self, e, lo=0, hi=None):
        """有序向量查找"""
        if hi is None:
            hi = self._size
        return self._binSearch1(e, lo, hi)

    def _remove(self, lo, hi):
        while hi < self._size:
            self._elem[lo] = self._elem[hi]
            lo += 1
            hi += 1
        self._size = lo
        self._shrink()

    def remove(self, lo, hi=None):
        if hi is None:
            e = self._elem[lo]
            self._remove(lo, lo + 1)
            return e
        else:
            self._remove(lo, hi)
            return hi - lo

    def insert(self, r, e):
        """
        r: index
        e: value
        """
        self._expand()
        hi = self._size
        while r < hi:
            self._elem[hi] = self._elem[hi - 1]
            hi -= 1
        self._elem[hi] = e
        self._size += 1

    def _bubble(self, lo, hi):
        sorted = True
        # for lo in range(lo + 1, hi):
        lo += 1
        while lo < hi:
            if self._elem[lo] < self._elem[lo - 1]:
                self._elem[lo], self._elem[lo - 1] = self._elem[lo - 1], self._elem[lo]
                sorted = False
            lo += 1
        return sorted

    def _bubbleSort(self, lo, hi):
        """冒泡排序
        每次比较直接交换元素不需要额外空间存储元素值， 而选择排序是先比较但不交换， 记录目前最值， 遍历结束后再交换一次
        """
        while not self._bubble(lo, hi):
            hi -= 1

    def _max(self, lo, hi):
        # return max(self._elem[lo:hi])
        hi -= 1
        e = self._elem[hi]
        while lo < hi:
            hi -= 1
            if e < self._elem[hi]:
                e = self._elem[hi]
        return e

    def _selectionSort(self, lo, hi):
        """选择排序"""
        while lo < hi:
            j = lo
            for i in range(lo + 1, hi):
                if self._elem[j] < self._elem[i]:
                    j = i
            hi -= 1
            self._elem[hi], self._elem[j] = self._elem[j], self._elem[hi]

    def _merge(self, lo, mi, hi):
        """需要额外空间"""
        B = [0] * (mi - lo)
        lb = 0
        for i in range(lo, mi):
            B[lb] = self._elem[i]
            lb += 1
        i = 0
        while i < lb and mi < hi:
            if B[i] <= self._elem[mi]:
                self._elem[lo] = B[i]
                i += 1
            else:
                self._elem[lo] = self._elem[mi]
                mi += 1
            lo += 1
        if i < lb:
            for j in range(i, lb):
                self._elem[lo] = B[j]
                lo += 1
        del B

    def _mergeSort(self, lo, hi):
        """合并排序"""
        if hi - lo < 2:  # 只有一个元素
            return
        mi = (lo + hi) // 2
        self._mergeSort(lo, mi)
        self._mergeSort(mi, hi)
        self._merge(lo, mi, hi)

    def _quickSort(self, lo, hi):
        """快速排序
        >>> vect = Vector(A=[90, 1, 3, 5, 55, 12, 34, 33])
        >>> vect._quickSort(0, vect.size())
        <Vector([1, 3, 5, 12, 33, 34, 55, 90])>
        """
        if hi - lo < 2:  # 单个元素有序
            return
        mi = self._partition(lo, hi - 1)  # 在 [lo, hi-1] 中构造轴点
        self._quickSort(lo, mi)
        self._quickSort(mi + 1, hi)  # mi 的位置已到位

    def _partition(self, lo, hi):
        """快速排序，构造轴点
        取值范围： [lo, hi]
        选取 lo 对应元素 m = elem[lo] 作为候选轴点， 最终达到：
            - lo = hi = index(m)
            - 0 < x < index(m), elem[x] <= m, 左边元素都小于 m
            - index(m) < x < elem.size, elem[x] > m， 右边元素都大于 m
        步骤：
            m = elem[lo]， 此时 elem[lo] 腾出， 用于其他元素调整
            进入循环
            - hi-- 向中间靠拢， 直到遇到小于 m 的值（不满足要求）
                - elem[lo] = elem[hi]
            - lo++ 向中间靠拢， 直到遇到大于 m 的值（不满足要求）
                - elem[hi] = elem[lo]， 那么lo 和 hi 都又满足要求了（相当于借助腾出的单元用于交换元素）
            - 以此类推， 循环上面步骤， 直到 lo = hi 时退出循环
            将 m 值放回腾出的单元中
            返回 lo
        """
        m = self._elem[lo]  # 任意取一轴点
        while lo < hi:
            # while lo < hi and self._elem[hi] >= m:
            #     hi -= 1
            # self._elem[lo] = self._elem[hi]
            # while lo < hi and self._elem[lo] <= m:
            #     lo += 1
            # self._elem[hi] = self._elem[lo]  # 于是， 此时的 elem[lo] 又是腾出的值（无效值）

            # 改进方案
            while lo < hi:
                if self._elem[hi] >= m:
                    hi -= 1
                else:
                    self._elem[lo] = self._elem[hi]
                    lo += 1
                    break
            while lo < hi:
                if self._elem[lo] <= m:
                    lo += 1
                else:
                    self._elem[hi] = self._elem[lo]
                    hi -= 1
                    break
        self._elem[lo] = m
        return lo

    def _heapSort(self, lo, hi):
        pass

    def sort(self, lo=0, hi=None):
        """排序"""
        if hi is None:
            hi = self._size
        rand = random.randint(0, 3)
        if rand == 0:
            self._bubbleSort(lo, hi)
        elif rand == 1:
            self._selectionSort(lo, hi)
        elif rand == 2:
            self._mergeSort(lo, hi)
        elif rand == 3:
            self._quickSort(lo, hi)
        else:
            self._heapSort(lo, hi)  # 未实现

    def unsort(self, lo=0, hi=None):
        """乱序"""
        if hi is None:
            hi = self._size
        while hi > lo:
            hi -= 1
            rand = random.randint(lo, hi)
            self._elem[hi], self._elem[rand] = self._elem[rand], self._elem[hi]

    def deduplicate(self):
        """无序向量去重"""
        oldSize = self._size
        for i in range(self._size):
            if self.find(self._elem[i], 0, i) > 0:
                self.remove(i)
        return oldSize - self._size

    def uniquify(self):
        """有序向量去重
        双指针， i用于设置当前不重复（有效）值， j用于遍历所有元素， 当发现有不同值时， 添加并使i向前一步
        """
        i, j = 0, 1
        while j < self._size:
            if self._elem[i] != self._elem[j]:
                i += 1
                self._elem[i] = self._elem[j]
            j += 1
        self._size = i + 1
        self._shrink()
        return j - i

    def traverse(self, func):
        for i in range(self._size):
            func(self._elem[i])


if __name__ == '__main__':
    vect = Vector(c=10)
    print(vect)
    vect = Vector(c=10, s=2, v=1)
    print(vect)
    vect = Vector(A=[1, 2, 3, 4])
    print(vect.search(4))
    vect.unsort()
    vect.remove(1, 3)
    vect.insert(0, 100)
    print(vect.find(2))
    print(vect)
    print(vect.disordered())
    vect = Vector(A=[1, 2, 3, 4], lo=1, hi=3)
    print(vect)
    vect = Vector(A=Vector(c=10, s=2))
    print(vect)
    vect = vect[1:50:2]
    print(vect)
    print(vect < Vector(A=[1, 2, 3, 4]))
    # print(vect < [1, 2, 3, 4])

    vect = Vector(A=[90, 1, 3, 5, 55, 12, 34, 33])
    vect._quickSort(0, vect.size())
    print(vect)