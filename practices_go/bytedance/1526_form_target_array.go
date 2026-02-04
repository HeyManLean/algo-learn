package bytedance

func minNumberOperations(target []int) int {
	/*
		1526. 形成目标数组的子数组的最少操作次数

		给你一个整数数组 target 。一开始你有一个长度为 n 的整数数组 initial ，其元素均为 0 。
		每一次操作你可以选择 initial 的任意子数组，并将子数组中每个元素加 1 。
		返回使 initial 变为 target 的最少操作次数。

		输入: target = [1,2,3,2,1]
		输出: 3
		解释: 至少需要 3 次操作：[0,0,0,0,0] -> [1,1,1,1,1] -> [1,2,2,2,1] -> [1,2,3,2,1]

		输入: target = [3,1,1,2]
		输出: 4

		输入: target = [3,1,5,4,2]
		输出: 7

		1 <= target.length <= 10^5
		1 <= target[i] <= 10^5
		测试数据保证答案在 32 位整数范围内
	*/
	// 如果当前数字比前一个数字大，则额外需要操作数需要加上差值
	// 如果当前数组小于等于前一个数字，则不需要额外操作数
	res := target[0]

	for i := 1; i < len(target); i++ {
		diff := target[i] - target[i-1]
		if diff > 0 {
			res += diff
		}
	}
	return res
}
