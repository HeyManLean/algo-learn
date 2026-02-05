package bytedance

func reversePairs(nums []int) int {
	/*
		剑指 Offer 51. 数组中的逆序对

		在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
		输入一个数组，求出这个数组中的逆序对的总数。

		输入: [7,5,6,4]
		输出: 5
		解释: 逆序对分别为 (7,5)、(7,6)、(7,4)、(5,4)、(6,4)，共 5 个。

		0 <= 数组长度 <= 50000
		结果需对 1000000007 取模
	*/
	n := len(nums)

	// 合并排序
	// 排序左边，排序右边
	// 合并时，如果左边 left[i] > right[j] ，则有逆序对 mid-i+1, 左边i后面的数字都能跟right[j]产生逆序对
	var mergeSort func(l, r int) int
	tmp := make([]int, n)
	mergeSort = func(l, r int) int {
		if l >= r {
			return 0
		}
		mid := (l + r) / 2
		cnt := mergeSort(l, mid) + mergeSort(mid+1, r)

		i, j, k := l, mid+1, l
		for i <= mid && j <= r {
			if nums[i] <= nums[j] {
				tmp[k] = nums[i]
				i++
			} else {
				cnt += mid - i + 1
				tmp[k] = nums[j]
				j++
			}
			k++
		}
		for i <= mid {
			tmp[k] = nums[i]
			i++
			k++
		}
		for j <= r {
			tmp[k] = nums[j]
			j++
			k++
		}

		for i := l; i <= r; i++ {
			nums[i] = tmp[i]
		}
		return cnt
	}
	return mergeSort(0, n-1)
}
