package dynamicplan

func getMaxMatrix(matrix [][]int) []int {
	/*
		面试题 17.24. 最大子矩阵

		给定一个正整数、负整数和 0 组成的 N × M 矩阵，编写代码找出元素总和最大的子矩阵。
		返回一个数组 [r1, c1, r2, c2]，其中 r1, c1 分别代表子矩阵左上角的行号和列号，r2, c2 分别代表右下角的行号和列号。若有多个满足条件的子矩阵，返回任意一个均可。


		输入：
		[
		   [-1,0],
		   [0,-1]
		]
		输出：[0,1,0,1]
		解释：输入中标粗的元素即为输出所表示的矩阵

	*/
	// 最大子数组和：如果前缀和为负数，则从当前位置开始重新计算

	// 通过遍历 上边界和下边界，通过遍历当前行，记录每一列长度，转换成一维数组的最大子数组和
	m := len(matrix)
	n := len(matrix[0])
	maxSum := matrix[0][0]
	res := []int{0, 0, 0, 0}

	for top := 0; top < m; top++ {
		colSum := make([]int, n) // 表示在上下边界之间，每一列的和
		for bottom := top; bottom < m; bottom++ {
			for col := 0; col < n; col++ {
				colSum[col] += matrix[bottom][col]
			}
			// 第一列
			subSum := colSum[0]
			left := 0
			if colSum[0] > maxSum {
				maxSum = colSum[0]
				res = []int{top, 0, bottom, 0}
			}

			// 子数组和
			for col := 1; col < n; col++ {
				if subSum < 0 {
					subSum = colSum[col]
					left = col
				} else {
					subSum += colSum[col]
				}

				if subSum > maxSum {
					maxSum = subSum
					res = []int{top, left, bottom, col}
				}
			}
		}
	}

	return res
}
