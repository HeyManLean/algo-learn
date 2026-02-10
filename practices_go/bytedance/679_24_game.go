package bytedance

import "math"

func judgePoint24(cards []int) bool {
	/*
		679. 24 点游戏

		给定一个长度为 4 的整数数组 cards，其中 cards[i] 的取值范围为 [1, 9]。
		你需要使用运算符 ['+', '-', '*', '/'] 和括号，将这四个数字排列成数学表达式，使得其计算结果为 24。

		规则：
		- 除法 '/' 表示实数除法，而非整数除法（例如 4 / (1 - 2/3) = 12）
		- 每个运算都必须发生在两个数字之间，你不能将 '-' 作为一元运算符使用
		- 不能将数字串联在一起（例如 "12 + 12" 无效）
		- 如果可以得到 24，返回 true，否则返回 false

		示例 1：
		输入: cards = [4,1,8,7]
		输出: true
		解释: (8-4) * (7-1) = 24

		示例 2：
		输入: cards = [1,2,1,2]
		输出: false

		示例 3：
		输入: cards = [3,3,8,8]
		输出: true
		解释: 8 / (3 - 8/3) = 24

		cards.length == 4
		1 <= cards[i] <= 9
	*/
	// 回溯
	// 从数组，选择两个数组，加减乘除，分别加入新的数组，并将其余数字加入新的数组，对每个新的数组进行回溯，直到相等
	const target = 24.0
	const eps = 1e-6

	nums := make([]float64, 0, 4)
	for _, v := range cards {
		nums = append(nums, float64(v))
	}

	var dfs func(arr []float64) bool
	dfs = func(arr []float64) bool {
		if len(arr) == 1 {
			return math.Abs(arr[0]-target) < eps
		}
		n := len(arr)

		for i := 0; i < n-1; i++ {
			for j := i + 1; j < n; j++ {
				rest := make([]float64, 0, n)
				for k := 0; k < n; k++ {
					if k != i && k != j {
						rest = append(rest, arr[k])
					}
				}

				a, b := arr[i], arr[j]

				cands := make([]float64, 0, 6)
				cands = append(cands, a+b)
				cands = append(cands, a*b)
				cands = append(cands, a-b)
				cands = append(cands, b-a)

				if math.Abs(b) > eps {
					cands = append(cands, a/b)
				}
				if math.Abs(a) > eps {
					cands = append(cands, b/a)
				}
				for _, c := range cands {
					next := append(rest, c)
					if dfs(next) {
						return true
					}
				}

			}
		}
		return false

	}

	return dfs(nums)
}
