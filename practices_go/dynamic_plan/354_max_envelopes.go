package dynamicplan

import "sort"

func maxEnvelopes(envelopes [][]int) int {
	/*
		354. 俄罗斯套娃信封问题
		给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。

		当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。

		请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

		注意：不允许旋转信封。

		输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
		输出：3
		解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。

		输入：envelopes = [[1,1],[1,1],[1,1]]
		输出：1
	*/
	// 先对信封按照第一维度排序，然后问题转换成最长递增子数组问题
	sort.Slice(envelopes, func(i, j int) bool {
		if envelopes[i][0] != envelopes[j][0] {
			return envelopes[i][0] < envelopes[j][0] // 宽度顺序
		}
		return envelopes[i][1] > envelopes[j][1] // 高度逆序
	})
	// 使用牌堆方式，二分查找，将dp时间复杂度的 n² 改成nlogn
	// 对于牌堆每个堆顶字段，如果大于当前数字，则将当前数字放入该堆顶，否则新建一个堆
	// 牌堆数量就是结果

	piles := 0
	top := make([]int, len(envelopes))

	for _, env := range envelopes {
		left, right := 0, piles // 左闭右开
		for left < right {
			mid := (left + right) / 2
			if env[1] <= top[mid] {
				right = mid
			} else {
				left = mid + 1
			}
		}
		top[left] = env[1]
		if left == piles {
			piles++
		}
	}

	return piles
}

func maxEnvelopesDp(envelopes [][]int) int {
	// dp 方式，超时！
	// 先对信封按照第一维度排序，然后问题转换成最长递增子数组问题
	sort.Slice(envelopes, func(i, j int) bool {
		return envelopes[i][0] <= envelopes[j][0]
	})

	// 最长递增子数组问题
	// dp[i] 表示包含i在内前i个数值的最长子数组的长度

	n := len(envelopes)
	dp := make([]int, n)
	dp[0] = 1
	res := 1

	for i := 1; i < n; i++ {
		dp[i] = 1
		for j := 0; j < i; j++ {
			if envelopes[i][1] > envelopes[j][1] && envelopes[i][0] > envelopes[j][0] {
				dp[i] = max(dp[i], dp[j]+1)
			}
		}
		if dp[i] > res {
			res = dp[i]
		}
	}
	return res
}
