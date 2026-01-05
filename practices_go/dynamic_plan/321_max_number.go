package dynamicplan

func maxNumber(nums1 []int, nums2 []int, k int) []int {
	/*
		321. 拼接最大数

		给你两个整数数组 nums1 和 nums2，它们的长度分别为 m 和 n。
		数组 nums1 和 nums2 分别代表两个数各位上的数字。同时你也会得到一个整数 k。

		请你利用这两个数组中的数字创建一个长度为 k <= m + n 的最大数。
		同一数组中数字的相对顺序必须保持不变。

		返回代表答案的长度为 k 的数组。

		输入：nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5
		输出：[9,8,6,5,3]

		输入：nums1 = [6,7], nums2 = [6,0,4], k = 5
		输出：[6,7,6,0,4]

		输入：nums1 = [3,9], nums2 = [8,9], k = 3
		输出：[9,8,9]

		提示：
		m == nums1.length
		n == nums2.length
		1 <= m, n <= 500
		0 <= nums1[i], nums2[i] <= 9
		1 <= k <= m + n
		nums1 和 nums2 没有前导 0。
	*/
	// 问题，提取两个数组的子序列，穿插成新的数值，且要求数值最大

	// 假设从 nums1 取 1 个数字，nums2 取 k-1 个数字，最大值子序列
	// 合并两边最大值子序列：取大的放前面
	// 最后遍历 nums1 取2，nums2 取k-2个数字，以此类推取最大的那个数组
	m := len(nums1)
	n := len(nums2)
	res := []int{0}

	for i := 0; i <= k; i++ {
		// nums1 取i个数值，nums2 取 k-i个数值
		if k-i > n || i > m {
			continue
		}
		seq1 := maxSequence(nums1, i)
		seq2 := maxSequence(nums2, k-i)
		merged := merge(seq1, seq2)

		if greater(merged, 0, res, 0) {
			res = merged
		}
	}
	return res
}

func maxSequence(nums []int, k int) []int {
	if k == 0 {
		return []int{}
	}
	// 返回 k 位且数值最大的数组
	// 从中删除 len(nums) - k 个数
	// 如果删除个数大于0，且下一个数字大于栈，则作为新的栈顶
	stack := make([]int, 0, k)
	drops := len(nums) - k

	for _, num := range nums {
		// 单调递减序列，如果遇到 x 大于栈顶，则将小于x的数都删掉，前提是删除数量大于0
		for len(stack) > 0 && drops > 0 && num > stack[len(stack)-1] {
			stack = stack[:len(stack)-1]
			drops--
		}
		stack = append(stack, num)
	}

	return stack[:k]
}

func merge(nums1 []int, nums2 []int) []int {
	// 合并两个数组，取两个数组前缀最大值作为新数组前面（判断数组谁更大）
	m := len(nums1)
	n := len(nums2)
	res := make([]int, m+n)

	i := 0
	j := 0
	for i < m || j < n {
		if greater(nums1, i, nums2, j) {
			res[i+j] = nums1[i]
			i++
		} else {
			res[i+j] = nums2[j]
			j++
		}
	}
	return res
}

func greater(nums1 []int, i int, nums2 []int, j int) bool {
	// 判断前缀谁更大，而不是数值
	for i < len(nums1) && j < len(nums2) && nums1[i] == nums2[j] {
		i++
		j++
	}
	return j == len(nums2) || (i < len(nums1) && nums1[i] > nums2[j])
}
