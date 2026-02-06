package bytedance

func kInversePairs(n int, k int) int {
	/*
		629. K个逆序对数组

		给定两个整数 n 和 k，找出有多少个不同的数组，由1到n的数字组成，恰好包含k个逆序对。

		逆序对定义：对于数组中第i个和第j个元素，如果 i < j 且 a[i] > a[j]，则它们组成一个逆序对。

		由于答案可能很大，需要对 10^9 + 7 取模。

		示例 1:
		输入: n = 3, k = 0
		输出: 1
		解释:
		只有数组 [1,2,3] 包含了从1到3的整数并且正好有 0 个逆序对。

		示例 2:
		输入: n = 3, k = 1
		输出: 2
		解释:
		数组 [1,3,2] 和 [2,1,3] 都有 1 个逆序对。

		说明:
		n 的范围是 [1, 1000] 并且 k 的范围是 [0, 1000]。
	*/
	if k == 0 {
		return 1
	}
	// dp[i][j] 表示，前 i 个字符，包含j个逆序对的数组数量
	// 当处理完 i-1 字符后，处理第i个字符时
	// 如果插入末尾，新增0个逆序对 dp[i-1][j]，插到倒数第一位，新增一个逆序对 dp[i-1][j-1]，以此类推最大往前推 x = min(j,i-1)步骤，直到 dp[i-1][j-x]
	// dp[i][j] = dp[i-1][j] + dp[i-1][j-1] ... dp[i-1][j-x],  x=[0, min(j,i-1)]
	// prefix[t] = dp[i-1][0..t] , 那么 dp[i-1][j-x] = prefix[j] - prefix[x]

	// 降维，dp[j] = dp[j-1] + prefix[j] (-prefix[j-i])

	prev := make([]int, k+1) // 表示前缀和
	prev[0] = 1
	MOD := 1000000007

	for i := 1; i <= n; i++ {
		cur := make([]int, k+1)
		cur[0] = 1
		for j := 1; j <= k; j++ {
			// 上一行的前缀和 1~j个字符
			cur[j] = cur[j-1] + prev[j]
			if j >= i { // 最大只能有 min(j, i) 个逆序对
				cur[j] -= prev[j-i] // 保留i个数字
			}

			cur[j] %= MOD
			if cur[j] < 0 {
				cur[j] += MOD
			}
		}
		prev = cur
	}

	return prev[k]
}
