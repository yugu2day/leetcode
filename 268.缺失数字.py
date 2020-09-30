#
# @lc app=leetcode.cn id=268 lang=python
#
# [268] 缺失数字
#

# @lc code=start
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        n = len(nums)
        for i in range(0, n):
            res += i - nums[i]
        res += n
        return res
# @lc code=end

