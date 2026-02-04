package bytedance

func maxSlidingWindow(nums []int, k int) []int {
	/*
		239. 滑动窗口最大值

		给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

		返回 滑动窗口中的最大值 。


		示例 1：
		输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
		输出：[3,3,5,5,6,7]
		解释：
		滑动窗口的位置                最大值
		---------------               -----
		[1  3  -1] -3  5  3  6  7       3
		 1 [3  -1  -3] 5  3  6  7       3
		 1  3 [-1  -3  5] 3  6  7       5
		 1  3  -1 [-3  5  3] 6  7       5
		 1  3  -1  -3 [5  3  6] 7       6
		 1  3  -1  -3  5 [3  6  7]      7

		示例 2：
		输入：nums = [1], k = 1
		输出：[1]


		1 <= nums.length <= 10^5
		-10^4 <= nums[i] <= 10^4
		1 <= k <= nums.length
	*/
	// 不能通过滑动窗口方式，因为窗口有相同值，无法确认左边的值是否多个，除非计数
	// 单调递减栈，从大到小，遇到比栈顶更大或相等的，则循环移除栈顶，左边就是最大值
	n := len(nums)
	stack := []int{}
	res := []int{}

	for i := 0; i < n; i++ {
		// 如果i大于等于k，则需要判断左侧是否等于nums[k-i]，并移除
		if i >= k && nums[i-k] == stack[0] {
			stack = stack[1:]

		}
		// 如果i小于k，则往栈添加
		for len(stack) > 0 && nums[i] > stack[len(stack)-1] {
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, nums[i])
		if i >= k-1 {
			res = append(res, stack[0])
		}

	}
	return res
}
