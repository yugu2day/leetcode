#
# @lc app=leetcode.cn id=1260 lang=python
#
# [1260] 二维网格迁移
#

# @lc code=start
class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        arr = [n for row in grid for n in row ]

        k = k % len(arr)
        arr = arr[-k:] + arr[:-k]

        res = []
        for i in range(0, len(arr), len(grid[0])):
            res.append(arr[i: i+len(grid[0])])
        return res
        
# @lc code=end

