package bytedance

func numIslands(grid [][]byte) int {
	/*
		200. 岛屿数量

		给你一个由 '1'（陆地）和 '0'（水）组成的二维网格 grid，请计算网格中岛屿的数量。
		岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
		此外，你可以假设网格的四个边均被水包围。

		输入：grid = [
		  ["1","1","1","1","0"],
		  ["1","1","0","1","0"],
		  ["1","1","0","0","0"],
		  ["0","0","0","0","0"]
		]
		输出：1

		输入：grid = [
		  ["1","1","0","0","0"],
		  ["1","1","0","0","0"],
		  ["0","0","1","0","0"],
		  ["0","0","0","1","1"]
		]
		输出：3

		m == grid.length
		n == grid[i].length
		1 <= m, n <= 300
		grid[i][j] 的值为 '0' 或 '1'
	*/
	// 遍历矩阵，遇到 1 则将周围相邻的1都改为0，岛屿数量+1
	var LAND byte = '1'
	var WATER byte = '0'

	m := len(grid)
	n := len(grid[0])

	var dfs func(i, j int)
	dfs = func(i, j int) {
		if i < 0 || i > m-1 || j < 0 || j > n-1 {
			return
		}
		if grid[i][j] == WATER {
			return
		}
		grid[i][j] = WATER
		dfs(i-1, j)
		dfs(i+1, j)
		dfs(i, j-1)
		dfs(i, j+1)
	}

	res := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] != LAND {
				continue
			}
			dfs(i, j)
			res++
		}
	}
	return res
}
