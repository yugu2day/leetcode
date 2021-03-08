#
# @lc app=leetcode.cn id=999 lang=python
#
# [999] 可以被一步捕获的棋子数
#

# @lc code=start
class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        for row in range(0, len(board)):
            for col in range(0, len(board[row])):
                if board[row][col] != "R":
                    continue
                return self.check(board, row, col)
    
    def check(self, board, row, col):
        res = 0
        for r in range(row-1, -1, -1):
            if board[r][col] == '.':
                continue
            if board[r][col] == "B":
                break
            if board[r][col] == "p":
                res += 1
                break
        for r in range(row+1, len(board)):
            if board[r][col] == '.':
                continue
            if board[r][col] == "B":
                break
            if board[r][col] == "p":
                res += 1
                break
        for c in range(col-1, -1, -1):
            if board[row][c] == ".":
                continue
            if board[row][c] == "B":
                break
            if board[row][c] == "p":
                res += 1
                break
        for c in range(col+1, len(board[row])):
            if board[row][c] == ".":
                continue
            if board[row][c] == "B":
                break
            if board[row][c] == "p":
                res += 1
                break
        return res
# @lc code=end

