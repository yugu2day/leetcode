#
# @lc app=leetcode.cn id=1582 lang=python
#
# [1582] 二进制矩阵中的特殊位置
#

# @lc code=start
class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        row = [0] * len(mat)
        col = [0] * len(mat[0])

        for r in range(len(mat)):
            for c in range(0, len(mat[0])):
                if mat[r][c] == 1:
                    row[r] += 1
                    col[c] += 1

        res = 0
        for r in range(len(mat)):
            for c in range(0, len(mat[0])):
                if mat[r][c] == 1 and row[r] == col[c] == 1:
                    res += 1
        return res
# @lc code=end

