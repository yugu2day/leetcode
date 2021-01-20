#
# @lc app=leetcode.cn id=63 lang=python
#
# [63] 不同路径 II
#

# @lc code=start
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0

        dp = [[0] * len(obstacleGrid[0]) for _ in range(0, len(obstacleGrid))]
        dp[0][0] = 1
        for row in range(1, len(obstacleGrid)):
            if obstacleGrid[row][0] == 1:
                dp[row][0] = 0
                continue
            
            dp[row][0] = dp[row-1][0] 
        
        for col in range(1, len(obstacleGrid[0])):
            if obstacleGrid[0][col] == 1:
                dp[0][col] = 0
                continue
            dp[0][col] = dp[0][col-1]

        for row in range(1, len(obstacleGrid)):
            for col in range(1, len(obstacleGrid[0])):
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                    continue
                dp[row][col] = dp[row-1][col] + dp[row][col-1]

        return dp[-1][-1] 
# @lc code=end

