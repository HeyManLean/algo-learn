package practicesgo

func longestConsecutive(nums []int) int {
	/*
		128. 最长连续序列
		给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

		请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
		输入：nums = [100,4,200,1,3,2]
		输出：4

		输入：nums = [0,3,7,2,5,8,4,6,0,1]
		输出：9

		输入：nums = [1,0,1,2]
		输出：3
	*/
	// 简述：找出升序排列的连续最长子序列的长度
	// O(n) 复杂度，不能做排序操作
	// 使用hash记录，num是否存在
	// 遍历nums，找到num后继有多少个数
	// 如果 num-1 存在，则跳过num

	numFlagMap := make(map[int]bool)
	for _, num := range nums {
		numFlagMap[num] = true
	}
	maxCons := 0
	handledMap := make(map[int]bool)
	for _, num := range nums {
		if numFlagMap[num-1] || handledMap[num] {
			continue
		}
		handledMap[num] = true
		cur := num
		cons := 1
		for numFlagMap[cur+1] {
			cons += 1
			cur += 1
		}
		if cons > maxCons {
			maxCons = cons
		}
	}
	return maxCons
}
