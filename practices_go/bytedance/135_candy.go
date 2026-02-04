package bytedance

func candy(ratings []int) int {
	/*
		135. 分发糖果

		n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。

		你需要按照以下要求，给这些孩子分发糖果：
		1. 每个孩子至少分配到 1 个糖果。
		2. 相邻两个孩子评分更高的孩子会获得更多的糖果。

		请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。

		示例 1：
		输入：ratings = [1,0,2]
		输出：5
		解释：你可以分别给第一个、第二个、第三个孩子分发 2、1、2 颗糖果。

		示例 2：
		输入：ratings = [1,2,2]
		输出：4
		解释：你可以分别给第一个、第二个、第三个孩子分发 1、2、1 颗糖果。
		     第三个孩子只得到 1 颗糖果，这满足题面中的两个条件。

		n == ratings.length
		1 <= n <= 2 * 10^4
		0 <= ratings[i] <= 2 * 10^4
	*/
	// 如 1,5,4,3   1,2,1 处理3的时候，需要将5,4（1和3之间）都加1

	n := len(ratings)

	// 贪心算法，先全部设为1，然后从左到右，将大于前面的值设为前面值+1
	// 从右到左，将大于后面的值设为后面值+1

	candies := make([]int, n)
	for i := range candies {
		candies[i] = 1
	}

	for i := 1; i < n; i++ {
		if ratings[i] > ratings[i-1] {
			candies[i] = candies[i-1] + 1
		}
	}

	for i := n - 2; i >= 0; i-- {
		if ratings[i] > ratings[i+1] {
			need := candies[i+1] + 1
			if need > candies[i] {
				candies[i] = need
			}
		}
	}
	res := 0
	for _, c := range candies {
		res += c
	}
	return res
}
