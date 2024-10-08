#
# @lc app=leetcode.cn id=871 lang=python
#
# [871] 最低加油次数
#

# @lc code=start
class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        # 动态规划获取加i次油能到达的最远距离
        n = len(stations)
        dp = [0] * (n+1)
        dp[0] = startFuel
        if dp[0] >= target:
            return 0
        
        for i, s in enumerate(stations):
            for j in range(i, -1, -1):
                if dp[j] >= s[0]:
                    dp[j+1] = max(dp[j+1], dp[j]+s[1])
        
        for i in range(0, len(dp)):
            if dp[i] >= target:
                return i 
        return -1
# @lc code=end

