package dynamicplan

import "testing"

func TestNumDecodings(t *testing.T) {
	tests := []struct {
		name     string
		s        string
		expected int
	}{
		{
			name:     "示例1: 12",
			s:        "12",
			expected: 2,
		},
		{
			name:     "示例2: 226",
			s:        "226",
			expected: 3,
		},
		{
			name:     "示例3: 06",
			s:        "06",
			expected: 0,
		},
		{
			name:     "单个数字1",
			s:        "1",
			expected: 1,
		},
		{
			name:     "单个数字0",
			s:        "0",
			expected: 0,
		},
		{
			name:     "包含0的情况: 10",
			s:        "10",
			expected: 1,
		},
		{
			name:     "包含0的情况: 20",
			s:        "20",
			expected: 1,
		},
		{
			name:     "包含0的情况: 30",
			s:        "30",
			expected: 0,
		},
		{
			name:     "复杂情况: 11106",
			s:        "11106",
			expected: 2,
		},
		{
			name:     "复杂情况: 27",
			s:        "27",
			expected: 1,
		},
		{
			name:     "复杂情况: 2101",
			s:        "2101",
			expected: 1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := numDecodings(tt.s)
			if result != tt.expected {
				t.Errorf("numDecodings(%s) = %d, expected %d", tt.s, result, tt.expected)
			}
		})
	}
}
