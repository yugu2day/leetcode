#
# @lc app=leetcode.cn id=121 lang=python
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        res = 0
        lowest = prices[0]
        for i in range(1, len(prices)):
            if lowest > prices[i]:
                lowest = prices[i]
            else:
                res = max(res, prices[i] - lowest)
        return res
# @lc code=end

