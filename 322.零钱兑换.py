#
# @lc app=leetcode.cn id=322 lang=python
#
# [322] 零钱兑换
#

# @lc code=start
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0

        coins = set(coins)
        dp = [float('inf')] * (amount + 1)
        for i in range(1, amount + 1):
            for coin in coins:
                if coin > i:
                    continue
                elif coin == i:
                    dp[i] = 1
                    break
                
                if dp[i-coin] != float('inf'):
                    dp[i] = min(dp[i], dp[coin] + dp[i-coin])
        return dp[-1] if dp[-1] != float('inf') else -1
# @lc code=end

