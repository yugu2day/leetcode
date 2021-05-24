#
# @lc app=leetcode.cn id=1738 lang=python
#
# [1738] 找出第 K 大的异或坐标值
#

# @lc code=start
class Solution(object):
    def kthLargestValue(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        helper = [row[:] for row in matrix]
        res = [matrix[0][0]]

        for i in range(1, len(helper[0])):
            helper[0][i] = helper[0][i-1] ^ matrix[0][i]
            res.append(helper[0][i])
        for j in range(1, len(helper)):
            helper[j][0] = helper[j-1][0] ^ matrix[j][0]
            res.append(helper[j][0])

        for i in range(1, len(helper)):
            for j in range(1, len(helper[i])):
                helper[i][j] = helper[i-1][j] ^ helper[i][j-1] ^ helper[i-1][j-1] ^ matrix[i][j]
                res.append(helper[i][j])

        res.sort(reverse=True)
        return res[k-1]
# @lc code=end

