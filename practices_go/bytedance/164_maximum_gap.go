package bytedance

import (
	"math"
)

func maximumGap(nums []int) int {
	/*
		164. 最大间距

		给定一个无序的数组 nums，返回 数组在排序之后，相邻元素之间最大的差值 。
		如果数组元素个数小于 2，则返回 0 。
		你必须设计一个在 O(n) 时间复杂度和 O(n) 空间复杂度下运行的算法。

		输入: nums = [3,6,9,1]
		输出: 3
		解释: 排序后的数组是 [1,3,6,9]，其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。

		输入: nums = [10]
		输出: 0
		解释: 数组元素个数小于 2，因此返回 0。

		1 <= nums.length <= 10^5
		0 <= nums[i] <= 10^9
	*/
	// 记录最大值和最小值
	// 计算每个数跟最小值的差值，将差值映射到桶里面
	// 桶的设定，(最大值-最小值)/(n-1) 这是平均的gap
	// 每个桶设置为 gap-1 小于平均值，保证最大差值在不同的桶中，其他差值可能在同一个桶但可以忽略
	// 设定最大桶和最小桶，分别记录的是该桶的最大的那个值和最小的那个值
	// 最后结果就是，当前桶最小值-前面非空桶的最大值，也就是相邻的值，取其中最大即可

	if len(nums) <= 1 {
		return 0
	}
	var min = func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}
	var max = func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	minVal := math.MaxInt
	maxVal := 0

	for _, num := range nums {
		minVal = min(minVal, num)
		maxVal = max(maxVal, num)
	}
	n := len(nums)
	gap := max((maxVal-minVal)/(n-1)-1, 1)
	bucketCount := (maxVal-minVal)/gap + 1

	minBucket := make([]int, bucketCount)
	maxBucket := make([]int, bucketCount)

	for i := range minBucket {
		minBucket[i] = math.MaxInt
		maxBucket[i] = -math.MaxInt
	}

	for _, num := range nums {
		bucketIndex := (num - minVal) / gap
		minBucket[bucketIndex] = min(minBucket[bucketIndex], num)
		maxBucket[bucketIndex] = max(maxBucket[bucketIndex], num)
	}

	// 遍历
	prevMax := -1
	res := 0
	for i := range minBucket {
		if minBucket[i] > maxVal {
			continue
		}
		if prevMax >= 0 {
			res = max(res, minBucket[i]-prevMax)
		}
		if maxBucket[i] >= 0 {
			prevMax = maxBucket[i]
		}
	}
	return res
}
