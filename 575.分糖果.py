#
# @lc app=leetcode.cn id=575 lang=python
#
# [575] 分糖果
#

# @lc code=start
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        c = dict()
        for t in candies:
            c[t] = c.get(t, 0) + 1
        all_t = len(c.keys())
        sis_c = len(candies) // 2
        return all_t if all_t <= sis_c else sis_c
# @lc code=end

