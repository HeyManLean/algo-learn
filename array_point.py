# -*- coding: utf-8 -*-


class Solution(object):
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        # 滑动窗口，两个指针维护相同值的左右侧，如果快指针下一个值不同，则判断快慢指针之间元素个数是否小于等于2，加入到前面数组
        # 快慢慢指针指向快指针下一个位置，继续
        i = 0  # 指向下一个有效元素位置
        slow = fast = 0
        while fast + 1 < len(nums):
            if nums[fast] != nums[fast + 1]:
                if fast - slow + 1 <= 2:
                    while slow <= fast:
                        nums[i] = nums[slow]
                        i += 1
                        slow += 1
                slow = fast + 1

            fast += 1

        if fast - slow + 1 <= 2:
            while slow <= fast:
                nums[i] = nums[slow]
                i += 1
                slow += 1

        return i


Solution().removeDuplicates([1, 1, 1, 2, 2, 3])



def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    # 左右双指针，比较左右指针值是否相同，相同则一起像中间移动，否则返回false
    def validate(c: str):
        return c.isalnum()

    left, right = 0, len(s) - 1
    while left < right:
        if not validate(s[left]):
            left += 1
            continue
        if not validate(s[right]):
            right -= 1
            continue

        if s[left].lower() == s[right].lower():
            left += 1
            right -= 1
        else:
            return False

    return True


assert isPalindrome("A man, a plan, a canal: Panama")


def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    counter = [0, 0, 0]
    for n in nums:
        counter[n] += 1

    pos = 0
    for num, cnt in enumerate(counter):
        for _ in range(cnt):
            nums[pos] = num


def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
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



nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3
merge(nums1, m, nums2, n)
print(nums1)
assert nums1 == [1,2,3,4,5,6]

print("OK")