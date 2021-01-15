#
# @lc app=leetcode.cn id=54 lang=python
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        while matrix:
            res.extend(matrix.pop(0))

            if matrix:
                for r in matrix:
                    if r:
                        res.append(r.pop())

            if matrix:
                res.extend(matrix.pop()[::-1])
                
            if matrix:
                for r in matrix[::-1]:
                    if r:
                        res.append(r.pop(0))
        return res
# @lc code=end

