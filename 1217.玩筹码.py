#
# @lc app=leetcode.cn id=1217 lang=python
#
# [1217] 玩筹码
#

# @lc code=start
class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        n1, n2 = 0, 0
        for pos in position:
            if pos % 2 == 0:
                n1 += 1
            else:
                n2 += 1
        return min(n1, n2)
# @lc code=end

