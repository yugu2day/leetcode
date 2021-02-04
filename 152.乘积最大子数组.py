#
# @lc app=leetcode.cn id=152 lang=python
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)

        dp[0] = (nums[0], nums[0])
        res = nums[0]
        for i, num in enumerate(nums):
            if i == 0:
                continue
            dp[i] = (max(dp[i-1][0] * num, num, dp[i-1][1] * num), min(dp[i-1][0] * num, dp[i-1][1] * num, num))
            res = max(dp[i][0], dp[i][1], res)
        # print dp
        return res
# @lc code=end

