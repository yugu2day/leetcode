#
# @lc app=leetcode.cn id=1266 lang=python
#
# [1266] 访问所有点的最小时间
#

# @lc code=start
class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for i, [x, y] in enumerate(points[:-1]):
            [x1, y1] = points[i+1]
            gap = min(abs(x1-x), abs(y1-y))
            res += gap + max(abs(x1-x)-gap, abs(y1-y)-gap)
        return res 
# @lc code=end

