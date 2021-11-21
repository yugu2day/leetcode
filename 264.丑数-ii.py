#
# @lc app=leetcode.cn id=264 lang=python
#
# [264] 丑数 II
#

# @lc code=start
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * max(n, 4)
        t2, t3, t5 = 0, 0, 0
        for i in range(1, n):
            dp[i] = min(dp[t2] * 2, dp[t3] * 3, dp[t5] * 5)
            if dp[i] == dp[t2] * 2:
                t2 += 1
            if dp[i] == dp[t3] * 3:
                t3 += 1
            if dp[i] == dp[t5] * 5:
                t5 += 1
        return dp[n-1]
# @lc code=end

