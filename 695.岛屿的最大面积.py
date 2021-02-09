#
# @lc app=leetcode.cn id=695 lang=python
#
# [695] 岛屿的最大面积
#

# @lc code=start
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        self.visited = set()
        for row in range(0, len(grid)):
            for col in range(0, len(grid[row])):
                if grid[row][col] == 1 and (row,col) not in self.visited:
                    area = self.get_area(row, col, grid)

                    res = max(res, area)
        return res
    

    def get_area(self, row, col, grid):
        if row < 0 or row >= len(grid) or col < 0 or col >=len(grid[0]):
            return 0 
        
        if grid[row][col] == 0 or (row, col) in self.visited:
            return 0
        self.visited.add((row, col))
        return 1 + self.get_area(row-1, col, grid) + self.get_area(row+1, col, grid) + self.get_area(row, col-1, grid) + self.get_area(row, col+1, grid) 



# @lc code=end

