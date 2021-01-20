#
# @lc app=leetcode.cn id=59 lang=python
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for _ in range(n)]

        end = len(matrix) // 2
        tmp = 1

        for cur in range(0, end + 1):
            for col in range(cur, n - cur):
                matrix[cur][col] = tmp
                tmp += 1
            for row in range(cur + 1, n - cur):
                matrix[row][n - cur - 1] = tmp
                tmp += 1

            for col in range(n-cur-2, cur, -1):
                matrix[n-cur-1][col] = tmp
                tmp += 1
            for row in range(n-cur-1, cur, -1):
                matrix[row][cur] = tmp
                tmp += 1

        return matrix
# @lc code=end

