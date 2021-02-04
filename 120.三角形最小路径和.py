#
# @lc app=leetcode.cn id=120 lang=python
#
# [120] 三角形最小路径和
#

# @lc code=start
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = triangle[-1]

        for row in triangle[:-1][::-1]:

            for i in range(0, len(row)):
                dp[i] = min(dp[i], dp[i+1]) + row[i]
        return dp[0]
# @lc code=end

