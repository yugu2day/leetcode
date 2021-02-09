#
# @lc app=leetcode.cn id=714 lang=python
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # dp[0] 不持有 dp[1] 持有
        dp = [[0, 0] for _ in range(len(prices))]

        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for idx, price in enumerate(prices):
            if idx == 0:
                continue
            
            dp[idx][0] = max(dp[idx-1][1] +prices[idx] - fee, dp[idx-1][0])  #idx-1持有的卖掉 或 idx-1持续不持有
            dp[idx][1] = max(dp[idx-1][0]-prices[idx], dp[idx-1][1])  # idx -1 不持有变持有 idx-1 持有继续买入
            
        return max(dp[-1])
# @lc code=end

