#
# @lc app=leetcode.cn id=1184 lang=python
#
# [1184] 公交站间的距离
#

# @lc code=start
class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        s = sum(distance)
        tmp = sum(distance[start:destination]) if destination > start else sum(distance[start:] + distance[:destination])
        return min(tmp, s-tmp)
# @lc code=end

