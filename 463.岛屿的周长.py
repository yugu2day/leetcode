#
# @lc app=leetcode.cn id=463 lang=python
#
# [463] 岛屿的周长
#

# @lc code=start
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for row in range(0, len(grid)):
            for col in range(0, len(grid[row])):
                if grid[row][col] == 1:
                    res += self.get_around(grid, row, col)
        return res

    
    def get_around(self, grid, row, col):
        # 获取(row, col)的周长
        around = 0
        if row == 0:
            around += 1
        else:
            if grid[row-1][col] == 0:
                around += 1
    
        if col == 0:
            around += 1
        else:
            if grid[row][col-1] == 0:
                around += 1
        
        if row == len(grid) - 1:
            around += 1
        else:
            if grid[row+1][col] == 0:
                around += 1
        
        if col == len(grid[0]) - 1:
            around += 1
        else:
            if grid[row][col+1] == 0:
                around += 1
        return around
# @lc code=end

