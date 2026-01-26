package dynamicplan

func minimumTotal(triangle [][]int) int {
	/*
		120. 三角形最小路径和

		给定一个三角形 triangle，找出自顶向下的最小路径和。

		每一步只能移动到下一行中相邻的结点上。相邻的结点在这里指的是下标与上一层结点下标相同或者等于上一层结点下标 + 1 的两个结点。
		也就是说，如果正位于当前行的下标 i，那么下一步可以移动到下一行的下标 i 或 i + 1。

		输入: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
		输出: 11
		解释: 如下面简图所示：
		   2
		  3 4
		 6 5 7
		4 1 8 3
		自顶向下的最小路径和为 2 + 3 + 5 + 1 = 11（加粗部分）。

		输入: triangle = [[-10]]
		输出: -10

		1 <= triangle.length <= 200
		triangle[0].length == 1
		triangle[i].length == triangle[i - 1].length + 1
		-10^4 <= triangle[i][j] <= 10^4
	*/
	// dp[j] 表示，以第j个字符为终点的最小路径和
	// i<=最后一行长度
	// dp[j] = min(dp[j] + triangle[i][j], dp[j-1] + triangle[i][j])  // 上一行的同坐标或前一个坐标
	n := len(triangle[len(triangle)-1])
	dp := make([]int, n)

	var min = func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}

	dp[0] = triangle[0][0]
	for i := 1; i < len(triangle); i++ {
		// 依赖上一行的 dp[j-1], 逆序
		for j := len(triangle[i]) - 1; j >= 0; j-- {
			v := triangle[i][j]
			// 不能把上一行的记录
			if j == len(triangle[i])-1 {
				dp[j] = dp[j-1] + v
			} else if j > 0 {
				dp[j] = min(dp[j], dp[j-1]) + v
			} else {
				dp[j] = dp[j] + v
			}
		}
	}
	res := dp[0]
	for _, v := range dp {
		res = min(v, res)
	}
	return res
}
