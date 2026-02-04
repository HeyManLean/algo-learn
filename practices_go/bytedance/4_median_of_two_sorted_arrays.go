package bytedance

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	/*
		4. 寻找两个正序数组的中位数

		给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

		算法的时间复杂度应该为 O(log (m+n)) 。


		示例 1：
		输入：nums1 = [1,3], nums2 = [2]
		输出：2.00000
		解释：合并数组 = [1,2,3] ，中位数 2

		示例 2：
		输入：nums1 = [1,2], nums2 = [3,4]
		输出：2.50000
		解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5


		nums1.length == m
		nums2.length == n
		0 <= m <= 1000
		0 <= n <= 1000
		1 <= m + n <= 2000
		-10^6 <= nums1[i], nums2[i] <= 10^6
	*/
	// 双指针，分别指向两个数组左侧，向前遍历，找到中位数
	m := len(nums1)
	n := len(nums2)

	k := (m + n) / 2 // 找到k和k+1，然后根据单双数求中位数
	i, j := 0, 0

	var mList = []int{0, 0}

	for i+j < k+1 {
		val := 0
		if i < m && j < n {
			if nums1[i] <= nums2[j] {
				val = nums1[i]
				i++
			} else {
				val = nums2[j]
				j++
			}
		} else if i < m {
			val = nums1[i]
			i++
		} else {
			val = nums2[j]
			j++
		}
		if i+j == k {
			mList[0] = val
		} else if i+j == k+1 {
			mList[1] = val
		}
	}

	if (m+n)%2 == 0 {
		return float64(mList[0]+mList[1]) / 2
	}
	return float64(mList[1])
}
