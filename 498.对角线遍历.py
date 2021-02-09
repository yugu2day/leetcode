#
# @lc app=leetcode.cn id=498 lang=python
#
# [498] 对角线遍历
#

# @lc code=start
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        res = []
        flag = True # 向上为true ，下为false
        for cur in range(0, len(matrix) + len(matrix[0]) - 1):
            if flag:
                row = min(cur, len(matrix)-1)
                col = cur - row
            else:
                col = min(cur, len(matrix[0])-1)
                row = cur - col

            while row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix[0]):
                # print flag, row, col
                res.append(matrix[row][col])
                if flag:
                    row, col = row-1, col+1
                else:
                    row, col = row+1, col-1
            flag = True if not flag else False
            
        return res
# @lc code=end

