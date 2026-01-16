package dynamicplan

import (
	"reflect"
	"sort"
	"testing"
)

func TestWordBreak(t *testing.T) {
	cases := []struct {
		name     string
		s        string
		wordDict []string
		expected []string
	}{
		// 题目示例
		{
			name:     "示例1: catsanddog",
			s:        "catsanddog",
			wordDict: []string{"cat", "cats", "and", "sand", "dog"},
			expected: []string{"cats and dog", "cat sand dog"},
		},
		{
			name:     "示例2: pineapplepenapple",
			s:        "pineapplepenapple",
			wordDict: []string{"apple", "pen", "applepen", "pine", "pineapple"},
			expected: []string{"pine apple pen apple", "pineapple pen apple", "pine applepen apple"},
		},
		{
			name:     "示例3: catsandog (无解)",
			s:        "catsandog",
			wordDict: []string{"cats", "dog", "sand", "and", "cat"},
			expected: []string{},
		},
		// 基本测试情况
		{
			name:     "单个单词匹配",
			s:        "cat",
			wordDict: []string{"cat"},
			expected: []string{"cat"},
		},
		{
			name:     "单个单词不匹配",
			s:        "dog",
			wordDict: []string{"cat"},
			expected: []string{},
		},
		{
			name:     "两个单词",
			s:        "catdog",
			wordDict: []string{"cat", "dog"},
			expected: []string{"cat dog"},
		},
		{
			name:     "重复单词",
			s:        "catcat",
			wordDict: []string{"cat"},
			expected: []string{"cat cat"},
		},
		// 多个解的情况
		{
			name:     "多个解: leetcode",
			s:        "leetcode",
			wordDict: []string{"leet", "code", "le", "et", "code"},
			expected: []string{"leet code", "le et code"},
		},
		{
			name:     "多个解: aaa",
			s:        "aaa",
			wordDict: []string{"a", "aa", "aaa"},
			expected: []string{"a a a", "a aa", "aa a", "aaa"},
		},
		// 边界情况
		{
			name:     "空字符串",
			s:        "",
			wordDict: []string{"cat"},
			expected: []string{},
		},
		{
			name:     "空字典",
			s:        "cat",
			wordDict: []string{},
			expected: []string{},
		},
		{
			name:     "完全匹配单个单词",
			s:        "apple",
			wordDict: []string{"apple"},
			expected: []string{"apple"},
		},
		{
			name:     "单词重叠但无解",
			s:        "catsandog",
			wordDict: []string{"cats", "dog", "sand", "and", "cat"},
			expected: []string{},
		},
	}

	for _, tt := range cases {
		t.Run(tt.name, func(t *testing.T) {
			result := wordBreak(tt.s, tt.wordDict)
			if !equalStringSlices(result, tt.expected) {
				t.Errorf("wordBreak(%q, %v) = %v, expected %v", tt.s, tt.wordDict, result, tt.expected)
			}
		})
		break
	}
}

// equalStringSlices 比较两个字符串切片是否相等（顺序无关）
func equalStringSlices(a, b []string) bool {
	if len(a) != len(b) {
		return false
	}
	// 创建副本并排序
	aCopy := make([]string, len(a))
	bCopy := make([]string, len(b))
	copy(aCopy, a)
	copy(bCopy, b)
	sort.Strings(aCopy)
	sort.Strings(bCopy)
	return reflect.DeepEqual(aCopy, bCopy)
}
