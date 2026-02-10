package bytedance

func longestOnes(nums []int, k int) int {
	/*
		1004. 最大连续1的个数 III

		给定一个二进制数组 nums 和一个整数 k，如果可以翻转最多 k 个 0 ，则返回数组中连续 1 的最大个数。

		示例 1：
		输入: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
		输出: 6
		解释: [1,1,1,0,0,1,1,1,1,1,1]
		粗体数字从 0 翻转到 1，最长的子数组长度为 6。

		示例 2：
		输入: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
		输出: 10
		解释: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
		粗体数字从 0 翻转到 1，最长的子数组长度为 10。

		1 <= nums.length <= 10^5
		nums[i] 不是 0 就是 1
		0 <= k <= nums.length
	*/
	// 滑动窗口，右边延伸，遇到0，则k减一，直到k为0且右边是0，开始左边前进，遇到0，则k加一，则此时开始延伸右边
	left, n := 0, len(nums)
	ans := 0

	// 反过来计算 0的个数
	cnt := 0
	for right := 0; right < n; right++ {
		if nums[right] == 0 {
			cnt++
		}

		for cnt > k {
			if nums[left] == 0 {
				cnt--
			}
			left++
		}
		if right-left+1 > ans {
			ans = right - left + 1
		}
	}

	return ans
}
