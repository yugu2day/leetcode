#
# @lc app=leetcode.cn id=279 lang=python
#
# [279] 完全平方数
#

# @lc code=start
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [i for i in range(n+1)]  # 假设每一步都是1*1 加起来
        
        for i in range(1, n+1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j += 1

        return dp[n]
# @lc code=end

