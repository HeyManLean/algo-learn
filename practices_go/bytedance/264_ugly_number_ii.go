package bytedance

func nthUglyNumber(n int) int {
	/*
		264. 丑数 II

		给你一个整数 n ，请你找出并返回第 n 个 丑数 。

		丑数 就是只包含质因数 2、3 和/或 5 的正整数。


		输入: n = 10
		输出: 12
		解释: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。

		输入: n = 1
		输出: 1
		解释: 1 通常被视为丑数。

		1 <= n <= 1690
	*/
	// 每个数字都是前面数字*2/3/5生成的
	// 维护列表，记录丑数列表
	// 三个变量分别维护2和3和5下一个相乘的数字
	u2 := 0
	u3 := 0
	u5 := 0

	var min = func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}

	ugly := []int{1}

	for len(ugly) < n {
		temp := min(ugly[u2]*2, min(ugly[u3]*3, ugly[u5]*5))
		ugly = append(ugly, temp)

		// 相等则跳过， 2*3， 3*2 会相等，则都前进
		if temp == ugly[u2]*2 {
			u2++
		}
		if temp == ugly[u3]*3 {
			u3++
		}
		if temp == ugly[u5]*5 {
			u5++
		}
	}
	return ugly[n-1]
}
