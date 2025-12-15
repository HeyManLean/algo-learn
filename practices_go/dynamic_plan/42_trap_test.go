package dynamicplan

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
	// 方案：第 i 个位置能接的雨水，等于它左边最高柱子和右边最高柱子的最小值，减去 i 的高度

	n := len(height)
	// 找出 i 左边最高柱子
	leftMax := 0

	left := make([]int, n)
	for i := 0; i < n; i++ {
		left[i] = leftMax
		if height[i] > leftMax {
			leftMax = height[i]
		}
	}

	// 找出 i 右边最高柱子
	rightMax := 0
	right := make([]int, n)
	for i := n - 1; i >= 0; i-- {
		right[i] = rightMax
		if height[i] > rightMax {
			rightMax = height[i]
		}
	}

	// 计算每个位置雨水，并累加
	waterSum := 0
	for i, h := range height {
		min := left[i]
		if right[i] < min {
			min = right[i]
		}
		water := min - h
		if water > 0 {
			waterSum += water
		}
	}

	return waterSum
}
