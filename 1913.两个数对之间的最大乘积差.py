#
# @lc app=leetcode.cn id=1913 lang=python
#
# [1913] 两个数对之间的最大乘积差
#

# @lc code=start
class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]
# @lc code=end

