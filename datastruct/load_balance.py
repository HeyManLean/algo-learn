# -*- coding: utf-8 -*-
"""
负载均衡算法

- 轮询
- 加权轮询
- 随机
- 加权随机
- 哈希
- 一致性哈希
"""

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


import hashlib


class SmoothWeightedRoundRobin:
    """平滑加权轮询

    场景：保证权重的情况下，避免同一时间请求都落在同一个节点，造成分配不均

    每个节点有两个属性：
    - weight：累加权重，即开始设置的权重，分配权重
    - current_weight: 记录节点当前权重值，每次取最大当前权重作为请求节点
        - 每次选取，将 weight 累加到 current_weight

    每次选中的节点，current_weight 需要减掉所有节点的 weight 总和
    """
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


class VirtualNode:
    def __init__(self, host, replicas_no, index):
        self.host = host
        self.replicas_no = replicas_no
        self.index = index

    def __repr__(self):
        return f'<VN {self.__dict__}>'


class ConsistentHashing:
    """一致性hash

    场景：用于需要将同一个用户请求落在同一个节点上
    - 如某个用户缓存只需要分布在个别节点，避免空间浪费，重复缓存带来一致性问题

    原理：
    1. 维护一个数值范围，新增节点时，每个节点创建多个虚拟节点，计算hash值，分别落在这个范围内
    2. 获取节点时，根据key的 hash 值，顺时针取下一个虚拟节点

    难点：
    hash算法，不能有冲突？ 如果有冲突，找下一个位置即可
    顺时针怎么高效找到下一个虚拟节点
    """
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


if __name__ == '__main__':
    nodes = [
        WeightedNode('host1', 5),
        WeightedNode('host2', 1),
        WeightedNode('host3', 1),
    ]
    rr = SmoothWeightedRoundRobin(nodes)
    for i in range(20):
        print(f"Request {i+1:<2d} -> {rr.get_next_host()}")

    print("---------- ConsistentHashing ---------")
    lb = ConsistentHashing()
    lb.add_host('host1')
    lb.add_host('host2')
    lb.add_host('host3')

    for i in range(10):
        print(f"Request {i:<2d} -> {lb.get_host(i)}")
        print(f"Request {i:<2d} -> {lb.get_host(i)}")
        print(f"Request {i:<2d} -> {lb.get_host(i)}")

    lb.remove_host('host2')
    print("after remove:")
    for i in range(10):
        print(f"Request {i:<2d} -> {lb.get_host(i)}")
        print(f"Request {i:<2d} -> {lb.get_host(i)}")
        print(f"Request {i:<2d} -> {lb.get_host(i)}")
