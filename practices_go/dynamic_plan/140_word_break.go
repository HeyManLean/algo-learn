package dynamicplan

func wordBreak2(s string, wordDict []string) []string {
	/*
		140. 单词拆分 II

		给定一个字符串 s 和一个字符串字典 wordDict ，在字符串 s 中增加空格来构建一个句子，使得句子中所有的单词都在词典中。以任意顺序 返回所有这些可能的句子。
		注意：词典中的同一个单词可能在分段中被重复使用多次。

		输入:s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
		输出:["cats and dog","cat sand dog"]

		输入:s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
		输出:["pine apple pen apple","pineapple pen apple","pine applepen apple"]
		解释: 注意你可以重复使用字典中的单词。

		输入:s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
		输出:[]

		提示：
		1 <= s.length <= 20
		1 <= wordDict.length <= 1000
		1 <= wordDict[i].length <= 10
		s 和 wordDict[i] 仅有小写英文字母组成
		wordDict 中所有字符串都 不同
	*/
	if len(wordDict) == 0 {
		return []string{}
	}
	var min = func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}
	var max = func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}

	wordMap := make(map[string]bool)
	minLen := len(wordDict[0])
	maxLen := minLen

	for _, w := range wordDict {
		minLen = min(len(w), minLen)
		maxLen = max(len(w), maxLen)
		wordMap[w] = true
	}

	n := len(s)

	memo := make(map[int][]string)
	var dfs func(start int) []string
	dfs = func(start int) []string {

		if v, ok := memo[start]; ok {
			return v
		}
		if start == n {
			return []string{""}
		}
		res := []string{}
		for end := start + minLen; end <= start+maxLen && end <= n; end++ {
			word := s[start:end]
			if !wordMap[word] {
				continue
			}
			for _, tail := range dfs(end) {
				if tail == "" {
					res = append(res, word)
				} else {
					res = append(res, word+" "+tail)
				}
			}
		}
		memo[start] = res
		return res
	}

	return dfs(0)
}
