package dynamicplan

import (
	"testing"
)

func TestMaxEnvelopes(t *testing.T) {
	cases := []struct {
		name      string
		envelopes [][]int
		expected  int
	}{
		{
			name:      "示例1 - 题目给出的标准答案",
			envelopes: [][]int{{5, 4}, {6, 4}, {6, 7}, {2, 3}},
			expected:  3,
		},
		{
			name:      "示例2 - 题目给出的标准答案",
			envelopes: [][]int{{1, 1}, {1, 1}, {1, 1}},
			expected:  1, // 宽度相同，不能嵌套
		},
		{
			name:      "单个信封",
			envelopes: [][]int{{5, 4}},
			expected:  1,
		},
		{
			name:      "两个信封可以嵌套",
			envelopes: [][]int{{2, 3}, {5, 4}},
			expected:  2, // [2,3] => [5,4]
		},
		{
			name:      "两个信封排序后可以嵌套",
			envelopes: [][]int{{5, 4}, {2, 3}},
			expected:  2, // 排序后 [2,3] => [5,4]
		},
		{
			name:      "两个信封不能嵌套（高度相同）",
			envelopes: [][]int{{5, 4}, {6, 4}},
			expected:  1, // 高度相同，不能嵌套
		},
		{
			name:      "多个信封严格递增",
			envelopes: [][]int{{1, 1}, {2, 2}, {3, 3}, {4, 4}},
			expected:  4, // 全部可以嵌套
		},
	}

	for _, tt := range cases {
		t.Run(tt.name, func(t *testing.T) {
			if res := maxEnvelopes(tt.envelopes); res != tt.expected {
				t.Errorf("maxEnvelopes(%v) = %d, expected %d", tt.envelopes, res, tt.expected)
			}
		})
	}
}
