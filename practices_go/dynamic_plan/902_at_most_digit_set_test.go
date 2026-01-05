package dynamicplan

import (
	"testing"
)

func TestAtMostNGivenDigitSet(t *testing.T) {
	cases := []struct {
		name     string
		digits   []string
		n        int
		expected int
	}{
		{
			name:     "示例1 - 题目给出的标准答案",
			digits:   []string{"1", "3", "5", "7"},
			n:        100,
			expected: 20,
		},
		{
			name:     "示例2 - 题目给出的标准答案",
			digits:   []string{"1", "4", "9"},
			n:        1000000000,
			expected: 29523,
		},
		{
			name:     "示例3 - 题目给出的标准答案",
			digits:   []string{"7"},
			n:        8,
			expected: 1,
		},
		{
			name:     "单个数字，n等于该数字",
			digits:   []string{"5"},
			n:        5,
			expected: 1,
		},
		{
			name:     "单个数字，n小于该数字",
			digits:   []string{"5"},
			n:        3,
			expected: 0,
		},
		{
			name:     "单个数字，n大于该数字",
			digits:   []string{"5"},
			n:        10,
			expected: 1,
		},
		{
			name:     "多个数字，n为一位数",
			digits:   []string{"1", "3", "5"},
			n:        5,
			expected: 3, // 1, 3, 5
		},
		{
			name:     "所有数字都小于n的第一位",
			digits:   []string{"1", "2", "3"},
			n:        50,
			expected: 12, // 1,2,3,11,12,13,21,22,23,31,32,33
		},
		{
			name:     "1-9",
			digits:   []string{"1", "2", "3", "4", "6", "7", "8", "9"},
			n:        67688637,
			expected: 12255070, // 1,2,3,11,12,13,21,22,23,31,32,33
		},
	}

	for _, tt := range cases {
		t.Run(tt.name, func(t *testing.T) {
			if res := atMostNGivenDigitSet(tt.digits, tt.n); res != tt.expected {
				t.Errorf("atMostNGivenDigitSet(%v, %d) = %d, expected %d", tt.digits, tt.n, res, tt.expected)
			}
		})
	}
}
