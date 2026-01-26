package dynamicplan

func findLength(nums1 []int, nums2 []int) int {
	/*
		718. 最长重复子数组

		给两个整数数组 nums1 和 nums2 ，返回 两个数组中 公共的 、长度最长的 子数组的长度 。

		输入：nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
		输出：3
		解释：长度最长的公共子数组是 [3,2,1] 。

		输入：nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
		输出：5

		提示：
		1 <= nums1.length, nums2.length <= 1000
		0 <= nums1[i], nums2[i] <= 100
	*/
	// dp[i][j] 表示 nums1[:i] 和 nums2[:j] 的最长公共长度，且包含 nums[i-1] 和 nums2[j-1]
	// dp[i][j] = dp[i-1][j-1] + 1 if  nums[i-1] == nums2[j-1]
	m := len(nums1)
	n := len(nums2)

	dp := make([][]int, m+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
	}

	res := 0

	for i := 1; i <= m; i++ {
		for j := 1; j <= n; j++ {
			if nums1[i-1] == nums2[j-1] {
				dp[i][j] = dp[i-1][j-1] + 1

				if dp[i][j] > res {
					res = dp[i][j]
				}
			}
		}
	}
	return res
}
