#
# @lc app=leetcode.cn id=1051 lang=python
#
# [1051] 高度检查器
#

# @lc code=start
class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        res = 0
        h = sorted(heights)
        for i in range(0, len(heights)):
            if h[i] != heights[i]:
                res += 1
        return res
# @lc code=end

