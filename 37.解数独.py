#
# @lc app=leetcode.cn id=37 lang=python
#
# [37] 解数独
#

# @lc code=start
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.rowB, self.colB = [[False] * 9 for _ in range(9)], [[False] * 9 for _ in range(9)]
        self.block = [[False] * 9 for _ in range(9)]
        self.stack = []
        self.valid = False

        for row in range(0, len(board)):
            for col in range(0, len(board[row])):
                if board[row][col] != '.':
                    n = int(board[row][col])
                    self.rowB[row][n-1] = True
                    self.colB[col][n-1] = True

                    b = row / 3 * 3 + col / 3 
                    self.block[b][n-1] = True
                else:
                    self.stack.append([row, col])
        
        def dfs(pos):
            if pos == len(self.stack):
                self.valid = True
                return
            
            [row, col] = self.stack[pos]

            for i in range(1, 10):
                if self.check(row, col, i, board):

                    board[row][col] = str(i)
                    self.rowB[row][i-1] = True
                    self.colB[col][i-1] = True
                    self.block[row / 3 * 3 + col / 3 ][i-1] = True
                    dfs(pos+1)

                    if self.valid:
                        return
                    
                    self.rowB[row][i-1] = False
                    self.colB[col][i-1] = False
                    self.block[row / 3 * 3 + col / 3 ][i-1] = False
        
        dfs(0)

    

    def check(self, row, col, num, board):

        if self.rowB[row][num-1]:
            return False
        
        if self.colB[col][num-1]:
            return False

        if self.block[row / 3 * 3 + col / 3 ][num-1]:
            return False

        return True
# @lc code=end

