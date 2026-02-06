package bytedance

func countRangeSum(nums []int, lower int, upper int) int {
	/*
		327. 区间和的个数

		给你一个整数数组 nums 以及两个整数 lower 和 upper，求数组中，值位于范围 [lower, upper] （包含 lower 和 upper）之内的 区间和的个数。

		区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。

		输入: nums = [-2,5,-1], lower = -2, upper = 2
		输出: 3
		解释: 存在三个区间 [0,0]、[2,2] 和 [0,2]，对应的区间和分别为 -2、-1、2。

		输入: nums = [0], lower = 0, upper = 0
		输出: 1

		1 <= nums.length <= 10^5
		-2^31 <= nums[i] <= 2^31 - 1
		-10^5 <= lower <= upper <= 10^5
		题目数据保证答案是一个 32 位的整数
	*/
	// 求连续的子数组的和，在 [lower,upper] 内的个数

	// 计算前缀和
	n := len(nums)
	pre := make([]int, n+1)
	for i, num := range nums {
		pre[i+1] = pre[i] + num
	}

	// 暴力求解，for i, for j, 从i到j 和是否在区间内，在则+1
	// 优化，归并排序，右边遍历 preSum[j]，找到 preSum[j] - preSum[i] 在区间内的个数
	// 排序后可以直接位置相减，而不需要逐个遍历，因为都在左边，preSum 是前缀和一定会跟右边相连，所以排序后不会影响数组的相对位置
	// 对前缀和归并排序

	var mergeSort func(l, r int) int
	tmp := make([]int, n+1)

	// 左闭右开
	mergeSort = func(l, r int) int {
		if r <= l {
			return 0
		}
		m := (l + r) / 2
		cnt := mergeSort(l, m) + mergeSort(m+1, r)

		// 找出左边，大于等于 preSum[j] - upper 的第一个位置 i，以及 大于 preSum[j] - lower 位置 t, 则符合要求的格式是 t-i
		// 当 j 向前，i 和 t应该在原有位置向前
		i := l
		t := l
		for j := m + 1; j <= r; j++ {
			for i <= m && pre[i] < pre[j]-upper {
				i++
			}
			for t <= m && pre[t] <= pre[j]-lower {
				t++
			}
			cnt += t - i
		}

		// 合并
		i, j, k := l, m+1, l
		for i <= m && j <= r {
			if pre[i] <= pre[j] {
				tmp[k] = pre[i]
				i++
			} else {
				tmp[k] = pre[j]
				j++
			}
			k++
		}
		for i <= m {
			tmp[k] = pre[i]
			i++
			k++
		}
		for j <= r {
			tmp[k] = pre[j]
			j++
			k++
		}

		for i := l; i <= r; i++ {
			pre[i] = tmp[i]
		}
		return cnt
	}

	return mergeSort(0, n)
}
