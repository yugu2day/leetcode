#
# @lc app=leetcode.cn id=1380 lang=python
#
# [1380] 矩阵中的幸运数
#

# @lc code=start
class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        m = zip(*matrix)

        for r in range(0, len(matrix)):
            for c in range(0, len(matrix[r])):
                if min(matrix[r]) == max(m[c]):
                    res.append(max(m[c]))
        return res
# @lc code=end

