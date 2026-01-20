package dynamicplan

import "testing"

func TestLongestPalindrome(t *testing.T) {
	tests := []struct {
		name       string
		input      string
		expected   string
		checkExact bool // 是否检查精确匹配
		minLength  int  // 最小长度要求
	}{
		{
			name:       "示例1: babad",
			input:      "babad",
			expected:   "bab", // 或 "aba" 也是有效答案
			checkExact: false,
			minLength:  3,
		},
		{
			name:       "示例2: cbbd",
			input:      "cbbd",
			expected:   "bb",
			checkExact: true,
			minLength:  2,
		},
		{
			name:       "示例3: abbcccba",
			input:      "abbcccba",
			expected:   "bcccb", // 实际输出
			checkExact: true,
			minLength:  3,
		},
		{
			name:       "示例3: bananas",
			input:      "bananas",
			expected:   "anana", // 实际输出
			checkExact: true,
			minLength:  5,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := longestPalindrome(tt.input)

			// 验证结果是否为回文
			if !isPalindrome(result) {
				t.Errorf("结果不是回文: %s", result)
			}

			// 验证长度
			if len(result) < tt.minLength {
				t.Errorf("结果长度 %d 小于最小长度 %d. 结果: %s",
					len(result), tt.minLength, result)
			}

			// 如果要求精确匹配，验证结果
			if tt.checkExact {
				if result != tt.expected {
					t.Errorf("期望 %s, 得到 %s", tt.expected, result)
				}
			} else {
				// 对于不要求精确匹配的，只验证长度合理
				if len(result) < tt.minLength {
					t.Errorf("结果长度 %d 小于最小长度 %d. 结果: %s",
						len(result), tt.minLength, result)
				}
			}

			// 验证结果确实是输入字符串的子串
			if tt.input != "" && !isSubstring(result, tt.input) {
				t.Errorf("结果 %s 不是输入字符串 %s 的子串", result, tt.input)
			}
		})
	}
}

// 辅助函数：验证字符串是否为回文
func isPalindrome(s string) bool {
	if len(s) == 0 {
		return true
	}
	left, right := 0, len(s)-1
	for left < right {
		if s[left] != s[right] {
			return false
		}
		left++
		right--
	}
	return true
}

// 辅助函数：验证 result 是否是 input 的子串
func isSubstring(result, input string) bool {
	if len(result) == 0 {
		return true
	}
	if len(result) > len(input) {
		return false
	}
	for i := 0; i <= len(input)-len(result); i++ {
		if input[i:i+len(result)] == result {
			return true
		}
	}
	return false
}
