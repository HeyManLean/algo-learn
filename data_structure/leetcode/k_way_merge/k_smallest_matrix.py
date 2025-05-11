# coding=utf-8


class Solution:
    def kthSmallest(self, matrix: list, k: int) -> int:
        """Kth Smallest Number in a Sorted Matrix (Hard)

        ```js
        有序矩阵中第K小的元素
        给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
        请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

        

        示例：

        matrix = [
        [ 1,  5,  9],
        [10, 11, 13],
        [12, 13, 15]
        ],
        k = 8,

        返回 13。
        

        提示：
        你可以假设 k 的值永远是有效的，1 ≤ k ≤ n2 。
        ```
        """
        n = len(matrix)
        list_firsts = [0 for _ in range(n)]

        while k > 0:
            min_val = float('inf')
            min_inx = -1

            for i in range(n):
                first = list_firsts[i]
                if first >= n:
                    continue
                val = matrix[i][first]

                if val < min_val:
                    min_val = val
                    min_inx = i

            if min_inx != -1:
                list_firsts[min_inx] += 1

            k -= 1

        return min_val
