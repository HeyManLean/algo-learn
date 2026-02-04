package bytedance

func insert(intervals [][]int, newInterval []int) [][]int {
	/*
		57. 插入区间

		给你一个 无重叠的 ，按照区间起始端点排序的区间列表 intervals。
		在列表中插入一个新的区间 newInterval，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

		输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
		输出: [[1,5],[6,9]]
		解释: 新区间 [2,5] 与 [1,3] 重叠，合并为 [1,5]，再与 [6,9] 不重叠。

		输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
		输出: [[1,2],[3,10],[12,16]]
		解释: 新区间 [4,8] 与 [3,5]、[6,7]、[8,10] 重叠，合并为 [3,10]。

		输入: intervals = [], newInterval = [5,7]
		输出: [[5,7]]

		0 <= intervals.length <= 10^4
		intervals[i].length == 2
		0 <= intervals[i][0] <= intervals[i][1] <= 10^5
		intervals 按 intervals[i][0] 升序排列
		newInterval.length == 2
		0 <= newInterval[0] <= newInterval[1] <= 10^5
	*/
	// 包含，交叉，反包含
	// 需要重叠才能合并，不能直接用桶
	res := [][]int{}
	merged := false
	for _, interval := range intervals {
		if merged {
			res = append(res, interval)
			continue
		}
		// 包含
		if interval[0] <= newInterval[0] && interval[1] >= newInterval[1] {
			return intervals
		}
		// 在左边，直接添加
		if newInterval[1] < interval[0] {
			res = append(res, newInterval, interval)
			merged = true
			continue
		}
		// 在右边，忽略
		if newInterval[0] > interval[1] {
			res = append(res, interval)
			continue
		}

		// 新全包含旧，跳过旧
		if newInterval[0] <= interval[0] && newInterval[1] >= interval[1] {
			continue
		}

		// 左边交叉
		if newInterval[0] < interval[0] && newInterval[1] >= interval[0] {
			newInterval[1] = interval[1]
			continue
		}
		// 右边交叉
		if newInterval[0] > interval[0] && newInterval[1] >= interval[1] {
			newInterval[0] = interval[0]
			continue
		}
	}
	if !merged {
		res = append(res, newInterval)
	}
	return res
}
