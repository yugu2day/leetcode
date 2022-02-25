#
# @lc app=leetcode.cn id=2154 lang=python
#
# [2154] 将找到的值乘以 2
#

# @lc code=start
class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        nums = set(nums)
        while original in nums:
            original *= 2
        return original
# @lc code=end

