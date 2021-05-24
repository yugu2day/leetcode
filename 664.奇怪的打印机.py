#
# @lc app=leetcode.cn id=664 lang=python
#
# [664] 奇怪的打印机
#

# @lc code=start
class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[float('inf') for _ in range(0, len(s))] for _ in range(0 ,len(s))]
        dp[0][0] = 1

        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if i == j:
                    dp[i][j] = 1
                    continue
                if s[i] == s[j]: # 首尾在一行上
                    dp[i][j] = dp[i][j-1]
                    continue
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])

        return dp[0][-1]
# @lc code=end

