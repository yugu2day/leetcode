#
# @lc app=leetcode.cn id=118 lang=python
#
# [118] 杨辉三角
#

# @lc code=start
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []

        res = [[1]]
        for r in range(2, numRows+1):
            tmp = []
            for i in range(1, r - 1):
                tmp.append(res[r-2][i-1] + res[r-2][i])
            tmp = [1] + tmp + [1]
            res.append(tmp)
        return res

# @lc code=end

