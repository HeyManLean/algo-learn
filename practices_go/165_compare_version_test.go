package practicesgo

import (
	"testing"
)

func compareVersion(version1 string, version2 string) int {
	/*
		165. 比较版本号
		给你两个 版本号字符串 version1 和 version2 ，请你比较它们。版本号由被点 '.' 分开的修订号组成。修订号的值 是它 转换为整数 并忽略前导零。
		比较版本号时，请按 从左到右的顺序 依次比较它们的修订号。如果其中一个版本字符串的修订号较少，则将缺失的修订号视为 0。

		返回规则如下：
		如果 version1 < version2 返回 -1，
		如果 version1 > version2 返回 1，
		除此之外返回 0。

		输入：version1 = "1.2", version2 = "1.10"
		输出：-1

		输入：version1 = "1.01", version2 = "1.001"
		输出：0

		解释：忽略前导零，"01" 和 "001" 都代表相同的整数 "1"。
	*/
	// 简述，比较版本号字符串，分别对比 . 分开前后两个数字大小
	// 方案：双指针，遍历字符串并转成数字，比较两个数字，遇到 . 作为截止

	p1 := 0
	p2 := 0
	m := len(version1)
	n := len(version2)

	for p1 < m || p2 < n {
		x := 0
		for ; p1 < m && version1[p1] != '.'; p1++ {
			x = x*10 + int(version1[p1]-'0')
		}
		p1++

		y := 0
		for ; p2 < n && version2[p2] != '.'; p2++ {
			y = y*10 + int(version2[p2]-'0')
		}
		p2++

		if x > y {
			return 1
		} else if x < y {
			return -1
		}
	}
	return 0
}

func TestCompareVersion(t *testing.T) {
	tests := []struct {
		name     string
		version1 string
		version2 string
		want     int
	}{
		{
			name:     "version1 < version2",
			version1: "1.2",
			version2: "1.10",
			want:     -1,
		},

		{
			name:     "忽略前导零，相等",
			version1: "1.01",
			version2: "1.001",
			want:     0,
		},

		{
			name:     "version1 > version2",
			version1: "2.1",
			version2: "1.10",
			want:     1,
		},

		{
			name:     "完全相等",
			version1: "1.2.3",
			version2: "1.2.3",
			want:     0,
		},

		{
			name:     "version1 修订号较少",
			version1: "1.2",
			version2: "1.2.1",
			want:     -1,
		},

		{
			name:     "version2 修订号较少",
			version1: "1.2.1",
			version2: "1.2",
			want:     1,
		},

		{
			name:     "多个前导零",
			version1: "1.0001",
			version2: "1.01",
			want:     0,
		},

		{
			name:     "单版本号比较",
			version1: "2",
			version2: "1",
			want:     1,
		},

		{
			name:     "单版本号相等",
			version1: "1",
			version2: "1",
			want:     0,
		},

		{
			name:     "复杂版本号比较",
			version1: "1.0.1",
			version2: "1.0.2",
			want:     -1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := compareVersion(tt.version1, tt.version2); got != tt.want {
				t.Errorf("compareVersion(%v, %v) = %v, want %v", tt.version1, tt.version2, got, tt.want)
			}
		})
	}
}
