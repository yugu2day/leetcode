#
# @lc app=leetcode.cn id=413 lang=python
#
# [413] 等差数列划分
#

# @lc code=start
class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)
        res = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = dp[i-1] + 1
                res += dp[i]
        return res

# @lc code=end

