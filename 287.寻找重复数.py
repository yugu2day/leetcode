#
# @lc app=leetcode.cn id=287 lang=python
#
# [287] 寻找重复数
#

# @lc code=start
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for n in nums:
        if nums[abs(n)-1] < 0:
            return abs(n)
        nums[abs(n)-1] *= -1
# @lc code=end

