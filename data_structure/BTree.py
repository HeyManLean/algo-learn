# coding=utf-8

from Vector import Vector


class BTNode:
    """B 树节点
    存着很多关键码： key
    像搜索树一样形成分支： child(保存很多节点)
    """

    def __init__(self, e=None, lc=None, rc=None):
        self.parent = None
        self.key = Vector()
        self.child = Vector()  # child = key + 1

        if e is not None:
            self.key.insert(0, e)
            self.child.insert(0, lc)
            self.child.insert(1, rc)
            if lc is not None:
                lc.parent = self
            if rc is not None:
                rc.parent = self
        else:
            self.child.insert(0, None)


BTNodePosi = BTNode


class BTree:
    """
    m 阶 B 树的每个超级节点分支数取值范围： [ceiling(m/2), m];
    每个超级节点包含的关键码 [ceiling(m/2) - 1, m - 1];
    只需看分支符合要求， 关键必符合要求
    所谓搜索是搜索关键码， 即一个超级节点上的其中一个关键码
    """

    def __init__(self, order=3):
        self._size = 0
        self._order = order  # 阶数
        self._root = BTNode()
        self._hot = None

    def order(self):
        return self._order

    def size(self):
        return self._size

    def root(self):
        return self._root

    def empty(self):
        return self._root is None

    def search(self, e):
        """搜索 e, 返回所在节点"""
        v = self._root
        self._hot = None
        while v is not None:
            r = v.key.search(e)
            if 0 <= r and e == v.key[r]:
                return v
            self._hot = v
            v = v.child[r + 1]
        return None

    def insert(self, e):
        v = self.search(e)
        if v is not None:
            return False
        r = self._hot.key.search(e)
        self._hot.key.insert(r + 1, e)
        self._hot.child.insert(r + 2, None)
        self._size += 1
        self.solveOverflow(self._hot)
        return True

    def solveOverflow(self, v: BTNodePosi):
        """插入关键码有可能导致上溢"""
        if self._order >= v.child.size():  # 分支不超过 B 树阶数 m， 不发生上溢
            return False
        s = self.order // 2  # 即 floor（m/2）， 此时 _order = v.key.size() = v.child.size() - 1
        # 0--s 关键码分裂成左侧新节点， 余下的 (s + 1)--(_order - 1) 关键码形成右侧节点， s 的关键码插入到父节点去
        u = BTNode()

        # s + 1 -- order - 1关键码分裂成右节点， 即共有 (_order - 1) - （s + 1） + 1 = _order - s - 1个, child 有 _order - s 个
        for j in range(0, self._order - s - 1):
            u.key.insert(j, v.key.remove(s + 1))  # s + 1 即右侧第一个, 循环即可
            u.child.insert(j, v.child.remove(s + 1))
        # child 比 key 多 1 个要处理
        u.child[self._order - s - 1] = v.child.remove(s + 1)

        # child 对应的节点 parent 修改值
        if u.child[0] is not None:
            for j in range(0, self._order - s):
                u.child[j].parent = u

        p = v.parent

        # 根节点溢出特殊处理, 需要创建一个新节点作为新的根节点
        if p is None:
            # 新的根节点与左节点连接
            p = BTNode()
            p.child[0] = v
            v.parent = p

        # 将 s 关键码插入到父节点 p 上
        r = p.key.search(v.key[0]) + 1
        p.key.insert(r, v.key.remove(s))
        p.child.insert(r + 1, u)
        u.parent = p
        self.solveOverflow(p)

    def remove(self, e):
        v = self.search(e)
        if v is None:
            return False
        r = v.key.search(e)
        if v.child[0] is not None:  # 非叶子节点
            # 找到直接后继节点， 然后替换关键码, 即转移成叶子节点
            u = v.child[r + 1]
            while u.child[0] is not None:
                u = u.child[0]
            v.key[r] = u.key[0]
            v = u
            r = 0
        v.key.remove(r)
        v.child.remove(r + 1)
        self._size -= 1
        self.solveUnderFlow(v)
        return True

    def solveUnderFlow(self, v: BTNodePosi):
        """关键码删除有可能导致下溢"""
        if (self._order + 1) // 2 <= v.child.size():
            return False
        p = v.parent
        if p is None:  # 递归基
            # 树根 v 已不含关键码， 但右唯一的非空孩子， 因为合并，导致根部的这种情况发生
            if not v.key.size() and v.child[0] is not None:
                self._root = v.child[0]
                self._root.parent = None
                v.child[0] = None
                del v
            return True

        r = 0
        while p.child[r] != v:
            r += 1

        # 情况一, 向左兄弟借关键码
        if 0 < r:  # 不是第一个孩子， 说明有左兄弟
            ls = p.child[r - 1]
            if (self._order + 1) // 2 < ls.child.size():
                # 旋转， 父节点对应位置的关键码放到 v 去， 左兄弟借到的(最后一个)关键码放到父节点去
                v.key.insert(0, p.key[r - 1])
                p.key[r - 1] = ls.key.remove(ls.key.size() - 1)
                v.child.insert(0, ls.child.remove(ls.child.size() - 1))
                if v.child[0] is not None:
                    v.child[0].parent = v
                return True

        # 情况二， 向右兄弟借关键码
        if p.child.size() - 1 > r:  # 不是最后一个孩子， 说明有右兄弟
            rs = p.child[r + 1]
            if (self._order + 1) // 2 < rs.child.size():
                v.key.insert(v.key.size(), p.key[r])
                p.key[r] = rs.key.remove(0)
                v.child.insert(v.child.size(), rs.child.remove(0))
                if v.child[v.child.size() - 1] is not None:
                    v.child[v.child.size() - 1].parent = v
                return True

        # 情况三， 左右兄弟要不为空（不能同时为空， 因为阶必大于等于2， 所以分支必然有两个或以上)， 要不太瘦(分支刚好 (order + 1) // 2), 可以考虑合并

        # 跟左兄弟合并， 父节点对应关键码移到下层作为连接关键码，连接左兄弟节点和 v
        if 0 < r:
            ls = p.child[r - 1]
            ls.insert(ls.key.size(), p.key.remove(r - 1))
            p.child.remove(r)  # 即 v
            ls.child.insert(ls.child.size(), v.child.remove(0))
            if ls.child[ls.child.size() - 1] is not None:
                ls.child[ls.child.size() - 1].parent = ls
            while not v.key.empty():
                ls.key.insert(ls.key.size(), v.key.remove(0))
                ls.child.insert(ls.child.size(), v.child.remove(0))
                if ls.child[ls.child.size() - 1] is not None:
                    ls.child[ls.child.size() - 1].parent = ls
            del v
        else:  # 跟右兄弟合并
            rs = p.child[r + 1]
            rs.insert(0, p.key.remove(r))
            p.child.remove(r)
            rs.child.insert(0, v.child.remove(v.child.size() - 1))
            if rs.child[0] is not None:
                rs.child[0].parent = rs
            while not v.key.empty():
                rs.key.insert(0, v.key.remove(v.key.size() - 1))
                rs.child.insert(0, v.child.remove(v.child.size() - 1))
                if rs.child[0] is not None:
                    rs.child[0].parent = rs
            del v

        self.solveUnderFlow(p)
        return True
