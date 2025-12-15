package dynamicplan

import "testing"

func knapsack(wgt []int, val []int, cap int) int {
	/*
		给定 n 个物品，第 i 个物品的重量为 wgt[i-1]、价值为 val[i-1]，和一个容量为 cap 的背包。每个物品只能选择一次，问在限定背包容量下能放入物品的最大价值。
	*/
	// 是否动态规划问题
	// 1. 判断是否决策树问题：对于物品 i 可以选择放入或不放入
	// 2. 是否计算最值：是
	// 3. 当前步骤是否可以通过前面状态转换：如果物品 i 不放入，则可以取前 i - 1 物品的最大价值

	// 决策、定义状态、dp
	// dp[i, c] 表示对 i 物品处理，最大容量为 c的情况下，val 是最大价值

	// 最优子结构、状态转换方程
	// dp[i, c] 如果不选择 i，则等于 dp[i - 1, c], 选择 i, 则等于 dp[i-1, c-wgt[i-1]] + val[i-1]

	// 边界条件
	// dp[0, c] = 0, dp[i, 0] = 0

	m := len(wgt)

	dp := make([][]int, m+1)
	for i := 0; i < m+1; i++ {
		dp[i] = make([]int, cap+1)
	}

	// 边界条件，已经默认为0

	// 最优子结构、状态转换
	for i := 1; i < m+1; i++ {
		for j := 1; j < cap+1; j++ {
			if wgt[i-1] <= j {
				dp[i][j] = maxInt(dp[i-1][j], dp[i-1][j-wgt[i-1]]+val[i-1])
			} else {
				dp[i][j] = dp[i-1][j]
			}
		}
	}
	return dp[m][cap]
}

func knapsackV2(wgt []int, val []int, cap int) int {
	/*
		空间优化

		改为一维数组，维度为原本的列数，就是cap+1

		因为当前行数据只依赖上一行的结果、当前行前一列的数据，不需要存储上一行其他列的数据
	*/
	m := len(wgt)
	dp := make([]int, cap+1)

	for i := 1; i < m+1; i++ {
		// 逆序，避免覆盖问题，i行数据只能依赖i-1行数据（不能重复选），而不能依赖同行前几列的数据
		for j := cap; j >= wgt[i-1]; j-- {
			dp[j] = maxInt(dp[j], dp[j-wgt[i-1]]+val[i-1])
		}
	}
	return dp[cap]
}

func unboundedKnapsack(wgt []int, val []int, cap int) int {
	/*
		给定 n 个物品，第 i 个物品的重量为 wgt[i-1]、价值为 val[i-1]，和一个容量为 cap 的背包。
		每个物品可以重复选取，问在限定背包容量下能放入物品的最大价值。
	*/
	// 允许重复选取第 i 个物品
	m := len(wgt)
	dp := make([][]int, m+1)
	for i := 0; i < m+1; i++ {
		dp[i] = make([]int, cap+1)
	}
	for i := 1; i < m+1; i++ {
		for j := 1; j < cap+1; j++ {
			if wgt[i-1] <= j {
				dp[i][j] = maxInt(dp[i-1][j], dp[i][j-wgt[i-1]]+val[i-1])
			} else {
				dp[i][j] = dp[i-1][j]
			}
		}
	}
	return dp[m][cap]
}

func unboundedKnapsackV2(wgt []int, val []int, cap int) int {
	// 空间优化，允许重复，顺序遍历
	dp := make([]int, cap+1)
	m := len(wgt)

	for i := 1; i < m+1; i++ {
		for j := wgt[i-1]; j < cap+1; j++ {
			dp[j] = maxInt(dp[j], dp[j-wgt[i-1]]+val[i-1])
		}
	}
	return dp[cap]
}

func maxInt(x int, y int) int {
	if x > y {
		return x
	}
	return y
}

func TestKnapsack(t *testing.T) {
	tests := []struct {
		name     string
		wgt      []int
		val      []int
		cap      int
		expected int
	}{
		{
			name:     "基本测试用例1",
			wgt:      []int{1, 2, 3},
			val:      []int{6, 10, 12},
			cap:      5,
			expected: 22, // 选择物品1和物品3: 6 + 12 = 18, 或选择物品2和物品3: 10 + 12 = 22
		},
		{
			name:     "基本测试用例2",
			wgt:      []int{2, 3, 4, 5},
			val:      []int{3, 4, 5, 6},
			cap:      8,
			expected: 10, // 选择物品2和物品4: 4 + 6 = 10
		},
		{
			name:     "经典01背包问题",
			wgt:      []int{2, 3, 4, 5},
			val:      []int{3, 4, 5, 7},
			cap:      9,
			expected: 12, // 选择物品2和物品4: 4 + 7 = 11, 或选择物品1、物品2和物品3: 3 + 4 + 5 = 12
		},
		{
			name:     "容量为0",
			wgt:      []int{1, 2, 3},
			val:      []int{6, 10, 12},
			cap:      0,
			expected: 0,
		},
		{
			name:     "空物品列表",
			wgt:      []int{},
			val:      []int{},
			cap:      10,
			expected: 0,
		},
		{
			name:     "容量小于所有物品重量",
			wgt:      []int{5, 6, 7},
			val:      []int{10, 20, 30},
			cap:      3,
			expected: 0,
		},
		{
			name:     "所有物品都能放入",
			wgt:      []int{1, 2, 3},
			val:      []int{5, 10, 15},
			cap:      10,
			expected: 30, // 所有物品都放入: 5 + 10 + 15 = 30
		},
		{
			name:     "单个物品",
			wgt:      []int{5},
			val:      []int{10},
			cap:      5,
			expected: 10,
		},
		{
			name:     "单个物品但容量不足",
			wgt:      []int{5},
			val:      []int{10},
			cap:      3,
			expected: 0,
		},
		{
			name:     "价值相同但重量不同",
			wgt:      []int{1, 2, 3, 4},
			val:      []int{10, 10, 10, 10},
			cap:      5,
			expected: 20, // 选择重量最小的两个: 1 + 2 = 3, 价值 = 10 + 10 = 20
		},
		{
			name:     "重量相同但价值不同",
			wgt:      []int{2, 2, 2, 2},
			val:      []int{1, 3, 5, 7},
			cap:      6,
			expected: 15, // 选择价值最高的三个: 5 + 7 + 3 = 15
		},
		{
			name:     "需要精确选择",
			wgt:      []int{1, 3, 4},
			val:      []int{15, 20, 30},
			cap:      4,
			expected: 35, // 选择物品1和物品2: 15 + 20 = 35
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := knapsack(tt.wgt, tt.val, tt.cap)
			if result != tt.expected {
				t.Errorf("knapsack() = %v, want %v", result, tt.expected)
			}
		})
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := knapsackV2(tt.wgt, tt.val, tt.cap)
			if result != tt.expected {
				t.Errorf("knapsackV2() = %v, want %v", result, tt.expected)
			}
		})
	}
}

func TestUnboundedKnapsack(t *testing.T) {
	tests := []struct {
		name     string
		wgt      []int
		val      []int
		cap      int
		expected int
	}{
		{
			name:     "基本测试用例-重复选择",
			wgt:      []int{1, 2, 3},
			val:      []int{6, 10, 12},
			cap:      5,
			expected: 30, // 选择5个物品1: 5 * 6 = 30
		},
		{
			name:     "重复选择高价值物品",
			wgt:      []int{2, 3, 4, 5},
			val:      []int{3, 4, 5, 6},
			cap:      8,
			expected: 12, // 选择4个物品1: 4 * 3 = 12
		},
		{
			name:     "混合选择",
			wgt:      []int{2, 3, 4},
			val:      []int{1, 4, 5},
			cap:      7,
			expected: 9, // 选择1个物品2和1个物品3: 4 + 5 = 9
		},
		{
			name:     "完全重复选择最优物品",
			wgt:      []int{1, 3, 4},
			val:      []int{15, 20, 30},
			cap:      4,
			expected: 60, // 选择4个物品1: 4 * 15 = 60
		},
		{
			name:     "容量为0",
			wgt:      []int{1, 2, 3},
			val:      []int{6, 10, 12},
			cap:      0,
			expected: 0,
		},
		{
			name:     "空物品列表",
			wgt:      []int{},
			val:      []int{},
			cap:      10,
			expected: 0,
		},
		{
			name:     "容量小于所有物品重量",
			wgt:      []int{5, 6, 7},
			val:      []int{10, 20, 30},
			cap:      3,
			expected: 0,
		},
		{
			name:     "单个物品重复选择",
			wgt:      []int{2},
			val:      []int{5},
			cap:      8,
			expected: 20, // 选择4个物品: 4 * 5 = 20
		},
		{
			name:     "单个物品但容量不足",
			wgt:      []int{5},
			val:      []int{10},
			cap:      3,
			expected: 0,
		},
		{
			name:     "价值密度高的物品重复选择",
			wgt:      []int{1, 2, 3, 4},
			val:      []int{10, 10, 10, 10},
			cap:      5,
			expected: 50, // 选择5个重量为1的物品: 5 * 10 = 50
		},
		{
			name:     "经典完全背包问题",
			wgt:      []int{2, 3, 4, 5},
			val:      []int{3, 4, 5, 7},
			cap:      9,
			expected: 13, // 选择1个物品4(重量5)和2个物品1(重量2*2=4): 7 + 2*3 = 13
		},
		{
			name:     "需要精确计算重复次数",
			wgt:      []int{3, 4},
			val:      []int{4, 5},
			cap:      10,
			expected: 13, // 选择2个物品1和1个物品2: 2*3 + 4 = 10，价值2*4 + 5 = 13
		},
		{
			name:     "最优解是重复选择同一物品",
			wgt:      []int{2, 3, 5},
			val:      []int{3, 4, 6},
			cap:      10,
			expected: 15, // 选择5个物品1: 5 * 3 = 15
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := unboundedKnapsack(tt.wgt, tt.val, tt.cap)
			if result != tt.expected {
				t.Errorf("unboundedKnapsack() = %v, want %v", result, tt.expected)
			}
		})
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := unboundedKnapsackV2(tt.wgt, tt.val, tt.cap)
			if result != tt.expected {
				t.Errorf("unboundedKnapsackV2() = %v, want %v", result, tt.expected)
			}
		})
	}
}
