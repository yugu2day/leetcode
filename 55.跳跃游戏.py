#
# @lc app=leetcode.cn id=55 lang=python
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_distance = 0

        for index, step in enumerate(nums):
            if index > max_distance:
                return False

            max_distance = max(max_distance, index + step)
            if max_distance >= len(nums) - 1:
                return True
        return False

# @lc code=end

