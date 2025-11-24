package practicesgo

import (
	"fmt"
	"testing"
)

func maxAreaOfIsland(grid [][]int) int {
	/*
		695. 岛屿的最大面积

		给你一个大小为 m x n 的二进制矩阵 grid 。
		岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。
		你可以假设 grid 的四个边缘都被 0（代表水）包围着。

		岛屿的面积是岛上值为 1 的单元格的数目。

		grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
		输出：6
	*/
	// 简述：找出最大面积的岛屿，返回其面积
	// 找到一个1，然后将其相邻的1改成0，并计数，直到没有相邻的1
	m := len(grid)
	n := len(grid[0])
	max := 0

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			area := dfs(grid, i, j)
			if area > max {
				max = area
			}
		}
	}
	return max
}

func dfs(grid [][]int, i, j int) int {
	// 遍历相邻单元格，并将1改为0，返回1的数目
	if grid[i][j] == 0 {
		return 0
	}
	res := 1
	grid[i][j] = 0

	if i > 0 && grid[i-1][j] == 1 {
		res += dfs(grid, i-1, j)
	}
	if j > 0 && grid[i][j-1] == 1 {
		res += dfs(grid, i, j-1)
	}
	if i < len(grid)-1 && grid[i+1][j] == 1 {
		res += dfs(grid, i+1, j)
	}
	if j < len(grid[0])-1 && grid[i][j+1] == 1 {
		res += dfs(grid, i, j+1)
	}
	return res
}

func TestMaxAreaOfIsland(t *testing.T) {
	grid := [][]int{{0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0}, {0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0}, {0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0}, {0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0}}
	max := maxAreaOfIsland(grid)
	if max != 6 {
		t.Errorf("failed")
	}
	fmt.Println("OK")
}
