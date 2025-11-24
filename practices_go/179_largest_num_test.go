package practicesgo

import (
	"strconv"
	"strings"
	"testing"
)

func largestNumber(nums []int) string {
	/*
		179. 最大数
		给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
		注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

		输入：nums = [10,2]
		输出："210"

		输入：nums = [3,30,34,5,9]
		输出："9534330"

	*/
	// 简述：调整数组数值位置，使得串起来的数字最大
	// 可以理解为排序，只是不是按照数值排序，按照前缀来排序
	strList := make([]string, 0, len(nums))
	for _, num := range nums {
		strList = append(strList, strconv.Itoa(num))
	}

	mergeSort(strList, 0, len(strList))

	result := strings.Join(strList, "")
	// 处理全0的情况，返回"0"而不是"000..."
	if len(result) > 0 && result[0] == '0' {
		return "0"
	}
	return result
}

func mergeSort(strList []string, lo, hi int) {
	// 左开右闭
	if hi-lo < 2 {
		return
	}
	mi := lo + (hi-lo)/2
	mergeSort(strList, lo, mi)
	mergeSort(strList, mi, hi)

	tempList := make([]string, mi-lo)
	for i := 0; i < mi-lo; i++ {
		tempList[i] = strList[lo+i]
	}

	i := 0
	n := len(tempList)
	j := mi

	for i < n && j < hi {
		// 比较 s1+s2 和 s2+s1，哪个更大
		if tempList[i]+strList[j] >= strList[j]+tempList[i] {
			strList[lo] = tempList[i]
			i++
		} else {
			strList[lo] = strList[j]
			j++
		}
		lo++
	}
	for i < n {
		strList[lo] = tempList[i]
		i++
		lo++
	}
}

func TestLargestNumber(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		expected string
	}{
		{
			name:     "示例1: 基本测试",
			nums:     []int{10, 2},
			expected: "210",
		},
		{
			name:     "示例2: 多个数字",
			nums:     []int{3, 30, 34, 5, 9},
			expected: "9534330",
		},
		{
			name:     "单个数字",
			nums:     []int{1},
			expected: "1",
		},
		{
			name:     "两个相同数字",
			nums:     []int{2, 2},
			expected: "22",
		},
		{
			name:     "包含0",
			nums:     []int{0, 0},
			expected: "0",
		},
		{
			name:     "全零",
			nums:     []int{0, 0, 0},
			expected: "0",
		},
		{
			name:     "混合包含零",
			nums:     []int{1, 0, 0},
			expected: "100",
		},
		{
			name:     "不同位数",
			nums:     []int{1, 10, 100},
			expected: "110100",
		},
		{
			name:     "大数字",
			nums:     []int{999, 99, 9},
			expected: "999999",
		},
		{
			name:     "复杂情况",
			nums:     []int{824, 938, 1399, 5607, 6973, 5703, 9609, 4398, 8247},
			expected: "9609938824824769735703560743981399",
		},
		{
			name:     "前缀相同",
			nums:     []int{12, 121},
			expected: "12121",
		},
		{
			name:     "前缀相同2",
			nums:     []int{121, 12},
			expected: "12121",
		},
		{
			name:     "单个零",
			nums:     []int{0},
			expected: "0",
		},
		{
			name:     "两位数组合",
			nums:     []int{20, 1},
			expected: "201",
		},
		{
			name:     "特殊边界",
			nums:     []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 0},
			expected: "9876543210",
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := largestNumber(tt.nums)
			if result != tt.expected {
				t.Errorf("largestNumber(%v) = %v, want %v", tt.nums, result, tt.expected)
			}
		})
	}
}
