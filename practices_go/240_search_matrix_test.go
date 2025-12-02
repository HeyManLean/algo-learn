package practicesgo

func searchMatrix(matrix [][]int, target int) bool {
	/*
		240. 搜索二维矩阵 II

		编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

		每行的元素从左到右升序排列。
		每列的元素从上到下升序排列。

		输入：matrix = [
			[ 1, 4, 7,11,15],
			[ 2, 5, 8,12,19],
			[ 3, 6, 9,16,22],
			[10,13,14,17,24],
			[18,21,23,26,30]
		], target = 5
		输出：true
	*/
	// z 字搜索法，从右上角开始，如果当前值大于target，则往左，小于target则往下
	m := len(matrix)
	n := len(matrix[0])

	i := 0
	j := n - 1

	for i < m && j >= 0 {
		if matrix[i][j] == target {
			return true
		} else if matrix[i][j] > target {
			j--
		} else {
			i++
		}
	}
	return false
}
