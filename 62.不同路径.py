#
# @lc app=leetcode.cn id=62 lang=python
#
# [62] 不同路径
#

# @lc code=start
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * n for _ in range(m)]
        for col in range(0, len(dp[0])):
            dp[0][col] = 1
        for row in range(0, len(dp)):
            dp[row][0] = 1
        
        for row in range(1, len(dp)):
            for col in range(1, len(dp[0])):
                dp[row][col] = dp[row-1][col] + dp[row][col - 1]
        return dp[-1][-1]
# @lc code=end

