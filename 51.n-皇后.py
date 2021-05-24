#
# @lc app=leetcode.cn id=51 lang=python
#
# [51] N 皇后
#

# @lc code=start
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        row, col = [False] * n, [False] * n
        # / 为 dia1 \ 为 dia2
        # dia1 每列r + c 相等, dia2 每列 r-c相等
        dia1 = [False] * (2*n-1)
        dia2 = [False] * (2*n-1)

        res = []

        def helper(cur, row, col, dia1, dia2, board):
            if cur == n:
                res.append([''.join(row) for row in board])
                return
            for i in range(0, n):
                if not row[cur] and not col[i] and not dia1[cur-i+n-1] and not dia2[cur+i]:
                    row[cur] = True
                    col[i] = True
                    dia1[cur-i+n-1] = True
                    dia2[cur+i] = True
                    board[cur][i] = "Q"
                    helper(cur + 1, row[:], col[:], dia1[:], dia2[:], board)
                    board[cur][i] = "."
                    row[cur] = False
                    col[i] = False
                    dia1[cur-i+n-1] = False
                    dia2[cur+i] = False

        board = [['.'] * n for i in range(0, n)]
        helper(0, row, col, dia1, dia2, board)
        return res
    

    def getBoard(self, row, col, dia1, dia2, n):
        board = [['.'] * n for _ in range(n)]
        for r in range(0, n):
            for c in range(0, n):
                if row[r] and col[c]:
                    board[r][c] = "Q"
        return [''.join(row) for row in board]
# @lc code=end

