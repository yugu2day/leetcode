#
# @lc app=leetcode.cn id=766 lang=python
#
# [766] 托普利茨矩阵
#

# @lc code=start
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for row in range(0, len(matrix)):
            if self.validPoint(matrix, row, 0) is False:
                return False
        
        for col in range(0, len(matrix[0])):
            if self.validPoint(matrix, 0, col) is False:
                return False
        return True

    def validPoint(self, matrix, row, col):
        if row >= len(matrix) - 1 or col >= len(matrix[row]) - 1:
            return True
        if matrix[row][col] != matrix[row+1][col+1]:
            return False
        
        return self.validPoint(matrix, row+1, col+1)
# @lc code=end

