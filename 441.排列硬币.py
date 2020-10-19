#
# @lc app=leetcode.cn id=441 lang=python
#
# [441] 排列硬币
#

# @lc code=start
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        row = 1
        while total + row <= n:
            total += row
            row += 1
        return row - 1
# @lc code=end

