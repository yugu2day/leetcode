#
# @lc app=leetcode.cn id=461 lang=python
#
# [461] 汉明距离
#

# @lc code=start
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res = 0
        while x or y:
            if (x ^ y) & 1:
                res += 1
            x = x >> 1
            y = y >> 1
        return res
        
# @lc code=end

