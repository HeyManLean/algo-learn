# coding=utf-8


def squaring_sorted_array(A: list):
    """Squaring a Sorted Array (easy)

    ```js
    有序数组的平方
    给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。

    示例 1：

    输入：[-4,-1,0,3,10]
    输出：[0,1,9,16,100]
    示例 2：

    输入：[-7,-3,2,3,11]
    输出：[4,9,9,49,121]


    提示：

    1 <= A.length <= 10000
    -10000 <= A[i] <= 10000
    A 已按非递减顺序排序。
    ```
    """
    posi = -1

    n = len(A)

    res = []

    nega_squas = []

    for i in range(n):
        num = A[i]
        squa_num = num * num
        if num >= 0:
            if posi == -1:
                posi = i
        else:
            nega_squas.append(squa_num)

        res.append(squa_num)

    if posi <= 0:
        return res

    j = posi - 1
    while j >= 0 and posi < n:
        if res[posi] <= nega_squas[j]:
            res[posi - j - 1] = res[posi]
            posi += 1
        else:
            res[posi - j - 1] = nega_squas[j]
            j -= 1
    if j >= 0:
        while j >= 0:
            res[posi - j - 1] = nega_squas[j]
            j -= 1

    return res


if __name__ == "__main__":
    A = [-2, 0]
    print(squaring_sorted_array(A))
