package dynamicplan

func lengthOfLIS(nums []int) int {
	/*
		300. 最长递增子序列

		给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

		子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
		例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

		输入：nums = [10,9,2,5,3,7,101,18]
		输出：4
		解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

		输入：nums = [0,1,0,3,2,3]
		输出：4

		输入：nums = [7,7,7,7,7,7,7]
		输出：1


		提示：
		1 <= nums.length <= 2500
		-104 <= nums[i] <= 104

		进阶：
		你能将算法的时间复杂度降低到 O(n log(n)) 吗?
	*/
	// 堆牌的方式，每个牌堆从大到小叠牌，每次新的牌找到比它大的左边第一个牌堆，如果没有则新增牌堆
	// 二分法找到比当前牌大或相等的牌堆
	// 牌堆顶部，就是从小到大
	// 让牌顶尽可能的小，从左到右都变小，那么就可能产生新的堆，扩大长度
	n := len(nums)

	piles := 0
	top := make([]int, n)

	for _, num := range nums {
		// 二分法找到堆顶，否则新建堆
		left := 0
		right := piles

		for left < right {
			mid := (left + right) / 2
			if top[mid] >= num {
				right = mid
			} else {
				left = mid + 1
			}
		}
		top[left] = num
		if left == piles {
			piles++
		}
	}
	return piles
}
