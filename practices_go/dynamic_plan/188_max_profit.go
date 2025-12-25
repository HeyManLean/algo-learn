package dynamicplan

func maxProfit4(k int, prices []int) int {
	/*
	   188. 买卖股票的最佳时机 IV

	   给你一个整数数组 prices 和一个整数 k ，其中 prices[i] 是某支给定的股票在第 i 天的价格。
	   设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。也就是说，你最多可以买 k 次，卖 k 次。

	   注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

	   输入：k = 2, prices = [2,4,1]
	   输出：2
	   解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。

	   输入：k = 2, prices = [3,2,6,5,0,3]
	   输出：7
	   解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
	   随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。

	*/
	if k == 0 || len(prices) == 0 {
		return 0
	}
	// 卖出依赖于前一次买入的最大利润
	// 状态，buy[i] 表示第i次购买
	// 状态，sell[i] 表示第i次卖出
	buy := make([]int, k+1)
	sell := make([]int, k+1)

	for i := 1; i <= k; i++ {
		buy[i] = -prices[0]
	}

	n := len(prices)
	for i := 1; i < n; i++ {
		for j := 1; j <= k; j++ {
			buy[j] = maxP(buy[j], sell[j-1]-prices[i])
			sell[j] = maxP(sell[j], buy[j]+prices[i])
		}
	}
	return sell[k]
}

func maxP(x, y int) int {
	if x > y {
		return x
	}
	return y
}
