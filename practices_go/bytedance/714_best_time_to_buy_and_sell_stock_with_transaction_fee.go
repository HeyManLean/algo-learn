package bytedance

func maxProfit(prices []int, fee int) int {
	/*
		714. 买卖股票的最佳时机含手续费

		给定一个整数数组 prices，其中 prices[i] 表示第 i 天的股票价格；整数 fee 代表了交易股票的手续费用。
		你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
		返回获得利润的最大值。
		注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

		输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
		输出: 8
		解释: 能够达到最大利润:
		在此处买入 prices[0] = 1
		在此处卖出 prices[3] = 8
		在此处买入 prices[4] = 4
		在此处卖出 prices[5] = 9
		总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8

		输入: prices = [1, 3, 7, 5, 10, 3], fee = 3
		输出: 6

		1 <= prices.length <= 5 * 10^4
		1 <= prices[i] < 5 * 10^4
		0 <= fee < 5 * 10^4
	*/
	// 买入：等于卖出的价格最大值-当前买入金额-手续费
	// 卖出：等于买入的价格最大值+当前卖出金额-手续费
	// buy[i] 表示第i次购买，可能在0-n位置
	// sell[i] 表示第i次卖出，可能在0-n位置

	n := len(prices)

	// 持股和没持股两个状态
	cash := 0 // 没持股
	hold := -prices[0]

	for i := 1; i < n; i++ {
		preCash := cash

		// 卖出
		if hold+prices[i]-fee > cash {
			cash = hold + prices[i] - fee
		}

		// 买入或不买
		if preCash-prices[i] > hold {
			hold = preCash - prices[i]
		}
	}
	return cash
}
