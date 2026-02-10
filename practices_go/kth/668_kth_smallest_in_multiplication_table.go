package bytedance

func findKthNumber(m int, n int, k int) int {
	/*
		668. 乘法表中第k小的数

		几乎每一个人都用 乘法表。但是你能在乘法表中快速找到第 k 小的数字吗？

		乘法表是大小为 m x n 的一个整数矩阵，其中 mat[i][j] == i * j（下标从 1 开始）。

		给你三个整数 m、n 和 k，请你在大小为 m x n 的乘法表中，找出并返回第 k 小的数字。

		示例 1：
		输入：m = 3, n = 3, k = 5
		输出：3
		解释：第 5 小的数字是 3 。
		乘法表:
		1	2	3
		2	4	6
		3	6	9

		示例 2：
		输入：m = 2, n = 3, k = 6
		输出：6
		解释：第 6 小的数字是 6 。
		乘法表:
		1	2	3
		2	4	6

		提示：
		1 <= m, n <= 3 * 10^4
		1 <= k <= m * n
	*/
	// 二分法，0~m*n，直到小于mid的数量，如果<=k，则往左边，否则往右边
	// 计算小于mid的数量，从第一行开始，计算列数 min(n, mid/i) 第i行的数值是: i, 2i, 3i, ...
	var min = func(a, b int) int {
		if a < b {
			return a
		}
		return b
	}

	left, right := 0, m*n
	for left < right {
		mid := (left + right) / 2

		cnt := 0
		for i := 1; i <= m; i++ {
			cnt += min(n, mid/i)
		}

		if cnt >= k {
			right = mid
		} else {
			left = mid + 1
		}
	}
	return left
}
