package dynamicplan

import "testing"

func Test_wordBreak(t *testing.T) {
	tests := []struct {
		name     string
		s        string
		wordDict []string
		want     bool
	}{
		{
			name:     "示例1: leetcode",
			s:        "leetcode",
			wordDict: []string{"leet", "code"},
			want:     true,
		},
		{
			name:     "示例2: applepenapple，单词可重复使用",
			s:        "applepenapple",
			wordDict: []string{"apple", "pen"},
			want:     true,
		},
		{
			name:     "示例3: catsandog，无法拼接",
			s:        "catsandog",
			wordDict: []string{"cats", "dog", "sand", "and", "cat"},
			want:     false,
		},
		{
			name:     "空字符串",
			s:        "",
			wordDict: []string{"a", "b"},
			want:     true,
		},
		{
			name:     "单个字符匹配",
			s:        "a",
			wordDict: []string{"a"},
			want:     true,
		},
		{
			name:     "单个字符不匹配",
			s:        "a",
			wordDict: []string{"b"},
			want:     false,
		},
		{
			name:     "多个单词组合",
			s:        "aaaaaaa",
			wordDict: []string{"aaaa", "aaa"},
			want:     true,
		},
		{
			name:     "字典中有多余单词",
			s:        "goalspecial",
			wordDict: []string{"go", "goal", "goals", "special"},
			want:     true,
		},
		{
			name:     "需要回溯的情况",
			s:        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
			wordDict: []string{"a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"},
			want:     false,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := wordBreak(tt.s, tt.wordDict); got != tt.want {
				t.Errorf("wordBreak() = %v, want %v", got, tt.want)
			}
		})
	}
}
