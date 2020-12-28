#
# @lc app=leetcode.cn id=134 lang=python
#
# [134] 加油站
#

# @lc code=start
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(cost) > sum(gas):
            return -1
        
        tmp = 0
        start = 0
        for i in range(0, len(gas)):
            tmp += gas[i] - cost[i]
            if tmp < 0:
                tmp = 0
                start = i + 1
        return start
# @lc code=end

