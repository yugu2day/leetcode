#
# @lc app=leetcode.cn id=11 lang=python
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        i0, i1 = 0 , len(height) - 1
        while i0 < i1:
            tmp = self.get_water(height[i0], height[i1], i1 - i0)
            res = max(tmp, res)
            if height[i0] < height[i1]:
                i0 += 1
            else:
                i1 -= 1
        return res
    
    def get_water(self, h1, h2, gap):
        return min(h1, h2) * gap
# @lc code=end

