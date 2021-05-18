#
# @lc app=leetcode.cn id=343 lang=python
#
# [343] 整数拆分
#

# @lc code=start
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
    
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])

        return dp[-1]
# @lc code=end

