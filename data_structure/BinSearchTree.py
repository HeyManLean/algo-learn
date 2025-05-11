# coding=utf-8

from BinTree import BinNodePosi, BinTree, HasLChild,\
    HasRChild, HasParent, IsRChild, IsLChild, release, \
    stature, SetFromParentTo, BinNode


class BST(BinTree):
    """
    a = BST()
    b = []
    b.append(a.insertAsRoot(10))
    b.append(a.insert(4))
    b.append(a.insert(13))
    b.append(a.insert(16))
    b.append(a.insert(28))
    print('height--data--parent--lc--rc')
    for i in b:
        print(i.height, i.data, i.parent.data if i.parent else None, i.lc.data if i.lc else None, i.rc.data if i.rc else None)
    print("before remove===================")
    a.travIn()
    a.remove(16)
    print("after remove====================")
    a.travIn()

    ===============================
    height--data--parent--lc--rc
    3 10 None 4 13
    0 4 10 None None
    2 13 10 None 16
    1 16 13 None 28
    0 28 16 None None
    before remove===================
    4
    10
    13
    16
    28
    after remove====================
    4
    10
    13
    28
    """
    @property
    def hot(self):
        """搜索有效或无效（是否查询到结果节点）时，保存搜索结果的父节点（必为节点）。"""
        if not hasattr(self, '_hot'):
            self._hot = None
        return self._hot

    @hot.setter
    def hot(self, value):
        self._hot = value

    def _searchIn(self, v: BinNodePosi, e):
        if v is None or e == v.data:
            return v
        self.hot = v
        if e < v.data:
            v = v.lc
        else:
            v = v.rc
        return self._searchIn(v, e)

    def search(self, e):
        return self._searchIn(self.root(), e)

    def insert(self, e):
        """插入节点
        如果查不到数据为e的节点，那就将新节点插到查询最后保留的父节点后面。
        """
        x = self.search(e)
        if x is None:
            if e < self.hot.data:
                x = self.insertAsLC(self.hot, e)
            else:
                x = self.insertAsRC(self.hot, e)
        return x

    def remove(self, e):
        x = self.search(e)
        if x is None:
            return False
        self._removeAt(x)
        self._size -= 1
        self._updateHeightAbove(self.hot)
        return True

    def _removeAt(self, x: BinNodePosi):
        """利用中序遍历的方式，将x与其直接后继交换, 将其后继节点删除"""
        w = x  # w 为被删除节点
        succ = None
        if not HasLChild(x):
            succ = x.rc
            if HasParent(x):
                xParent = x.parent
                if IsLChild(x):
                    xParent.lc = succ
                else:
                    xParent.rc = succ
        elif not HasRChild(x):
            succ = x.rc
            if HasParent(x):
                xParent = x.parent
                if IsLChild(x):
                    xParent.lc = succ
                else:
                    xParent.rc = succ
        else:  # x 有左右子树
            w = self.getSucc(w)  # 在右子树中找到直接后继
            x.data, w.data = w.data, x.data
            # x 和 w 交换数据后，需要删除 w 节点
            u = w.parent
            if u == x:  # 说明 w 为 x 的右子节点， 且 w 没有左子树
                u.rc = succ = w.rc
            else:  # 说明 w 为 x 的右子树的左子树的最左节点（即无左节点）， 所以无论那种情况， 只需处理 w 的右子树（右子节点）。
                u.lc = succ = w.rc  # 左侧节点 w 比 w 的父节点小， 其右子树放在父节点左子节点（类似链表移除节点， 指针越位即可）
        self.hot = w.parent
        if succ is not None:
            succ.parent = self.hot
        release(w)
        return succ
    
    def _connect34(self, a, b, c, T0, T1, T2, T3):
        """拆散重组所有涉及重平衡的节点， 重新连接三个用于旋转的顶点成以下统一重新平衡结构
        a|b|c: 大小顺序为 a < b < c的三个节点
        T0|T1|T2|T3 为分别为各个连接三个节点的子树的根节点
                b
                |
            ---------
            |       |    
            a       c
        -------- --------
        |      | |      |
        T0     T1 T2     T3
        """
        a.lc = T0
        if T0 is not None:
            T0.parent = a
        a.rc = T1
        if T1 is not None:
            T1.parent = a
        self._updateHeight(a)

        c.lc = T2
        if T2 is not None:
            T2.parent = c
        c.rc = T3
        if T3 is not None:
            T3.parent = c
        self._updateHeight(c)

        b.lc = a
        a.parent = b
        b.rc = c
        c.parent = b
        self._updateHeight(b)
        return b  # 返回新子树（结构）的根节点
    
    def rotateAt(self, v):
        """节点旋转， 处理失衡节点， v 为失衡节点的孙子， 可以通过 parent 获取失衡节点孩子 p 和失衡节点 g。
        失衡情况下， g, v, p 的相对位置有四种情况， 且每一种情况对 T0-3 子树的划分会不同
        g 为最低失衡节点， 即最往下的左右子树高度差超过2的， p 为较高子树的根节点， 同理 v 为 p较高子树的根节点
        zig: 需要顺时针旋转
        zag: 需要逆时针旋转
        旋转对象固定， 先旋转 p， 后旋转 g。 
        zig-zig 只需旋转一次， 而 zig-zag 需要旋转2次。
        1: zig-zig, 左左形式， 即 p 为 g 的左子节点， v 为 p 的右子节点
                    g               
                    |               
                ---------              
                |       |    
                p       T3
            -------- 
            |      | 
            v     T2
            |
        ---------
        |       |
        T0     T1
        2： zag-zig, 左右形式, 先zag p 后 zig g
                  g               
                  |               
            ------------              
            |           |    
            p           T3
        -------- 
        |      | 
        T0      v    
                |
            --------
            |      |
            T1    T2
        3： zag-zag, 右右形式
                g               
                |               
            ---------              
            |       |   
           T0       p
                -------- 
                |      | 
                T1      v    
                        |
                    --------
                    |      |
                    T2    T3
        4: zig-zag, 右左形式
              g               
              |               
        -------------             
        |           |    
        T0          p 
                    | 
                --------
                |       |
                v       T3
                |
            -------
            |     |
            T1   T2
        """
        p = v.parent  # 失衡节点的孩子
        g = p.parent  # 失衡孩子
        if IsLChild(p):
            if IsLChild(v):  # zig-zig
                # 只需确定 v， p， g的大小顺序和 T0-3的位置带入connect34即可
                # 中间的作为新子树的根结点连接到 g 的父节点去
                p.parent = g.parent
                SetFromParentTo(g, p)
                return self._connect34(v, p, g, v.lc, v.rc, p.rc, g.rc)
            else:  # zig-zag
                v.parent = g.parent
                SetFromParentTo(g, v)
                return self._connect34(p, v, g, p.lc, v.lc, v.rc, g.rc)
        else:
            if IsRChild(v):  # zag-zag
                p.parent = g.parent
                SetFromParentTo(g, p)
                return self._connect34(g, p, v, g.lc, p.lc, v.lc, v.rc)
            else:  # zag-zig
                v.parent = g.parent
                SetFromParentTo(g, v)
                return self._connect34(g, v, p, g.lc, v.lc, v.rc, g.rc)


class AVL(BST):
    """AVL自平衡二叉搜索树
        a = AVL()
        b = []
        b.append(a.insertAsRoot(10))
        b.append(a.insert(4))
        b.append(a.insert(13))
        b.append(a.insert(16))
        b.append(a.insert(28))
        print('data--height--parent--lc--rc')
        for i in b:
            print(i.data, i.height, i.parent.data if i.parent else None, i.lc.data if i.lc else None, i.rc.data if i.rc else None)
        print("before remove===================")
        a.travIn()
        a.remove(16)
        print("after remove====================")
        a.travIn()
        =================================================
        data--height--parent--lc--rc
        10 2 None 4 16
        4 0 10 None None
        13 0 16 None None
        16 1 10 13 28
        28 0 16 None None
        before remove===================
        4
        10
        13
        16
        28
        after remove====================
        4
        10
        13
        28
    """

    def insert(self, e):
        # x = BST.insert(self, e)  # 这里不能直接用insert， 因为后面会自动更新高度的信息（前面的节点的高度有可能不修改）。
        x = self.search(e)
        if x is not None:
            return x
        x = BinNodePosi(e, self._hot)
        if self.hot.data < e:
            self.hot.rc = x
        else:
            self.hot.lc = x
        self._size += 1
        g = self.hot
        while g is not None:
            if not AvlBalanced(g):
                self.rotateAt(TallerChild(TallerChild(g)))
                break
            else:
                self._updateHeight(g)
            g = g.parent
        return x

    def remove(self, e):
        """删除会导致向上失衡，不能提前中止"""
        x = self.search(e)
        if x is None:
            return False
        self._removeAt(x)
        self._size -= 1
        g = self.hot
        while g is not None:
            if not AvlBalanced(g):
                g = self.rotateAt(TallerChild(TallerChild(g)))
            self._updateHeight(g)
            g = g.parent
        return True


def Balanced(x: BinNodePosi):
    return stature(x.lc) == stature(x.rc)


def BalFac(x):
    """左右节点高度之差即平衡因子"""
    return stature(x.lc) - stature(x.rc)


def AvlBalanced(x):
    """节点（左右子树）平衡条件"""
    return -2 < BalFac(x) < 2


def TallerChild(x):
    """获取失衡节点x的更高（高度）孩子，和更高孙子节点的方向(调用两次)"""
    lStature = stature(x.lc)
    rStature = stature(x.rc)
    if lStature > rStature:
        return x.lc
    elif lStature < rStature:
        return x.rc
    else:  # 如果相等获取 x 同方向节点
        if IsLChild(x):
            return x.lc
        else:
            return x.rc


class Splay(BST):
    """伸展树
    不需要平衡因子，每访问一次，调整一次。
         a = Splay()
        b = []
        b.append(a.insertAsRoot(10))
        b.append(a.insert(4))
        b.append(a.insert(13))
        b.append(a.insert(16))
        b.append(a.insert(28))
        print('data--height--parent--lc--rc')
        for i in b:
            print(i.data, i.height, i.parent.data if i.parent else None, i.lc.data if i.lc else None, i.rc.data if i.rc else None)
        print("before remove===================")
        a.travIn()
        a.remove(16)
        print("after remove====================")
        a.travIn()
        print(a.search(4))
        for i in b:
            print(i.data, i.height, i.parent.data if i.parent else None, i.lc.data if i.lc else None, i.rc.data if i.rc else None)
        a.travIn()
        print(a.search(13))
        for i in b:
            print(i.data, i.height, i.parent.data if i.parent else None, i.lc.data if i.lc else None, i.rc.data if i.rc else None)
        a.travIn()

        =======================================================
        data--height--parent--lc--rc
        10 1 13 4 None
        4 0 10 None None
        13 2 16 10 None
        16 3 28 13 None
        28 4 None 16 None
        before remove===================
        4
        10
        13
        16
        28
        after remove====================
        4
        10
        13
        28
        <BinTree.BinNode object at 0x7fe34890b3c8>
        10 1 28 None 13
        4 3 None None 28
        13 0 10 None None
        16 3 None None 28
        28 2 4 10 None
        4
        10
        13
        28
        <BinTree.BinNode object at 0x7fe34890feb8>
        10 0 4 None None
        4 1 13 None 10
        13 2 None 4 28
        16 3 None None 28
        28 0 13 None None
        4
        10
        13
        28
    """

    def attachAsLChild(self, p: BinNodePosi, lc=None):
        p.lc = lc
        if lc is not None:
            lc.parent = p

    def attachAsRChild(self, p: BinNodePosi, rc=None):
        p.rc = rc
        if rc is not None:
            rc.parent = p

    def splay(self, v: BinNodePosi):
        """四种情况分别拆散组装成最终的形态
        最终实现的效果是 v 为新子树的根节点， 所以 zig-zag和zag-zig按照AVL处理， 而zig-zig和zag-zag需要先旋转g后p。
        1: zig-zig, 左左形式（先旋转 g 后 p）
                    g                      v      
                    |                      |     
                ---------              ---------   
                |       |              |       |  
                p       T3            T0       p 
            --------          ==>          ---------  
            |      |                       |       |   
            v     T2                       T1      g      
            |                                      |  
        ---------                              --------  
        |       |                              |      |  
        T0     T1                              T2    T3  
        2: zig-zag, 右左形式, 跟AVL一样先 zig 旋转 p， 后 zag 旋转 g
              g                               v    
              |                               |     
        -------------                     ---------          
        |           |                     |       |      
        T0          p                     g       p
                    |                     |       |
                ---------       ==>     -----  ------
                |       |               |   |  |    |
                v       T3              T0  T1 T2   T3
                |
            -------
            |     |
            T1   T2             
        3： zag-zag, 右右形式（先旋转 g 后 p）
                g                                     v        
                |                                     |          
            ---------                           ------------       
            |       |                           |          |    
           T0       p                           p          T3     
                --------        ==>         --------           
                |      |                    |      |              
                T1      v                   g      T2     
                        |                   |          
                    --------            --------               
                    |      |            |      |               
                    T2    T3            T0    T1        
        4： zag-zig, 左右形式, 跟AVL一样先 zag 旋转 p， 后 zig 旋转 g
                  g                           v
                  |                           |
            ------------                  ---------
            |           |                 |       |
            p           T3                p       g
        --------              ==>     -------   --------
        |      |                      |     |   |      |
        T0      v                     T0    T1  T2     T3
                |                     
            --------                      
            |      |                      
            T1    T2     
        每次都进行双层伸展操作
        """
        if v is None:
            return None
        p = v.parent
        while p is not None and p.parent is not None:
            g = p.parent
            gg = g.parent
            isLChild = IsLChild(g)
            if IsLChild(v):
                if IsLChild(p):  # zig-zig
                    self.attachAsLChild(g, p.rc)
                    self.attachAsLChild(p, v.rc)
                    self.attachAsRChild(p, g)
                    self.attachAsRChild(v, p)
                else:  # zig-zag
                    self.attachAsLChild(p, v.rc)
                    self.attachAsRChild(g, v.lc)
                    self.attachAsLChild(v, g)
                    self.attachAsRChild(v, p)
            else:
                if IsRChild(p):  # zag-zag
                    self.attachAsRChild(g, p.lc)
                    self.attachAsRChild(p, v.lc)
                    self.attachAsLChild(p, g)
                    self.attachAsLChild(v, p)
                else:  # zag-zig
                    self.attachAsRChild(p, v.lc)
                    self.attachAsLChild(g, v.rc)
                    self.attachAsRChild(v, g)
                    self.attachAsLChild(v, p)
            if gg is None:
                v.parent = None
            else:
                if isLChild:
                    self.attachAsLChild(gg, v)
                else:
                    self.attachAsRChild(gg, v)
            self._updateHeight(g)  # 因为调整后 g 最低， v 最高
            self._updateHeight(p)
            self._updateHeight(v)
            p = v.parent
        if p is not None:  # 循环结束， 而 p 存在，说明g不存在， 即高度为奇数， 需要再作一次单旋。
            if IsLChild(v):  # zig
                self.attachAsLChild(p, v.rc)
                self.attachAsRChild(v, p)
            else:  # zag
                self.attachAsRChild(p, v.lc)
                self.attachAsLChild(v, p)
            self._updateHeight(p)
            self._updateHeight(v)
        v.parent = None  # 根节点
        return v

    def search(self, e):
        """每次访问 e 对应的节点， 节点往根节点伸展"""
        p = self._searchIn(self._root, e)
        self._root = self.splay(p if p is not None else self.hot)
        return self._root

    def insert(self, e):
        if self._root is None:
            self.insertAsRoot(e)
            return self._root
        if e == self.search(e).data:  # search 之后，目标节点在根节点
            return self._root
        # 说明不存在 e 对应的节点, 需要将 e 作为根节点连接
        t = self._root
        if self._root.data < e:  # 不存在的话， root.lc < e < root 或者 root < e < root.rc
            self._root = BinNode(e, None, t, t.rc)
            t.parent = self._root
            if HasRChild(t):
                t.rc.parent = self._root
                t.rc = None
        else:
            self._root = BinNode(e, None, t.lc, t)
            t.parent = self._root
            if HasLChild(t):
                t.lc.parent = self._root
                t.lc = None
        self._updateHeightAbove(t)
        self._size += 1
        return self._root

    def remove(self, e):
        if not self._root or e != self.search(e).data:
            return False
        w = self._root
        if not HasLChild(self._root):
            self._root = self._root.rc
            if self._root is not None:
                self._root.parent = None
        elif not HasRChild(self._root):
            self._root = self._root.lc
            if self._root is not None:
                self._root.parent = None
        else:  # 左右子树存在
            lTree = self._root.lc
            lTree.parent = None
            self._root.lc = None
            self._root = self._root.rc
            self._root.parent = None

            # 搜索删除节点数据（根节点）， 此时必然搜索不到
            # 则会将删除节点的后继节点作为根节点， 且只可能有右子树
            self.search(w.data)
            self._root.lc = lTree
            lTree.parent = self._root
        release(w)
        self._size -= 1
        if self._root is not None:
            self._updateHeight(self._root)
        return True


