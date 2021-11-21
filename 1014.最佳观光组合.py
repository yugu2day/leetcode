#
# @lc app=leetcode.cn id=1014 lang=python
#
# [1014] 最佳观光组合
#

# @lc code=start
class Solution(object):
    def maxScoreSightseeingPair(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        tmp = values[0] + 0
        res = 0
        for i in range(1, len(values)):
            res = max(res, tmp+values[i]-i)
            tmp = max(tmp, values[i]+i)
        return res
# @lc code=end

