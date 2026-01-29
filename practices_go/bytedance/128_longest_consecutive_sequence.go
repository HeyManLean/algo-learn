package bytedance

func longestConsecutive(nums []int) int {
	/*
		128. 最长连续序列

		给定一个未排序的整数数组 nums，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

		请你设计并实现时间复杂度为 O(n) 的算法解决此问题。


		输入: nums = [100,4,200,1,3,2]
		输出: 4
		解释: 最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。

		输入: nums = [0,3,7,2,5,8,4,6,0,1]
		输出: 9

		0 <= nums.length <= 10^5
		-10^9 <= nums[i] <= 10^9
	*/
	// 遇到一个数字，尝试往 num+1 进行，直到计算能触达的最大数字，之后跳过访问这些数字
	// 记录 num 往后有多少个字符

	numFlag := make(map[int]bool)
	for _, num := range nums {
		numFlag[num] = true
	}

	consMap := make(map[int]int)
	res := 0

	var max = func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	for _, num := range nums {
		// 前面数字一定会算，那就不用算当前数字
		if numFlag[num-1] || consMap[num] > 0 {
			continue
		}
		cur := num
		cons := 1
		for numFlag[cur+1] {
			cons++
			cur++
		}
		consMap[num] = cons
		res = max(res, cons)
	}
	return res
}

func longestConsecutiveUgly(nums []int) int {
	if len(nums) <= 1 {
		return len(nums)
	}
	// 维护每个数字前面有多少个，后面有多少个数字，如果是连续的序列，只维护最左和最右
	right := make(map[int]int) // right[i] = j 最左边为 i, 右边是j
	left := make(map[int]int)  // left[i] = j 最右边是i，左边是j

	var max = func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	res := 1

	// 过滤重复
	visited := make(map[int]bool)

	for _, num := range nums {
		// 检查左边和右边
		if visited[num] {
			continue
		}
		visited[num] = true

		l, hasLeft := left[num-1]
		r, hasRight := right[num+1]

		if hasLeft && !hasRight {
			// 只有左边
			right[l] = num      // 左边的右侧改为 num
			left[num] = l       // 当前数字左侧改为l
			delete(left, num-1) // 移除前一个数字的左侧映射
			res = max(res, num-l+1)
		} else if !hasLeft && hasRight {
			// 只有右边
			left[r] = num        // 右边的最左侧改为 num
			right[num] = r       // 当前数字的右侧为r
			delete(right, num+1) // 移除下一个数字的右侧映射
			res = max(res, r-num+1)
		} else if hasLeft && hasRight {
			// 有左右
			// 左边的右侧改为r
			// 右边的左侧改为l
			// 移除 left[num-1] 和 right[num+1]
			right[l] = r
			left[r] = l
			delete(left, num-1)
			delete(right, num+1)
			res = max(res, r-l+1)
		} else {
			// 都没有
			left[num] = num
			right[num] = num
		}
	}
	return res
}
