#
# @lc app=leetcode.cn id=1232 lang=python
#
# [1232] 缀点成线
#

# @lc code=start
class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        # (y2-y1)/(x2-x1) = (y3-y2)/(x3-x2)
        # (y2-y1)*(x3-x2) = (y3-y2)*(x2-x1)

        for i in range(1, len(coordinates)-1):
            [x1, y1] = coordinates[i-1]
            [x2, y2] = coordinates[i]
            [x3, y3] = coordinates[i+1]
            if (y2-y1)*(x3-x2) != (y3-y2)*(x2-x1):
                return False
        return True
# @lc code=end

