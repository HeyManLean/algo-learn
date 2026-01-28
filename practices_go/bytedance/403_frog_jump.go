package bytedance

func canCross(stones []int) bool {
	/*
		403. 青蛙过河

		一只青蛙想要过河。 假定河流被等分为若干个单元格，并且每一个单元格内都有可能放有一块石子（也有可能没有）。
		青蛙可以跳上石子，但是不可以跳入水中。

		给你石子的位置列表 stones（用单元格序号 升序 表示）， 请判定青蛙能否成功过河（即能否在最后一步跳至最后一块石子上）。
		开始时， 青蛙默认已站在第一块石子上，并可以假定它第一步只能跳跃 1 个单位（即只能从单元格 1 跳至单元格 2）。

		如果青蛙上一步跳跃了 k 个单位，那么它接下来的跳跃距离只能选择为 k - 1、k 或 k + 1 个单位。
		另请注意，青蛙只能向前方（终点的方向）跳跃。

		示例 1：
		输入：stones = [0,1,3,5,6,8,12,17]
		输出：true
		解释：青蛙可以成功过河，按照如下方案跳跃：跳 1 个单位到第 2 块石子, 然后跳 2 个单位到第 3 块石子,
		     接着 跳 2 个单位到第 4 块石子, 然后跳 3 个单位到第 6 块石子, 跳 4 个单位到第 7 块石子,
		     最后，跳 5 个单位到第 8 个石子（即最后一块石子）。

		示例 2：
		输入：stones = [0,1,2,3,4,8,9,11]
		输出：false
		解释：青蛙无法跳到最后一块石子，因为无论怎么跳，都会跳不过去（即无法到达位置 11）。

		提示：
		2 <= stones.length <= 2000
		0 <= stones[i] <= 2^31 - 1
		stones[0] == 0
		stones 按严格升序排列
	*/
	// 下一跳能选择的距离，取决于前一条的距离
	// 下一跳，可以跳到后面0到3个为止（k-1,k,k+1)

	if stones[1]-stones[0] > 1 {
		return false
	}
	n := len(stones)

	var dfs func(start int, lastStep int) bool
	memo := make(map[int]map[int]bool)
	dfs = func(start int, lastStep int) bool {
		if start == n-1 {
			return true
		}
		if m, ok := memo[start]; ok {
			if res, ok := m[lastStep]; ok {
				return res
			}
		} else {
			memo[start] = make(map[int]bool)
		}

		// 不是后三位，而是 lastStep -1... lastStep +
		res := false

		for next := start + 1; next < n; next++ {
			if stones[next]-stones[start] > lastStep+1 {
				break
			}
			if stones[next]-stones[start] >= lastStep-1 {
				res = dfs(next, stones[next]-stones[start])
			}
			if res {
				break
			}
		}
		memo[start][lastStep] = res
		return res
	}
	return dfs(1, 1)
}
