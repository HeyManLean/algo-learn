package bytedance

func trap(height []int) int {
	/*
		42. 接雨水
		给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

		输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
		输出：6
		解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

		https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/rainwatertrap.png

		输入：height = [4,2,0,3,2,5]
		输出：9
	*/
	// 当前位置能接的雨水，等于左右两边最高柱子，最矮的柱子高度 - 当前位置的高度
	// 两个数组，分别维护当前位置左边或右边的最高柱子（不包含当前位置）
	if len(height) == 0 {
		return 0
	}
	n := len(height)
	left := make([]int, n)
	right := make([]int, n)

	var min = func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}

	lMax := 0
	for i := 0; i < n; i++ {
		left[i] = lMax
		if height[i] > lMax {
			lMax = height[i]
		}
	}
	rMax := 0
	for i := n - 1; i >= 0; i-- {
		right[i] = rMax
		if height[i] > rMax {
			rMax = height[i]
		}
	}
	res := 0
	for i := 0; i < n-1; i++ {
		water := min(left[i], right[i]) - height[i]
		if water > 0 {
			res += water
		}
	}
	return res
}
