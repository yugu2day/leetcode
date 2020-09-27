#
# @lc app=leetcode.cn id=119 lang=python
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for r in range(2, rowIndex+2):
            tmp = []
            for i in range(1, r-1):
                tmp.append(row[i-1] + row[i])
            row = [1] + tmp + [1]
        return row

# @lc code=end

