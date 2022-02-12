#
# @lc app=leetcode.cn id=1020 lang=python
#
# [1020] 飞地的数量
#

# @lc code=start
class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = []

        res = 0
        for row in range(0, len(grid)):
            for col in range(0, len(grid[row])):
                if grid[row][col] != 1:
                    continue
                # 获取所有陆地的数量
                res += 1
                if row == 0 or col == 0 or row == len(grid) - 1 or col == len(grid[row]) - 1:
                    # 记录所有边界上的陆地
                    queue.append([row, col])
                    grid[row][col] = -1
        
        # 去掉所有可以触及到边界的陆地
        while queue:
            [row, col] = queue.pop(0)
            res -= 1

            if row > 0 and grid[row-1][col] == 1:
                queue.append([row-1, col])
                grid[row-1][col] = -1
            if col > 0 and grid[row][col-1] == 1:
                queue.append([row, col-1])
                grid[row][col-1] = -1
            if row < len(grid)-1 and grid[row+1][col] == 1:
                queue.append([row+1, col])
                grid[row+1][col] = -1
            if col < len(grid[row])-1 and grid[row][col+1] == 1:
                queue.append([row, col+1])
                grid[row][col+1] = -1
        
        return res
# @lc code=end

