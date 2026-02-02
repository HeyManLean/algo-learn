package bytedance

func fourSumCount(nums1 []int, nums2 []int, nums3 []int, nums4 []int) int {
	/*
		454. 四数相加 II

		给你四个整数数组 nums1、nums2、nums3 和 nums4 ，数组长度都是 n ，请你计算有多少个元组 (i, j, k, l) 能满足：

		0 <= i, j, k, l < n
		nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

		输入：nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
		输出：2
		解释：两个元组如下：
		(0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
		(1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0

		输入：nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
		输出：1

		n == nums1.length == nums2.length == nums3.length == nums4.length
		1 <= n <= 200
		-2^28 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2^28
	*/
	// 不限制重复
	// 暴力法
	ans := 0
	countAB := map[int]int{}
	for _, v := range nums1 {
		for _, w := range nums2 {
			countAB[v+w]++
		}
	}
	for _, v := range nums3 {
		for _, w := range nums4 {
			ans += countAB[-v-w]
		}
	}
	return ans
}
