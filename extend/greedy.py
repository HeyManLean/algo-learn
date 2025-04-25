# -*- coding: utf-8 -*-


class Solution:
    def jump(self, nums: list[int]) -> int:
        """45. 跳跃游戏 II
        给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。
        每个元素 nums[i] 表示从索引 i 向后跳转的最大长度。
        返回到达 nums[n - 1] 的最小跳跃次数。

        输入: nums = [2,3,1,1,4]
        输出: 2
        解释: 跳到最后一个位置的最小跳跃数是 2。从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

        输入: nums = [2,3,0,1,4]
        输出: 2
        """
        # 全局已经保证一定能达到，则不需要判断不能到达
        # 贪心算法
        # 遍历每个位置，计算全局最长到达位置，如果超过数组长度，则返回ok
        # 如果每次遍历，计算后最大长度小于等于当前位置，则返回false
        max_dist = 0
        end = 0  # 上次的位置，肯定当时最长距离的位置
        n = len(nums)
        step = 0
        for i in range(n - 1):
            if i + nums[i] > max_dist:
                max_dist = i + nums[i]

            if end == i:
                end = max_dist
                step += 1
        return step

        # 贪心算法
        # 在可跳跃的位置中，选择下一次跳跃可以更远的那个位置
        q = [0]
        target = len(nums) - 1
        step = 0

        while q:
            for _ in range(len(q)):
                i = q.pop(0)
                if i == target:
                    return step

                if i + nums[i] >= target:
                    return step + 1

                # 选取下一跳最大的值
                max_dist = 0
                nxt = i
                for j in range(i + 1, i + nums[i] + 1):
                    if j + nums[j] > max_dist:
                        nxt = j
                        max_dist = j + nums[j]

                if nxt != i:
                    q.append(nxt)

            step += 1
        return -1
    
    def canJump(self, nums: list[int]) -> bool:
        """55. 跳跃游戏
        给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
        数组中的每个元素代表你在该位置可以跳跃的最大长度。

        判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。

        输入：nums = [2,3,1,1,4]
        输出：true

        输入：nums = [3,2,1,0,4]
        输出：false
        """
        # 贪心算法
        # 遍历每个位置，计算全局最长到达位置，如果超过数组长度，则返回ok
        # 如果每次遍历，计算后最大长度小于等于当前位置，则返回false
        max_dist = 0
        n = len(nums)
        for i in range(n - 1):
            if i + nums[i] > max_dist:
                max_dist = i + nums[i]

            if max_dist <= i:
                return False
            
        return max_dist >= n - 1

        q = [0]
        target = len(nums) - 1

        while q:
            for _ in range(len(q)):
                i = q.pop(0)
                if i == target:
                    return True

                if i + nums[i] >= target:
                    return True

                # 选取下一跳最大的值
                max_dist = 0
                nxt = i
                for j in range(i + 1, i + nums[i] + 1):
                    if j + nums[j] > max_dist:
                        nxt = j
                        max_dist = j + nums[j]

                if nxt != i:
                    q.append(nxt)

        return False


if __name__ == "__main__":
    print(Solution().jump([2, 3, 1, 1, 4]))
    assert Solution().jump([2, 3, 1, 1, 4]) == 2
    assert Solution().jump([2, 3, 0, 1, 4]) == 2
    assert Solution().jump([0]) == 0
    assert Solution().canJump([2, 3, 1, 1, 4])
    assert Solution().canJump([2, 3, 0, 1, 4])
    assert not Solution().canJump([0, 1])
