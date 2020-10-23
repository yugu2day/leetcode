#
# @lc app=leetcode.cn id=492 lang=python
#
# [492] 构造矩形
#

# @lc code=start
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        res = []
        for l in range(area, int(math.sqrt(area)) - 1, -1):
            if area % l != 0:
                continue
            r = area // l
            if l >= r:
                res = [l, area // l]
        return res
# @lc code=end

