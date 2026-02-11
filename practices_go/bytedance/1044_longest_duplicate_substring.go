package bytedance

func longestDupSubstring(s string) string {
	/*
		1044. 最长重复子串

		给你一个字符串 s ，考虑其所有 重复子串 ：即 s 的（连续）子串，在 s 中出现 2 次或更多次。这些出现之间可能存在重叠。

		返回 任意一个 可能具有最长长度的重复子串。如果 s 不含重复子串，那么答案为 "" 。

		示例 1：
		输入：s = "banana"
		输出："ana"

		示例 2：
		输入：s = "abcd"
		输出：""

		提示：
		2 <= s.length <= 3 * 10^4
		s 由小写英文字母组成
	*/
	// 从长度1开始，如 a，出现的位置有三个， 那么考虑 an 的时候，an最多也是三个，找到a的三个位置，后面是否都是n，ana 以此类推
	return ""
}
