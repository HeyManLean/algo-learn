package bytedance

func findKthNumberInDict(n int, k int) int {
	/*
		440. 字典序的第K小数字

		给定整数 n 和 k，返回 [1, n] 中字典序第 k 小的数字。

		示例 1:
		输入: n = 13, k = 2
		输出: 10
		解释: 字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。

		示例 2:
		输入: n = 1, k = 1
		输出: 1

		提示:
		1 <= k <= n <= 10^9
	*/
	// 以1开头数字数量
	// 以2开头数字数量...

	// 确定以1开头，则k-1继续迭代
	// 如果以2开头，则k-以1开头的数量，继续迭代下一个数字

	// 以1开头的数量怎么算

	// 1, 10-19, 100-199, 1000-1999
	// 1+10+100+1000

	// n/10  > 0 : cnt+=1   1    n%=10
	// n/10  > 0 : cnt+=10  10-19  n%=10
	// ...
	// n/10  < 0 : cnt += n%=10 + 1    if n < 1000,  数量为：n-100 + 1

	countSteps := func(prefix int) int {
		steps := 0
		first, next := prefix, prefix+1
		for first <= n {
			// min(n+1, next) - first
			upper := next
			if upper > n+1 {
				upper = n + 1
			}
			steps += upper - first
			first *= 10
			next *= 10
		}
		return steps
	}

	// 从1开始，如果k大于1开头数量，则k-1开头数量，开始迭代2
	// 如果k小于2开头数量，k-1, 继续迭代2下一个数字
	cur := 1
	k--
	for k > 0 {
		steps := countSteps(cur)
		if steps <= k {
			k -= steps
			cur++
		} else {
			k -= 1
			cur = cur * 10
		}
	}

	return cur
}
