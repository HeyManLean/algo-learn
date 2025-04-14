# -*- coding: utf-8 -*-


class SegmentNode:
    """线段节点"""
    def __init__(self, start: int, end: int, val: int, left=None, right=None):
        self.start = start
        self.end = end
        self.val = val
        self.left = left  # type:SegmentNode
        self.right = right  # type:SegmentNode


class SegmentTree:
    """线段树（支持单个更新）

    用于高效解决数组的区间查询和区间动态修改问题。

    每个节点维护一个数值范围的聚合值，其子节点的数值范围是当前节点的一半

    建立线段树：
    1. 初始化根节点，是最大范围的线段
    2. 将根节点拆成两边，递归建立线段树，直到左右相等，即个数为1

    更新线段树：
    1. 递归找到对应节点，并将沿途的线段节点的聚合值改为新的左右子树相加
    """
    def __init__(self, start=0, end=100, default=0):
        self.root = SegmentNode(start, end, default)
        self.default = default

    def init_children_node(self, node: SegmentNode):
        """动态更新线段树节点

        当需要操作该节点时，将左右子树都初始化
        """
        if node.start >= node.end:
            return

        mid = node.start + (node.end - node.start) // 2
        if not node.left:
            node.left = SegmentNode(node.start, mid, self.default)
        if not node.right:
            node.right = SegmentNode(mid + 1, node.end, self.default)

    def update(self, index, value):
        self._update(self.root, index, value)

    def _update(self, node: SegmentNode, index, value):
        if node.start == node.end:
            node.val = value
            return

        # 初始化当前递归节点的左右节点
        self.init_children_node(node)

        mid = node.start + (node.end - node.start) // 2
        if index <= mid:
            self._update(node.left, index, value)
        else:
            self._update(node.right, index, value)

        # 将最新值累加到当前节点
        node.val = node.left.val + node.right.val

    # 区间查询：返回区间 [qL, qR] 的聚合值
    def query(self, start, end):
        return self._query(self.root, start, end)

    def _query(self, node: SegmentNode, start, end):
        """二分查找，中途找到在 start,end 区间内的线段树，并返回对应聚合值"""
        if not node:
            return 0

        if node.start >= start and node.end <= end:
            return node.val

        mid = node.start + (node.end - node.start) // 2
        if end <= mid:
            return self._query(node.left, start, end)
        if start > mid:
            return self._query(node.right, start, end)

        return self._query(node.left, start, mid) + self._query(node.right, mid + 1, end)


class NumArray:
    """支持查询范围的和，支持单个更新"""
    def __init__(self, nums: list[int]):
        self.seg_tree = SegmentTree(0, len(nums) - 1)
        for i, num in enumerate(nums):
            self.seg_tree.update(i, num)

    def update(self, index: int, val: int) -> None:
        self.seg_tree.update(index, val)

    # 查询闭区间 [left, right] 的累加和
    def sumRange(self, left: int, right: int) -> int:
        return self.seg_tree.query(left, right)


class RangeSegmentNode:
    def __init__(self, start, end, val=0, left=None, right=None):
        self.start = start
        self.end = end
        self.val = val
        self.left = left  # type:RangeSegmentNode
        self.right = right  # type:RangeSegmentNode
        self.has_assign = False  # 判断是否有值需要往下传递
        self.assign = 0         # 缓存需要向下传递的值


class SumRangeSegmentTree:
    """懒加载线段树（求和）

    更新上级线段树时，先对该范围的上层线段树进行更新，
    并记录更新的值，等到下次要范围下层线段树时，将更新的值传递到下层

    主要用于范围更新和范围取值
    """
    def __init__(self, start=0, end=1000, default=0):
        self.root = RangeSegmentNode(start, end, (end - start + 1) * default)
        self.default = default

    def init_children_node(self, node: RangeSegmentNode):
        if node.start >= node.end:
            return

        mid = node.start + (node.end - node.start) // 2
        if not node.left:
            node.left = RangeSegmentNode(node.start, mid, self.default)
        if not node.right:
            node.right = RangeSegmentNode(mid + 1, node.end, self.default)

    def push_down(self, node: RangeSegmentNode):
        """先把左右节点当前的 assign 下钻，再将当前节点的 assign 同步到左右节点"""
        if not node.has_assign:
            return

        self.init_children_node(node)

        # 一般为覆盖原有的值，不需要将子节点的assign继续往下传递，直接将当前节点assign覆盖
        left = node.left
        right = node.right

        left.val = (left.end - left.start + 1) * node.assign
        left.has_assign = True
        left.assign = node.assign

        right.val = (right.end - right.start + 1) * node.assign
        right.has_assign = True
        right.assign = node.assign

        node.has_assign = False

    def range_update(self, start, end, val):
        return self._range_update(self.root, start, end, val)

    def _range_update(self, node: RangeSegmentNode, start, end, val):
        """更新范围，如果节点范围在需要更新的范围内，则更新节点的值，并设置懒加载数值"""
        if node.start >= start and node.end <= end:
            node.val = (node.end - node.start + 1) * val
            node.has_assign = True
            node.assign = val
            return

        self.init_children_node(node)
        self.push_down(node)

        mid = node.start + (node.end - node.start) // 2
        if end <= mid:
            self._range_update(node.left, start, end, val)
        elif start > mid:
            self._range_update(node.right, start, end, val)
        else:
            self._range_update(node.left, start, mid, val)
            self._range_update(node.right, mid + 1, end, val)

        # 当前节点的值
        node.val = node.left.val + node.right.val


    def query(self, start, end):
        return self._query(self.root, start, end)

    def _query(self, node: RangeSegmentNode, start, end):
        """对node的值进行二分，判断区域左右进行递归"""
        if start > end:
            return 0

        # 如果目标区间包含了当前区间，则返回当前区间的值
        if start <= node.start and end >= node.end:
            return node.val

        self.init_children_node(node)
        self.push_down(node)

        mid = node.start + (node.end - node.start) // 2
        if end <= mid:
            return self._query(node.left, start, end)
        if start > mid:
            return self._query(node.right, start, end)

        return self._query(node.left, start, mid) + self._query(node.right, mid + 1, end)


class MyCalendar:

    def __init__(self):
        self.seg_tree = SumRangeSegmentTree(0, 10 ** 9, 0)

    def book(self, startTime: int, endTime: int) -> bool:
        if startTime >= endTime:
            return False

        print(startTime, endTime, self.seg_tree.query(startTime, endTime - 1))

        if self.seg_tree.query(startTime, endTime - 1) > 0:
            return False

        self.seg_tree.range_update(startTime, endTime - 1, 1)
        return True


if __name__ == '__main__':
    numArray = NumArray([1, 3, 5])
    assert numArray.sumRange(0, 2) == 9     # 返回 1 + 3 + 5 = 9
    numArray.update(1, 2)                   # nums = [1,2,5]
    assert numArray.sumRange(0, 2) == 8     # 返回 1 + 2 + 5 = 8

    calendar = MyCalendar()
    books = [[0, 0], [10, 20], [15, 25], [20, 30]]
    results = [False, True, False, True]
    for i, book in enumerate(books):
        result = calendar.book(book[0], book[1])
        print(result, book, results[i])
        assert result == results[i]

    print("OK")
