

## 双指针

### 合并两个有序数组

1. 两个指针分别指向两个数组尾部
2. 比较两指针大小，最大值加入新数组结尾，并往前一步

```py
def merge(nums1, m, nums2, n):
    # 左右比较，将较大值跟当前尾部值交换
    tail = m + n
    m -= 1
    n -= 1

    while m >= 0 or n >= 0:
        tail -= 1
        if m < 0:
            nums1[tail] = nums2[n]
            n -= 1
            continue
        if n < 0:
            break

        if nums1[m] < nums2[n]:
            nums1[tail] = nums2[n]
            n -= 1
        else:
            nums1[tail] = nums1[m]
            m -= 1
```

### 有序数组的平方（977）

1. 将负数和正数看做两个有序数组
2. 指针1指向负数的开头，指针2指向正数的结尾
3. 对比两个指针平方的大小，将较大值加入新数组结尾，如果是负数大，负数指针前进一步，否则正数指针后退一步

```py
def sortedSquares(nums):
    # 越小的负数平方后越大
    # 可以讲原本数组分为两部分，负数和正数
    # 问题将变成了合并两个有序数组
    # 左右指针
    ret = [0] * len(nums)
    left = 0
    right = len(nums) - 1

    tail = right

    while left <= right:
        if nums[left] ** 2 > nums[right] ** 2:
            ret[tail] = nums[left] ** 2
            left += 1
        else:
            ret[tail] = nums[right] ** 2
            right -= 1
        tail -= 1

    return ret
```

## 滑动窗口

### 最小覆盖子串（76）

- [76](https://leetcode.cn/problems/minimum-window-substring/)
滑动窗口，右指针向前，并记录元素个数，当符合要求需要收缩时，左指针开始收缩直到不符合要求

1. 字典1维护目标字符的个数，字典2维护当前窗口中每个字符的个数，数值变量 contain_count 维护当前涵盖的字符数量
2. 右指针向前
- 如果字符在目标字符中，则字典2对应字符数值加一
- 如果该字符当前数值等于目标字典1对应字符的数值，则 contain_count 加1
3. contain_count等于目标字符串的个数，则将当前结果记录，开始搜索左指针

```py
def minWindow(s: str, t: str) -> str:
    # 1. 滑动窗口，维护当前包含 t 所有字符的子串
    # 2. 计数器维护 t 每个字符在滑动中的个数
    # 3. 字符数变量，表示t中多少个字符在滑动窗口中，如果跟t的长度一样，表示已经涵盖t所有字符

    # t 的字符允许重复，需要维护各字符的目标个数

    left = right = 0
    counter = {}
    target_counter = {}
    for c in t:
        target_counter.setdefault(c, 0)
        target_counter[c] += 1
        counter[c] = 0

    contain_count = 0
    result = ""

    while right < len(s):
        if s[right] in counter:
            if counter[s[right]] < target_counter[s[right]]:
                contain_count += 1
            counter[s[right]] += 1

        right += 1

        # 将左边指针收缩，直到不能覆盖 t 所有字符
        while left < right and contain_count == len(t):
            if not result or len(result) > right - left:
                result = s[left:right]

            if s[left] in counter:
                if counter[s[left]] <= target_counter[s[left]]:
                    contain_count -= 1
                counter[s[left]] -= 1

            left += 1

    return result
```

### 字符串排列（567）

滑动窗口
- 左指针收缩的终止条件是窗口长度大于等于目标字符串长度

```py
def checkInclusion(s1, s2):
    # 滑动窗口
    # 目标计数器维护目标个数
    # 滑动窗口计数器维护当前字符个数
    # int变量维护当前窗口覆盖s1的字符个数
    # int变量维护当前窗口非s1的字符个数

    # 窗口左右侧，左闭右开
    left = right = 0
    # valid表示覆盖s1的字符个数，other表示包含其他字符个数
    valid = 0
    # needs 表示需要的字符个数
    needs = {}
    # windows 表示当前字符（在s1中的）个数
    windows = {}
    for c in s1:
        needs.setdefault(c, 0)
        needs[c] += 1
        windows[c] = 0

    while right < len(s2):
        if s2[right] in windows:
            # 还没超过目标字符所需的个数，valid 加一
            if windows[s2[right]] < needs[s2[right]]:
                valid += 1
            windows[s2[right]] += 1
        right += 1

        # 维持当前滑动窗口在 s1 的长度，当能包含s1则返回True，否则加入下一个元素
        while right - left >= len(s1):
            if valid == len(s1):
                return True

            if s2[left] in windows:
                if windows[s2[left]] <= needs[s2[left]]:
                    valid -= 1
                windows[s2[left]] -= 1

            left += 1
        
    return False
```

### 无重复字符的最长子串

1. 记录重复字符数，并进行滑动
2. 如果当前重复字符为0，则记录当前最大长度
- 左指针收缩的终止条件是重复字符为0

```py
def lengthOfLongestSubstring(s):
    counter = {}
    left = right = 0
    res = 0
    dups = 0

    while right < len(s):
        counter[s[right]] = counter.get(s[right], 0) + 1
        if counter[s[right]] == 2:
            dups += 1

        right += 1

        while dups > 0:
            if counter[s[left]] == 2:
                dups -= 1
            counter[s[left]] -= 1
            left += 1

        res = max(right - left, res)

    return res
```

## 反转

### 旋转图像（48）

1. 将矩阵对称反转
2. 针对每一行各自进行反转

```py
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
```

### 螺旋矩阵（54）

1. 维护 top,right,bottom,left 四个边界，不能越界
2. 每轮遍历四个方向，直到数目满足要求为止
    - 顶部，从左到右遍历，top加一
    - 右侧，从上到下遍历，right减一
    - 底部，从右到左遍历，bottom减一
    - 左侧，从下到上遍历，left加一


```py
def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    n = len(matrix)
    top = 0
    bottom = n - 1
    left = 0
    right = n - 1
    res = []

    while left < right or top < bottom:
        for i in range(left, right + 1):
            res.append(matrix[top][i])
            top += 1

        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
            right -= 1

        for i in range(right, left - 1, -1):
            res.append(matrix[bottom][i])
            bottom -= 1

        for i in range(bottom, top - 1, -1):
            res.append(matrix[i][left])
            left += 1

    return res
```

## 前缀数组

对于需要反复计算数组某一段区间求和的场景，使用前缀数组效率更高

1. 创建新数组 sums，新数组第 i 个元素是原来数组前 i-1 个元素之和
2. 求某个区间 `[left,right]` 的总和，直接用 `sums[right + 1] - sums[left]` 就能得出结果

```py
class NumArray:
    # 前缀和数组
    def __init__(self, nums: List[int]):
        self.sums = [0] * (len(nums) + 1)
        for i in range(1, len(self.sums)):
            self.sums[i] = self.sums[i - 1] + nums[i - 1]

    # 查询闭区间 [left, right] 的累加和
    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right + 1] - self.sums[left]
```


## 差分数组

对于经常需要对数组某区间进行差值计算，并查询某个结果
1. 维护新数组diff，第i个数值是原数组第i个数值减第i-1数值的结果
2. 当需要对某个区间`[left,right]`的数值都减某个值val，`diff[left]-=val,diff[right]+=val` 就能完成
3. 第i个最新值等于第i-1个最新值+diff[i]

### 拼车（1094）

- [https://leetcode.cn/problems/car-pooling/](https://leetcode.cn/problems/car-pooling/)

```py
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0 for _ in range(1001)]
        diff[0] = capacity

        for book in trips:
            diff[book[1]] -= book[0]
            diff[book[2]] += book[0]

        nums = []
        for i, num in enumerate(diff):
            if i == 0:
                nums.append(num)
            else:
                nums.append(nums[i - 1] + diff[i])

            if nums[-1] < 0:
                return False
        return True
```


使用动态规划方法

无限定条件
无范围约束
无下标需求
就是求最值
53 最长子数组和
使用滑动窗口

有下标需求
有至少等字眼不确定的范围限定
862 和至少为K的最短子数组
使用前缀和数组

一般与 HashMap结合使用
确定的范围限定（不使用至少等字眼）