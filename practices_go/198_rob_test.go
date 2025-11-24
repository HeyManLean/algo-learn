package practicesgo

import (
	"fmt"
	"testing"
)

func rob(nums []int) int {
	/*
		198. 打家劫舍
		你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
		影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
		给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

		输入：[1,2,3,1]
		输出：4
		解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
		     偷窃到的最高金额 = 1 + 3 = 4 。

		输入：[2,7,9,3,1]
		输出：12
		解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
		     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

	*/

	// 简述：给定一个整型数组，从中选择一组数值和最大，限制：选取数值不能相邻。
	// dp[i] 表示选择了位置 i 的前面最大金额
	// dp[i] = max(dp[i - 2] + dp[i], dp[i - 3] + dp[i])
	// 因为是非负数组，dp[i - 2] 已经包含了 dp[i - 4] 的考虑
	dp := make([]int, len(nums))
	max := 0
	for i := 0; i < len(nums); i++ {
		if i < 2 {
			dp[i] = nums[i]
		} else {
			dp[i] = nums[i] + dp[i-2]
			if i >= 3 && nums[i]+dp[i-3] > dp[i] {
				dp[i] = nums[i] + dp[i-3]
			}
		}
		if dp[i] > max {
			max = dp[i]
		}
	}
	return max
}

func Test_Rob(t *testing.T) {
	// 定义测试用例结构体
	testCases := []struct {
		name     string // 测试用例名称
		input    []int  // 输入参数
		expected int    // 期望输出
	}{
		{
			name:     "示例1: [1,2,3,1]",
			input:    []int{1, 2, 3, 1},
			expected: 4,
		},
		{
			name:     "示例2: [2,7,9,3,1]",
			input:    []int{2, 7, 9, 3, 1},
			expected: 12,
		},
		{
			name:     "单个房屋",
			input:    []int{5},
			expected: 5,
		},
		{
			name:     "两个房屋",
			input:    []int{1, 2},
			expected: 2,
		},
		{
			name:     "空数组",
			input:    []int{},
			expected: 0,
		},
	}

	// 遍历测试用例
	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			// 执行函数
			actual := rob(tc.input)

			// 对比结果并报错
			if actual != tc.expected {
				t.Errorf("测试失败 %s\n输入: %v\n期望输出: %d\n实际输出: %d",
					tc.name, tc.input, tc.expected, actual)
			} else {
				fmt.Printf("✓ 测试通过: %s, 输入=%v, 输出=%d\n", tc.name, tc.input, actual)
			}
		})
	}
}
