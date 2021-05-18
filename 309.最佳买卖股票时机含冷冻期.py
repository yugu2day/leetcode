#
# @lc app=leetcode.cn id=309 lang=python
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # dp[i][0] 第i天持有股票
        # dp[i][1] 第i天不持有股票且在冷冻期
        # dp[i][2] 第i天不持有股票也不在冷冻期
        dp = [[0,0,0] for _ in range(len(prices))]
        dp[0] = [-prices[0], 0, 0]

        for i in range(1, len(prices)):

            dp[i][0] = max(dp[i-1][0], dp[i-1][2]-prices[i])
            dp[i][1] = prices[i] + dp[i-1][0]
            dp[i][2] = max(dp[i-1][1], dp[i-1][2])
        # print dp
        return max(dp[-1])
# @lc code=end

