package bytedance

func largestRectangleArea(heights []int) int {
	/*
		84. 柱状图中最大的矩形

		给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

		求在该柱状图中，能够勾勒出来的矩形的最大面积。


		示例 1:

		输入：heights = [2,1,5,6,2,3]
		输出：10
		解释：最大的矩形为图中红色区域，面积为 10

		示例 2：

		输入： heights = [2,4]
		输出： 4


		提示：

		1 <= heights.length <= 10^5
		0 <= heights[i] <= 10^4
	*/
	// 单调递增栈，遇到更小的，先将栈顶移除，栈顶元素高度*（栈顶位置-新栈顶位置）
	h := make([]int, 0, len(heights)+2)
	h = append(h, 0)
	h = append(h, heights...)
	h = append(h, 0) // 避免超过stack长度

	res := 0
	stack := []int{}

	for i := 0; i < len(h); i++ {
		for len(stack) > 0 && h[i] < h[stack[len(stack)-1]] {
			top := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			left := stack[len(stack)-1]
			area := (i - left - 1) * h[top] // 当前位置往前
			if area > res {
				res = area
			}
		}
		stack = append(stack, i)
	}
	return res
}
