# coding=utf-8

from BinTree import BinNodePosi, BinNode, stature, RBColor, IsRoot, \
    uncle, IsLChild, IsRChild, SetFromParentTo, HasLChild, HasRChild
from BinSearchTree import BST


def IsBlack(p: BinNodePosi):
    return p is not None or p.color == RBColor.RB_BLACK.value


def IsRed(p: BinNodePosi):
    return not IsBlack(p)


def BlackHeightUpdated(x: BinNodePosi):
    """红黑树更新高度条件"""
    if stature(x.lc) != stature(x.rc):  # 左右子树高度相等
        return False
    if IsRed(x):
        return x.height == stature(x.lc)  # 红色高度等于左右子树（黑色）高度， 黑色才算高度
    else:
        return x.height == stature(x.lc) + 1  # 黑色高度等于左右子树高度加上自身 1


class RedBlack(BST):
    """红黑树， 如果红色节点向上提升到黑色父节点两边， 则成为一个4阶B树。
    也是一种BST， 但必须满足以下条件:
    1. 树根始终为黑色；
    2. 外部节点均为黑色（None节点）；
    3. 其余节点若为红色， 则其孩子节点必为黑色（如果有父节点， 父节点也必为黑色）；
    4. 从任一外部节点到根节点的沿途， 黑色节点的数目相等（除去外部节点， 这个数目成为黑高度）。
    """

    def _updateHeight(self, x: BinNodePosi):
        x.height = max(stature(x.lc), stature(x.rc))
        if IsBlack(x):
            x.height += 1
        return x.height

    def insert(self, e):
        x = self.search(e)
        if x is not None:
            return x
        x = BinNode(e, self._hot, None, None, -1)
        if e < self._hot.data:
            self._hot.lc = x
        else:
            self._hot.rc = x
        self._size += 1
        self.solveDoubleRed(x)
        return x

    def solveDoubleRed(self, v: BinNodePosi):
        if IsRoot(v):
            v.color = RBColor.RB_BLACK.value
            v.height += 1
            return
        p = v.parent
        if IsBlack(p):
            return
        # p 为红色， 说明出现双红
        g = p.parent  # 因为根节点必黑， p 为红即不是根节点， 所以 p 的父节点 g 一定存在
        u = uncle(v)

        # uncle 节点空或黑色， 需要旋转（3 + 4重构), 修改颜色两边红， 中间黑
        if IsBlack(u):
            # p 和 v 同侧, 则 v < p < g 或 g < p < v, zig-zig或zag-zag
            if IsLChild(v) == IsLChild(p):
                p.color = RBColor.RB_BLACK.value
            else:  # p 和 v 不同侧， 则 p < v < g 或者 g < v < p, zig-zag或zag-zig
                v.color = RBColor.RB_BLACK.value
            g.color = RBColor.RB_RED.value

            gg = g.parent
            isLChild = IsLChild(g)

            r = self.rotateAt(v)
            r.parent = gg

            if gg is not None:
                if isLChild:
                    gg.lc = r
                else:
                    gg.rc = r
            return
        else:  # uncle 节点为红色， 则只需将 p 和 u 颜色改黑色， g该红色（如果是根节点不修改）即可
            p.color = RBColor.RB_BLACK.value
            p.height += 1  # 黑高度 + 1
            u.color = RBColor.RB_BLACK.value
            u.height += 1
            if not IsRoot(g):
                g.color = RBColor.RB_RED.value
            self.solveDoubleRed(g)  # g 置于红色可能上层会形成双红情况， 需要递归往上处理

    def remove(self, e):
        x = self.search(e)
        if x is None:
            return False
        r = self._removeAt(x)
        self._size -= 1
        if self._size == 0:  # 节点为空
            return True
        if self._hot is None:  # hot为空， 说明删除的是根节点， 需要将根节点置黑色
            self._root.color = RBColor.RB_BLACK.value
            self._updateHeight(self._root)
            return True
        if BlackHeightUpdated(self._hot):  # 黑深度平衡
            return True

        if IsRed(r):  # 删除节点和其后继节点（其中一个为红色）， 保持黑色即可
            r.color = RBColor.RB_BLACK.value
            r.height += 1
            return True
        # 删除节点和其后继节点都为黑色
        self.solveDoubleBlack(r)
        return True

    def solveDoubleBlack(self, r: BinNodePosi):
        """调整过程是：
        先提升所有红节点， 形成等价 4 阶 B 树， 考虑节点的下溢情况， 
        以 B 树处理方式处理得出最终的 B 树结构， 再将最终的B树转换成红黑树，
        以最后的红黑树调整节点。
        """
        if r is not None:
            p = r.parent
        else:
            p = self._hot
        if p is None:
            return
        if r == p.lc:
            s = p.rc
        else:
            s = p.lc

        if IsBlack(s):  # 删除节点x/r 兄弟节点 s 为黑色， 向兄弟节点 s 借关键码
            t = None
            if IsRed(s.rc):
                t = s.rc
            if IsRed(s.lc):
                t = s.lc
            # 第一种情况： s至少有一个孩子为红色节点， BB-1
            if t is not None:
                oldColor = p.color
                b = self.rotateAt(t)
                SetFromParentTo(p, b)

                if HasLChild(b):
                    b.lc.color = RBColor.RB_BLACK.value
                    self._updateHeight(b.lc)
                if HasRChild(b):
                    b.rc.color = RBColor.RB_BLACK.value
                    self._updateHeight(b.rc)
                b.color = oldColor
                self._updateHeight(b)
            else:
                s.color = RBColor.RB_RED.value
                s.height -= 1

                # 第二种情况： s的孩子都为黑色节点， p为红色， BB-2R
                if IsRed(p):
                    p.color = RBColor.RB_BLACK.value
                else:  # 第三种情况： s的孩子都为黑色节点， p为红色， BB-2R
                    p.height -= 1
                    self.solveDoubleBlack(p)
        else:  # 第四种情况， s 为红色， BB-3
            s.color = RBColor.RB_BLACK.value
            p.color = RBColor.RB_RED.value
            if IsLChild(s):
                t = s.lc
            else:
                t = s.rc
            self._hot = p
            SetFromParentTo(p, self.rotateAt(t))
            self.solveDoubleBlack(r)
