#
# @lc app=leetcode.cn id=977 lang=python
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums, key=lambda x:abs(x))
        nums = map(lambda x: x*x, nums)
        return nums
# @lc code=end

