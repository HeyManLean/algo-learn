package bytedance

import (
	"sort"
)

func smallestDistancePair(nums []int, k int) int {
	/*
		719. 找出第 k 小的距离对

		给定一个整数数组 nums 和一个整数 k ，返回所有数对中第 k 小的距离对（距离定义为 |nums[i] - nums[j]|）。

		注意：|nums[i] - nums[j]| 表示 nums[i] 和 nums[j] 之间的绝对差值。

		示例 1：
		输入：nums = [1,3,1], k = 1
		输出：0
		解释：数对和对应的距离如下：
		(1,3) -> 2
		(1,1) -> 0
		(3,1) -> 2
		距离排序后为 0, 2, 2，第 1 小的距离对是 0。

		示例 2：
		输入：nums = [1,1,1], k = 2
		输出：0

		示例 3：
		输入：nums = [1,6,1], k = 3
		输出：5

		提示：
		n == nums.length
		2 <= n <= 10^4
		0 <= nums[i] <= 10^6
		1 <= k <= n * (n - 1) / 2
	*/
	// 暴力法
	// 逐个生成对，然后计算距离，取第k大  n² + n + klogn
	// 优化：能否递增式，而不是先生成所有差值，扔到堆，再取k个
	// 改为逐个扔进对，到了k个就马上结束
	// 先排序，计算前后数字差值（相邻数字更小）
	// 先排序，遍历一轮，将相邻差扔到堆（包括 i,j,v），每次pop出来，将该i,j旁边的位置扔到堆里面，扩大，i-1,j  i,j+1

	sort.Ints(nums)
	n := len(nums)
	// 二分法，从最大差值，找到中间差值的距离对数量，直到找到距离对数量是k
	// 滑动窗口，收缩或扩展，找到差值在 mid 内的数量

	var countDistance = func(mid int) int {
		// 找到差值 <= mid 的距离对数量
		j := 1
		cnt := 0
		for i := 0; i < n; i++ {
			if j < i+1 {
				j = i + 1
			}
			for j < n && nums[j]-nums[i] <= mid {
				j++
			}
			cnt += j - i - 1
		}
		return cnt
	}
	lo, hi := 0, nums[n-1]-nums[0]
	for lo < hi {
		mid := (lo + hi) / 2
		cnt := countDistance(mid)
		if cnt >= k {
			hi = mid // 可能有比mid小的值，也是k
		} else {
			lo = mid + 1
		}
	}
	return lo
}
