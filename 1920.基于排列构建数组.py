#
# @lc app=leetcode.cn id=1920 lang=python
#
# [1920] 基于排列构建数组
#

# @lc code=start
class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = [0] * len(nums)
        for i in range(0, len(nums)):
            arr[i] = nums[nums[i]]
        return arr
# @lc code=end

