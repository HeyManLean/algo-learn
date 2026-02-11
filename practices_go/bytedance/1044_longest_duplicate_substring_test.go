package bytedance

import "testing"

func TestLongestDupSubstring(t *testing.T) {
	t.Run("示例1-banana", func(t *testing.T) {
		got := longestDupSubstring("banana")
		// "ana" 出现了2次（位置1和位置3），是最长的重复子串
		if got != "ana" {
			t.Errorf("longestDupSubstring(\"banana\") = %q, want \"ana\"", got)
		}
	})

	t.Run("示例2-无重复子串", func(t *testing.T) {
		got := longestDupSubstring("abcd")
		if got != "" {
			t.Errorf("longestDupSubstring(\"abcd\") = %q, want \"\"", got)
		}
	})

	t.Run("全部相同字符", func(t *testing.T) {
		got := longestDupSubstring("aaaa")
		if got != "aaa" {
			t.Errorf("longestDupSubstring(\"aaaa\") = %q, want \"aaa\"", got)
		}
	})

	t.Run("两个字符相同", func(t *testing.T) {
		got := longestDupSubstring("aa")
		if got != "a" {
			t.Errorf("longestDupSubstring(\"aa\") = %q, want \"a\"", got)
		}
	})

	t.Run("两个字符不同", func(t *testing.T) {
		got := longestDupSubstring("ab")
		if got != "" {
			t.Errorf("longestDupSubstring(\"ab\") = %q, want \"\"", got)
		}
	})

	t.Run("较长字符串", func(t *testing.T) {
		got := longestDupSubstring("abcabcabc")
		// "abcabc" 出现了2次（位置0和位置3），是最长的重复子串
		if got != "abcabc" {
			t.Errorf("longestDupSubstring(\"abcabcabc\") = %q, want \"abcabc\"", got)
		}
	})

	t.Run("重叠重复子串", func(t *testing.T) {
		got := longestDupSubstring("aabaa")
		// "aa" 出现了2次（位置0和位置3）
		if got != "aa" {
			t.Errorf("longestDupSubstring(\"aabaa\") = %q, want \"aa\"", got)
		}
	})
}
