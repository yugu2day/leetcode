#
# @lc app=leetcode.cn id=48 lang=python
#
# [48] 旋转图像
#

# @lc code=start
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        cur = 0
        while cur < len(matrix) // 2:
            
            for i in range(cur, len(matrix) - cur - 1):
                matrix[cur][i], matrix[i][len(matrix) - cur - 1], matrix[len(matrix) - cur - 1][len(matrix) - i - 1], matrix[len(matrix) - i - 1][cur] = matrix[len(matrix) - i - 1][cur], matrix[cur][i], matrix[i][len(matrix) - cur - 1], matrix[len(matrix) - cur - 1][len(matrix) - i - 1]
            
            cur += 1
# @lc code=end

