#
# @lc app=leetcode.cn id=41 lang=python
#
# [41] 缺失的第一个正数
#

# @lc code=start
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        for i in range(1, 301):
            if i not in nums:
                return i
# @lc code=end

