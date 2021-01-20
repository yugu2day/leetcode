#
# @lc app=leetcode.cn id=79 lang=python
#
# [79] 单词搜索
#

# @lc code=start
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for row in range(0, len(board)):
            for col in range(0, len(board[0])):
                if board[row][col] == word[0]:
                    if self.confirm(board, word, row, col):
                        return True
        return False

    

    def confirm(self, board, word, row, col):
        if not word:
            return True
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[row]):
            return False
        if board[row][col] == word[0]:
            
            tmp = [_[:] for _ in board]
            tmp[row][col] = 0
            if self.confirm(tmp, word[1:], row-1, col):
                return True
            if self.confirm(tmp, word[1:], row+1, col):
                return True
            if self.confirm(tmp, word[1:], row, col-1):
                return True
            if self.confirm(tmp, word[1:], row, col+1):
                return True
        else:
            return False

        return False
# @lc code=end

