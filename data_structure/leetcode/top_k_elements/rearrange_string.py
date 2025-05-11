# coding=utf-8
import heapq


class Solution:
    def reorganizeString(self, S: str) -> str:
        """Rearrange String (hard)

        ```js
        重构字符串
        给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。

        若可行，输出任意可行的结果。若不可行，返回空字符串。

        示例 1:

        输入: S = "aab"
        输出: "aba"
        示例 2:

        输入: S = "aaab"
        输出: ""
        注意:

        S 只包含小写字母并且长度在[1, 500]区间内。
        ```
        """
        count_map = {}

        for c in S:
            count_map[c] = count_map.get(c, 0) + 1

        max_heap = [(-cnt, c) for c, cnt in count_map.items()]
        heapq.heapify(max_heap)

        result_chars = []

        # 每次取最多的两个字符, 交替, 最多的在前, 知道最少的没了, 再把最多的字符和最新计数放入堆中
        while max_heap:
            if len(max_heap) == 1:
                cnt, c = -max_heap[0][0], max_heap[0][1]

                if cnt > 1:
                    return ''
                elif cnt == 1:
                    result_chars.append(c)

                break

            big = heapq.heappop(max_heap)
            big_cnt = -big[0]
            big_c = big[1]

            small = heapq.heappop(max_heap)
            small_cnt = -small[0]
            small_c = small[1]

            for _ in range(small_cnt):
                result_chars.append(big_c)
                result_chars.append(small_c)

            big_cnt -= small_cnt
            if big_cnt > 0:
                heapq.heappush(max_heap, (-big_cnt, big_c))

        return ''.join(result_chars)


if __name__ == '__main__':
    S = "aab"
    print(Solution().reorganizeString(S))
