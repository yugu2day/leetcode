#
# @lc app=leetcode.cn id=1252 lang=python
#
# [1252] 奇数值单元格的数目
#

# @lc code=start
class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        res = 0
        row, col = dict(), dict()
        for [r, c] in indices:
            row[r] = row.get(r, 0) + 1
            col[c] = col.get(c, 0) + 1
        for r in range(0, n):
            if row.get(r, 0) % 2 != 0:
                for c in range(0, m):
                    if col.get(c, 0) % 2 == 0:
                        res += 1
            else:
                for c in range(0, m):
                    if col.get(c, 0) % 2 != 0:
                        res += 1
            
        return res
        
# @lc code=end

