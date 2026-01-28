package bytedance

func minWindow(s string, t string) string {
	/*
		76. 最小覆盖子串

		给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。
		如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

		注意：
		- 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
		- 如果 s 中存在这样的子串，我们保证它是唯一的答案。

		示例 1：
		输入：s = "ADOBECODEBANC", t = "ABC"
		输出："BANC"
		解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。

		示例 2：
		输入：s = "a", t = "a"
		输出："a"
		解释：整个字符串 s 是最小覆盖子串。

		示例 3：
		输入：s = "a", t = "aa"
		输出：""
		解释：t 中两个字符 'a' 均应包含在 s 的子串中，
		因此没有符合条件的子串，返回空字符串。

		提示：
		m == s.length
		n == t.length
		1 <= m, n <= 10^5
		s 和 t 由英文字母组成

		进阶：你能设计一个在 O(m+n) 时间内解决此问题的算法吗？
	*/
	// 滑动窗口，左边指针向前移动，直到字符在 t 中，

	// 重复
	// 则右边往前走，直到包含了 t 所有字符（包括重复）
	// 尝试让左边指针前进，直到无法包含t所有字符

	// 怎么判断是否包含t所有字符？
	// map 维护，当前未包含的字符及个数，遇到t中字符，则个数减一，如果为0，则移除掉字符，如果map长度为0，则表示包含
	// 如果左边指针移动，则尝试将字符加回map，不要多加

	// 需要维护原本t每个字符的个数，避免加多

	col := NewCollection(t)

	m := len(s)
	res := ""

	left := 0
	right := 0
	for left <= right && right < m {
		for !col.Full() && right < m {
			col.Add(s[right])
			right++
		}
		for col.Full() {
			if res == "" || len(res) > right-left {
				res = s[left:right]
			}
			col.Remove(s[left])
			left++
		}
	}
	return res
}

type Collection struct {
	targetMap    map[byte]int
	containMap   map[byte]int
	containCount int
}

func (col *Collection) Add(c byte) {
	target, ok := col.targetMap[c]
	if !ok {
		return
	}
	col.containMap[c] += 1
	// 刚好相等时，记录匹配到的字母数量
	if col.containMap[c] == target {
		col.containCount += 1
	}
}

func (col *Collection) Remove(c byte) {
	target, ok := col.targetMap[c]
	if !ok {
		return
	}
	if col.containMap[c] == target {
		col.containCount -= 1
	}
	col.containMap[c] -= 1
}

func (col *Collection) Full() bool {
	return col.containCount == len(col.targetMap)
}

func NewCollection(t string) *Collection {
	targetMap := make(map[byte]int)

	n := len(t)
	for i := 0; i < n; i++ {
		targetMap[t[i]] += 1
	}
	return &Collection{
		targetMap:  targetMap,
		containMap: make(map[byte]int),
	}
}
