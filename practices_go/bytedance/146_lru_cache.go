package bytedance

type LRUNode struct {
	Prev *LRUNode
	Next *LRUNode
	Val  int
	Key  int
}

// LRUCache 146. LRU 缓存机制
type LRUCache struct {
	// TODO: 定义内部字段，不实现逻辑

	// Get 需要使用 map 映射
	// 访问过需要移到最近访问，双向链表，并维护队列头和队列尾巴

	head *LRUNode
	tail *LRUNode
	cap  int
	size int
	dict map[int]*LRUNode
}

// Constructor 使用 capacity 初始化 LRU 缓存
func Constructor(capacity int) LRUCache {
	/*
		146. LRU 缓存机制

		请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。

		实现 LRUCache 类：
		- LRUCache(capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
		- Get(key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1
		- Put(key, value) 如果关键字 key 已经存在，则变更其数据值 value；
		  如果不存在，则向缓存中插入该组 key-value。
		  若插入操作导致关键字数量超过 capacity，则应该 逐出 最久未使用的关键字。

		函数 get 和 put 必须以 O(1) 平均时间复杂度运行。

		输入
		["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
		[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
		输出
		[null, null, null, 1, null, -1, null, -1, 3, 4]

		解释
		LRUCache lRUCache = new LRUCache(2);
		lRUCache.put(1, 1); // 缓存是 {1=1}
		lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
		lRUCache.get(1);    // 返回 1
		lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
		lRUCache.get(2);    // 返回 -1 (未找到)
		lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
		lRUCache.get(1);    // 返回 -1 (未找到)
		lRUCache.get(3);    // 返回 3
		lRUCache.get(4);    // 返回 4

		1 <= capacity <= 3000
		0 <= key <= 10^4
		0 <= value <= 10^5
		最多调用 2*10^5 次 get 和 put
	*/
	head := &LRUNode{}
	tail := &LRUNode{}
	head.Next = tail
	tail.Prev = head
	return LRUCache{
		head: head,
		tail: tail,
		size: 0,
		cap:  capacity,
		dict: make(map[int]*LRUNode),
	}
}

func (c *LRUCache) moveFirst(node *LRUNode) {
	c.removeNode(node)
	next := c.head.Next
	c.head.Next = node
	next.Prev = node

	node.Prev = c.head
	node.Next = next
}

func (c *LRUCache) delLast() {
	if c.size == 0 {
		return
	}
	c.size -= 1
	node := c.tail.Prev
	c.removeNode(node)
	delete(c.dict, node.Key)
}

func (c *LRUCache) removeNode(node *LRUNode) {
	node.Next.Prev = node.Prev
	node.Prev.Next = node.Next

	node.Next = nil
	node.Prev = nil
}

// Get 若 key 存在返回对应值，否则返回 -1
func (c *LRUCache) Get(key int) int {
	node, ok := c.dict[key]
	if !ok {
		return -1
	}
	c.moveFirst(node)
	return node.Val
}

// Put 插入或更新 key-value，超过容量时逐出最久未使用的项
func (c *LRUCache) Put(key int, value int) {
	node, ok := c.dict[key]
	if ok {
		node.Val = value
		c.moveFirst(node)
		return
	}
	if c.size == c.cap {
		c.delLast()
	}
	node = &LRUNode{
		Val:  value,
		Next: c.head.Next,
		Prev: c.head,
		Key:  key,
	}
	c.dict[key] = node
	c.head.Next.Prev = node
	c.head.Next = node
	c.size += 1
}
