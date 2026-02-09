package bytedance

import (
	"strconv"
	"strings"
)

func getPermutation(n int, k int) string {
	/*
		60. 第k个排列

		给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。

		按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

		"123"
		"132"
		"213"
		"231"
		"312"
		"321"
		给定 n 和 k，返回第 k 个排列。

		示例 1：
		输入: n = 3, k = 3
		输出: "213"

		示例 2：
		输入: n = 4, k = 9
		输出: "2314"

		示例 3：
		输入: n = 3, k = 1
		输出: "123"

		1 <= n <= 9
		1 <= k <= n!
	*/
	//  假设第一个数字选定后，剩余数字有 (n-1)!  个选法
	// 1 开头，顺序是：1~(n-1)!
	// 2 开头，顺序是:(n-1)!~2*(n-1)!

	// 则第一个数字是 k / (n-1)! 位置的数字，然后剩余 k % (n-1)! 继续选第二、第三个位置，直到选了n个数字
	// 选计算 n 为 1 到 n 时的排列数

	fact := make([]int, n+1)
	nums := make([]int, n)
	fact[0] = 1
	for i := 1; i <= n; i++ {
		fact[i] = fact[i-1] * i
		nums[i-1] = i
	}

	s := strings.Builder{}
	// 选n个数，
	k-- // 从0开始
	for i := n; i >= 1; i-- {
		block := fact[i-1]
		idx := k / block

		s.WriteString(strconv.Itoa(nums[idx]))

		k = k % block
		// 移除nums[idx]
		nums = append(nums[:idx], nums[idx+1:]...)
	}
	return s.String()

}
