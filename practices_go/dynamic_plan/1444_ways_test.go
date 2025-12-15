package dynamicplan

import (
	"testing"
)

func TestWays(t *testing.T) {
	cases := []struct {
		name     string
		pizza    []string
		k        int
		expected int
	}{
		{
			name:     "示例1",
			pizza:    []string{"A..", "AAA", "..."},
			k:        3,
			expected: 3,
		},
		{
			name:     "示例2",
			pizza:    []string{"A..", "AA.", "..."},
			k:        3,
			expected: 1,
		},
		{
			name:     "示例3",
			pizza:    []string{"A..", "A..", "..."},
			k:        1,
			expected: 1,
		},
		{
			name:     "单个苹果",
			pizza:    []string{"A"},
			k:        1,
			expected: 1,
		},
		{
			name:     "全部是苹果",
			pizza:    []string{"AAA", "AAA", "AAA"},
			k:        3,
			expected: 6,
		},
		{
			name:     "只有一行",
			pizza:    []string{"A.A"},
			k:        2,
			expected: 1,
		},
		{
			name:     "只有一列",
			pizza:    []string{"A", ".", "A"},
			k:        2,
			expected: 1,
		},
		{
			name:     "无法切分",
			pizza:    []string{"A..", "...", "..."},
			k:        2,
			expected: 0,
		},
	}

	for _, tt := range cases {
		t.Run(tt.name, func(t *testing.T) {
			if res := ways(tt.pizza, tt.k); res != tt.expected {
				t.Errorf("ways(%v, %d) = %d, expected %d", tt.pizza, tt.k, res, tt.expected)
			}
		})
	}
}
