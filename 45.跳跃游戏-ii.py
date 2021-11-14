#
# @lc app=leetcode.cn id=45 lang=python
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [float('inf') for _ in range (0, len(nums))]
        dp[0] = 0
        for idx, num in enumerate(nums):
            for j in range(1, min(len(nums), num+1)):
                if idx+j >= len(nums):
                    break
                dp[idx+j] = min(dp[idx+j], dp[idx]+1)
        return dp[-1]
# @lc code=end

