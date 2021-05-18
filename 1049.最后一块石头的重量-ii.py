#
# @lc app=leetcode.cn id=1049 lang=python
#
# [1049] 最后一块石头的重量 II
#

# @lc code=start
class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        if len(stones) == 1:
            return stones[0]
        # dp[i] 为n块石头凑成的重量为i
        total = sum(stones)

        # dp[i][j] 序号i个石头在重量不超过j的情况下和的最大值
        dp = [[0] * (total / 2 + 1) for _ in range(len(stones))]
        
        for j in range(stones[0], total/2+1):
            dp[0][j] = stones[0]
        
        for i in range(1, len(stones)):
            for j in range(total/2+1):
                if j >= stones[i]:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-stones[i]] + stones[i])
                else:
                    dp[i][j] = dp[i-1][j]
        return abs(total - 2 * dp[-1][-1])
# @lc code=end

