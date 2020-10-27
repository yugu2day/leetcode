#
# @lc app=leetcode.cn id=598 lang=python
#
# [598] 范围求和 II
#

# @lc code=start
class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m * n

        row, col = [], []
        for [r, c] in ops:
            row.append(r)
            col.append(c)
        return min(min(row), m) * min(min(col), n)
       