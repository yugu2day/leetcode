#
# @lc app=leetcode.cn id=42 lang=python
#
# [42] 接雨水
#

# @lc code=start
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        tmp, cur = 0, 0
        res = 0
        for h in height:
            if h < cur:
                tmp += cur - h
            else:
                cur = h
                res += tmp
                tmp = 0
        tmp, cur = 0, 0
        for h in height[::-1]:
            if h <= cur:
                tmp += cur - h
            else:
                cur = h
                res += tmp
                tmp = 0
            
        return res
# @lc code=end

