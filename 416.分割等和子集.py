#
# @lc app=leetcode.cn id=416 lang=python
#
# [416] 分割等和子集
#

# @lc code=start
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return False
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        dp = [True] + [False] * target
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]
        
        return dp[target]

# @lc code=end

