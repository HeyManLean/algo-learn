package dynamicplan

import (
	"math"
	"strconv"
)

func atMostNGivenDigitSet(digits []string, n int) int {
	/*
		902. 最大为 N 的数字组合

		给定一个按 非递减顺序 排列的数字数组 digits 。你可以用任意次数 digits[i] 来写的数字。
		例如，如果 digits = ['1','3','5']，我们可以写数字，如 '13', '551', 和 '1351315'。

		返回 可以生成的小于或等于给定整数 n 的正整数的个数 。


		输入：digits = ["1","3","5","7"], n = 100
		输出：20
		解释：
		可写出的 20 个数字是：
		1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.

		输入：digits = ["1","4","9"], n = 1000000000
		输出：29523
		解释：
		我们可以写 3 个一位数字，9 个两位数字，27 个三位数字，
		81 个四位数字，243 个五位数字，729 个六位数字，
		2187 个七位数字，6561 个八位数字和 19683 个九位数字。
		总共，可以使用D中的数字写出 29523 个整数。

		输入：digits = ["7"], n = 8
		输出：1

		1 <= digit[i] <= 9

	*/
	D := len(digits)
	S := strconv.Itoa(n)
	N := len(S)
	res := 0
	// 对于位数小于 N，则通过排列组合累加到结果
	for i := 1; i < N; i++ {
		res += int(math.Pow(float64(D), float64(i)))
	}

	// 针对位数=N，对于前缀小于当前n的前缀，可以排列组合剩余的位数
	for i := 0; i < N; i++ {
		cur := S[i : i+1]
		smaller := 0
		equal := false
		for _, s := range digits {
			if s < cur {
				smaller++
			}
			if s == cur {
				equal = true
			}
		}
		res += smaller * int(math.Pow(float64(D), float64(N-i-1))) // 剩余字符可以随意组合

		// 如果没有相等的字符，那么不需要处理后续了
		if !equal {
			return res
		}
	}
	return res + 1 // 有相等数字

}

func atMostNGivenDigitSetV1(digits []string, n int) int {
	// 解法超时！！
	// 生成的数值都是 digits 数字开头的衍生数字
	// 对 digits 每个数字，视为一个层序树
	// 1->11,13,15,17 -> 111,113....
	// 3->31,33,35,37 -> ...
	// ...
	// 层序遍历，遇到大于N的数字则退出即可
	res := 0

	nums := make([]string, 0, len(digits))
	for _, s := range digits {
		v, _ := strconv.Atoi(s)
		if v > n {
			break
		}
		nums = append(nums, s)
		res++
	}

	for len(nums) > 0 {
		cur := nums[0]
		nums = nums[1:]

		end := false
		for _, s := range digits {
			v, _ := strconv.Atoi(cur + s)
			if v > n {
				end = true
				break
			}
			nums = append(nums, cur+s)
			res++
		}
		if end {
			break
		}
	}
	return res
}
