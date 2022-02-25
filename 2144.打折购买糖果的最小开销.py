#
# @lc app=leetcode.cn id=2144 lang=python
#
# [2144] 打折购买糖果的最小开销
#

# @lc code=start
class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.sort(reverse=True)
        res = 0
        while len(cost) >= 3:
            res += cost[0] + cost[1]
            cost = cost[3:]
        res += sum(cost)
        return res
# @lc code=end

