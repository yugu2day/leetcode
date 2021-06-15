#
# @lc app=leetcode.cn id=212 lang=python
#
# [212] 单词搜索 II
#

# @lc code=start
class Solution(object):
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 记录每个字符的初始坐标
        pos = collections.defaultdict(list)
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                pos[board[i][j]].append((i,j))

        res = []
        for word in words:
            queue = pos[word[0]]
            for (row, col) in queue:
                visited = set()
                if self.check(row, col, word, board, visited):
                    res.append(word)
                    break
        return res

    
    def check(self, row, col, word, board, visited):
        if len(word) == 0:
            return True

        if row < 0 or row >= len(board) or col < 0 or col >= len(board[row]) or (row, col) in visited:
            return False

        if board[row][col] != word[0]:
            return False

        visited.add((row, col))
        return self.check(row-1, col, word[1:], board, visited) or self.check(row, col-1, word[1:], board, visited) or self.check(row+1, col, word[1:], board, visited) or self.check(row, col+1, word[1:], board, visited)
# @lc code=end

