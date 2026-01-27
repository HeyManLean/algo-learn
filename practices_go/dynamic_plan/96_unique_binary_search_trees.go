package dynamicplan

func numTrees(n int) int {
	/*
		96. 不同的二叉搜索树

		给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？
		返回满足题意的二叉搜索树的种数。

		示例 1：
		输入：n = 3
		输出：5

		示例 2：
		输入：n = 1
		输出：1

		1 <= n <= 19
	*/
	// dp[i] 表示有i个字符的字符的树数量
	// dp[i] = sum(dp[i-j-1] * dp[j] for j < i) // 分界点有一个
	dp := make([]int, n+1)
	dp[1] = 1
	dp[0] = 1
	for i := 2; i <= n; i++ {
		for j := 0; j < i; j++ {
			dp[i] += dp[i-j-1] * dp[j]
		}
	}
	return dp[n]
}
