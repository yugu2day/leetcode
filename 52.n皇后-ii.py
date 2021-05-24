#
# @lc app=leetcode.cn id=52 lang=python
#
# [52] N皇后 II
#

# @lc code=start
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        row = [False] * n
        col = [False] * n
        dia1 = [False] * (2*n - 1)
        dia2 = [False] * (2*n - 1)
        self.res = 0

        def helper(cur, row, col, dia1, dia2):
            if cur == n:
                self.res += 1
                return
            for i in range(0, n):
                if not row[cur] and not col[i] and not dia1[cur-i+n-1] and not dia2[cur+i]:
                    row[cur] = True
                    col[i] = True
                    dia1[cur-i+n-1] = True
                    dia2[cur+i] = True
                    helper(cur+1, row[:], col[:], dia1[:], dia2[:])
                    row[cur] = False
                    col[i] = False
                    dia1[cur-i+n-1] = False
                    dia2[cur+i] = False
        
        helper(0, row, col, dia1, dia2)
        return self.res

# @lc code=end

