# -*- coding: utf-8 -*-


def rotate_matrix(matrix: list[list]) -> None:
    # 规律：先对称反转，在对单个数组反转
    n = len(matrix)

    # 针对对角线上半部分的单元跟下半部分交换
    for i in range(n):
        for j in range(i + 1):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # 针对每个数组进行反转
    for arr in matrix:
        i, j = 0, n - 1
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        top = 0
        bottom = m - 1
        left = 0
        right = n - 1
        res = []

        while len(res) < m * n:
            if top <= bottom:
                for i in range(left, right + 1):
                    res.append(matrix[top][i])
                top += 1

            if left <= right:
                for i in range(top, bottom + 1):
                    res.append(matrix[i][right])
                right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res


class Solution2(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # 维护 top,right,bottom,left 四个边界，不能越界
        # 每轮遍历四个方向，直到数目为 n*n
        num = 1
        top = left = 0
        right = bottom = n - 1

        matrix = [[0 for _ in range(n)] for _ in range(n)]

        while num <= n * n:
            if top <= bottom:
                for i in range(left, right + 1):
                    matrix[top][i] = num
                    num += 1
                top += 1

            if left <= right:
                for i in range(top, bottom + 1):
                    matrix[i][right] = num
                    num += 1
                right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    matrix[bottom][i] = num
                    num += 1
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1

        return matrix

if __name__ == "__main__":
    m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    rotate_matrix(m)
    assert m == [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]
    print('ok')

    assert Solution().spiralOrder([
        [1,2,3],
        [4,5,6],
        [7,8,9]]
    ) == [1,2,3,6,9,8,7,4,5]
    assert Solution().spiralOrder([
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ]) == [1,2,3,4,8,12,11,10,9,5,6,7]

    assert Solution().spiralOrder([[3],[2]]) == [3, 2]

    assert Solution2().generateMatrix(3) == [[1,2,3],[8,9,4],[7,6,5]]