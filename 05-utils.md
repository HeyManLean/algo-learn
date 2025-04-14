# 常见工具实现

## 缓存淘汰算法

### LRU 缓存（146）

LRU 最近最少使用，在 O(1) 时间复杂度获取元素和新增元素
- 如果超过容量，则淘汰最近最少使用的元素（即上次使用时间最早）

实现方案：
1. 使用双向链表，按照使用时间排序元素节点
2. 另外维护一个 hash 字典，维护 key 到元素节点的映射
- 可以在 O(1) 找到元素所在节点
3. 访问或修改元素节点时，通过 hash 字典找到元素节点，将节点移到链表头部；
4. 容量满时，将链表尾部的节点移除，并从 hash 字典删除；

```py
class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev  # type:Node
        self.next = next  # type:Node


class LRUCache:
    def __init__(self, capacity: int):
        # 维护一个 hash map 和一个双向链表
        # 1. hash map 通过key索引到链表节点，访问可以做到 O(1)
        # 2. 访问该节点时，将节点移到 head 节点，将前后两节点直连，保证访问时间顺序
        # 3. 容量满时，将尾部节点移除，并将key从hash map移除
        self.map = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        node = self.map.get(key)
        if not node:
            return -1

        self.move_first(node)
        return node.val

    def move_first(self, node: Node):
        """将刚访问的节点移到头部"""
        if node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev

        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove_last(self):
        """检查是否超过容量，超过则移除尾部节点"""
        if self.size <= self.capacity:
            return False

        # 移出尾部节点
        remove_node = self.tail.prev
        self.map.pop(remove_node.key)
        self.tail.prev = remove_node.prev
        remove_node.prev.next = self.tail
        self.size -= 1

    def put(self, key: int, value: int) -> None:
        node = self.map.get(key)
        if node:
            node.val = value
        else:
            node = Node(key, value)
            self.map[key] = node
            self.size += 1

        self.move_first(node)
        self.remove_last()
```


### LFU 缓存（460）

LFS: 最少使用次数，在 O(1) 时间复杂度访问或修改某个 key 的数值
- 如果容量满了，淘汰使用次数最少的元素，如果使用次数一样，则淘汰上次使用时间最早的元素

实现方案：
1. 使用一个 hash 字典 `map` 维护 key 到节点映射，节点保存 key，val，访问次数等信息
2. 另外使用一个 hash 字典 `freq_to_keys` 维护每个访问次数，对应有哪些 key
3. 使用一个变量 `min_freq` 维护当前最小频次，默认是 1

新增数据时：
1. `map` 添加 key 到节点映射，访问次数为1
2. 将 key 加入 `freq_to_keys` 对应频次 1 的列表中
3. 最小频次 `min_freq` 改成 1

访问或修改数据时：
1. 更新 `map` 对应key的访问次数
2. 将该 key 从 `freq_to_keys` 对应频次的列表移除
- 如果对应频次的列表为空，且频次等于最小频次 `min_freq`，则 `min_freq` 加 1
3. 将 key 加到 `freq_to_keys` 频次加1的列表中

```py
class Node:
    def __init__(self, key, val, freq=1):
        self.key = key
        self.val = val
        self.freq = freq


class LFUCache:
    def __init__(self, capacity: int):
        self.map = {}  # type:dict[int, Node]
        self.freq_to_keys = {}
        self.min_freq = 1
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        node = self.map.get(key)
        if not node:
            return -1

        self.add_freq(node)
        return node.val

    def add_freq(self, node):
        # 从原本的 FV 移除
        self.freq_to_keys[node.freq].pop(node.key)
        if not self.freq_to_keys[node.freq]:
            # 最小频次的key空了，需要加1
            if node.freq == self.min_freq:
                self.min_freq = node.freq + 1
            self.freq_to_keys.pop(node.freq)

        # 加入新的 FV
        node.freq += 1
        self.freq_to_keys.setdefault(node.freq, OrderedDict())
        self.freq_to_keys[node.freq][node.key] = 1

    def remove_min(self):
        """移除最小频率的节点
        - 从列表移除，不需要更新 min_freq，put 会重置 min_freq
        """
        keys = self.freq_to_keys.get(self.min_freq)
        if not keys:
            return

        key, _ = keys.popitem(last=False)
        self.map.pop(key)
        if not keys:
            self.freq_to_keys.pop(self.min_freq)
        self.size -= 1

    def put(self, key: int, value: int) -> None:
        """添加节点"""
        node = self.map.get(key)
        if node:
            node.val = value
            self.add_freq(node)
            return

        # 新增 node，需要检查是否超过容量，移除掉最小频率的值
        if self.size + 1 > self.capacity:
            self.remove_min()

        self.min_freq = 1
        self.freq_to_keys.setdefault(self.min_freq, OrderedDict())
        self.freq_to_keys[self.min_freq][key] = 1
        self.map[key] = Node(key, value)
        self.size += 1
```

## 负载均衡算法

### 平滑加权轮询

场景：保证权重的情况下，避免同一时间请求都落在同一个节点，造成分配不均
每个节点额外维护两个权重：
- `weight`：配置的该节点的固定权重
- `current_weight`：轮询动态权重，初始化为0

1. 获取节点时，会对各个节点的 `current_weight`先加上各自配置的权重 `weight`
2. 每轮加权重之后，获取 `current_weight` 最大的节点作为选择的节点
3. 将选择的节点的 `current_weight` 减去所有节点配置权重总和

```py
import hashlib

class WeightedNode:
    def __init__(self, host, weight):
        self.host = host
        self.weight = weight
        self.current_weight = 0

    def incr_weight(self):
        self.current_weight += self.weight
        return self.current_weight
    
    def sub_weight(self, weight):
        self.current_weight -= weight
        return self.current_weight


class SmoothWeightedRoundRobin:
    def __init__(self, nodes: list[WeightedNode]):
        self.nodes = nodes
        self.total_weight = sum(node.weight for node in nodes)

    def get_next_host(self) -> str:
        """获取下一个host"""
        max_weight = self.nodes[0].incr_weight()
        selected_node = self.nodes[0]

        for node in self.nodes[1:]:
            cur_weight = node.incr_weight()
            if cur_weight > max_weight:
                selected_node = node

        selected_node.sub_weight(self.total_weight)
        return selected_node.host
```

### 一致性哈希算法

场景：需要将同一个用户的请求交于相同节点进行处理，避免用户缓存的冗余

原理：
1. 维护一个虚拟空间，节点范围足够大
2. 当节点注册时，每个节点会按照指定数量，创建多个虚拟节点
3. 这些虚拟节点会映射到虚拟空间的某个具体位置
4. 当通过某个key获取节点时，对 key 进行 hash，选取该 hash 在虚拟空间顺时针遇到的第一个虚拟节点作为目标节点

```py

class VirtualNode:
    def __init__(self, host, replicas_no, index):
        self.host = host
        self.replicas_no = replicas_no
        self.index = index

    def __repr__(self):
        return f'<VN {self.__dict__}>'


class ConsistentHashing:
    def __init__(self, capacity=1000, replicas=10):
        self.capacity = capacity  # capacity 要足够大！
        self.ring = {}
        self.key_to_node = {}
        self.replicas = replicas

    def get_hash(self, key):
        return int(hashlib.md5(str(key).encode()).hexdigest(), 16) % self.capacity

    def get_index(self, key):
        h = self.get_hash(key)
        # 找到不冲突的位置
        for i in range(self.capacity):
            index = (h + i) % self.capacity
            if index in self.ring:
                continue
            return index

        raise ValueError("exceed hashing size!")

    def add_host(self, host):
        for replicas_no in range(self.replicas):
            key = f'{host}_{replicas_no}'
            index = self.get_index(key)
            node = VirtualNode(host, replicas_no, index)
            self.ring[index] = node
            self.key_to_node[key] = node

    def remove_host(self, host):
        for replicas_no in range(self.replicas):
            key = f'{host}_{replicas_no}'
            if key not in self.key_to_node:
                continue
            node = self.key_to_node.pop(key)
            self.ring.pop(node.index)

    def get_host(self, key):
        h = self.get_hash(key)
        for i in range(self.capacity):
            index = (h + i) % self.capacity
            if index not in self.ring:
                continue
            return self.ring[index].host
        return ""
```

## 计算器（224）

计算机处理的关键主要有两个点：
1. 括号最优先，且存在嵌套括号
2. 乘除法较优先

加减法计算：
1. 使用一个栈维护数值，将加减数先加到栈中
2. 返回最后结果时，算出总和即可

括号问题处理：
1. 对输入字符串进行遍历，维护各个开括号和闭括号的位置映射；
2. 当访问到开括号，则找到对应闭括号的位置，进行递归计算，返回一个结果数值

乘除法处理：
1. 遇到乘除符号，将上一个数直接跟该数进行乘除
2. 将得出结果覆盖上一个数

```py
class Solution:
    def calculate(self, s: str) -> int:
        # 先移除空格
        s = s.replace(' ', '')

        # index_map 维护各个开括号和闭括号的位置映射
        left_index = []
        index_map = {}
        for idx, c in enumerate(s):
            if c == '(':
                left_index.append(idx)
            elif c == ')':
                index_map[left_index.pop()] = idx

        def _caculate(s: str, left, right):
            # [left, right) 左闭右开
            stk = []
            num = 0
            sign = "+"
            while left < right:
                c = s[left]

                # 遇到数字则加到当前数字
                if c.isdigit():
                    num = num * 10 + int(c)

                # 这个num可能是两个括号算出的新 num
                # 遇到一个开括号 ( 则进入递归运算，将 () 的值计算出来加入栈中后，再对当前数值继续遍历
                if c == '(':
                    right_index = index_map[left]
                    num = _caculate(s, left + 1, right_index)
                    left = right_index  # 跳到闭括号

                # 遇到新的符号，将之前的数字和符号进行运算
                # 处理最后一个字符结果后，需要将num加入栈中
                if c in "+-*/" or left + 1 == right:
                    if sign == '+':
                        stk.append(num)
                    elif sign == '-':
                        stk.append(-num)
                    elif sign == '*':
                        stk[-1] *= num
                    elif sign == '/':
                        stk[-1] = int(stk[-1] / num)
                    sign = c
                    num = 0  # 重置数字
                left += 1
            return sum(stk)
        return _caculate(s, 0, len(s))
```