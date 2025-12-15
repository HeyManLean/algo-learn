package dynamicplan

func maximalRectangle(matrix [][]byte) int {
	/*
		85. 最大矩形
		给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

		输入：matrix = [
			["1","0","1","0","0"],
			["1","0","1","1","1"],
			["1","1","1","1","1"],
			["1","0","0","1","0"]
		]
		输出：6

		输入：matrix = [["0"]]
		输出：0

		输入：matrix = [["1"]]
		输出：1
	*/

	// 每遍历一行，则记录当前列的高度，如果为0，则高度为0
	// 然后通过单调栈记录当前的最大矩阵
	m := len(matrix)
	n := len(matrix[0])

	heights := make([]int, n)

	max := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if matrix[i][j] == '0' {
				heights[j] = 0
			} else {
				heights[j] += 1
			}
		}
		max = maxArea(max, calcArea(heights))
	}
	return max
}

func calcArea(heights []int) int {
	// 单调栈
	stack := []int{-1} // 避免超过边界
	heights = append(heights, 0)
	n := len(heights)

	max := 0
	for i := 0; i < n; i++ {
		// 单调栈，栈顶前面没有值的位置都大于栈顶高度的，所以用栈顶高度，左边界是新栈顶+1，右边界是 i-1
		for stack[len(stack)-1] != -1 && heights[i] < heights[stack[len(stack)-1]] {
			// 计算面积
			h := heights[stack[len(stack)-1]]
			stack = stack[:len(stack)-1]
			w := i - 1 - stack[len(stack)-1]

			max = maxArea(max, h*w)
		}
		stack = append(stack, i)
	}

	return max
}

func maxArea(x, y int) int {
	if x > y {
		return x
	}
	return y
}
