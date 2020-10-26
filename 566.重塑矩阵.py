#
# @lc app=leetcode.cn id=566 lang=python
#
# [566] 重塑矩阵
#

# @lc code=start
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        arr = [n for row in nums for n in row]

        if len(arr) != r * c:
            return nums
        res = [[0]*c for _ in range(r)]

        i = 0
        for row in range(0, len(res)):
            for col in range(0, len(res[row])):
                res[row][col] = arr[i]
                i += 1
        return res
# @lc code=end

