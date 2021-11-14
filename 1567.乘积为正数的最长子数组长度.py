#
# @lc app=leetcode.cn id=1567 lang=python
#
# [1567] 乘积为正数的最长子数组长度
#

# @lc code=start
class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [[0, 0]] # dp[i][0] 乘积为正数的长度 , dp[i][1] 乘积为负数的长度
        res = 0
        for num in nums:
            item = [0, 0]
            if num > 0:
                item[0] = dp[-1][0] + 1
                item[1] = dp[-1][1] + 1 if dp[-1][1] > 0 else 0

            elif num < 0:
                item[0] = dp[-1][1] + 1 if dp[-1][1] > 0 else 0
                item[1] = dp[-1][0] + 1 
            else:
                item = [0, 0]
            res = max(res, item[0])
            dp.append([item[0], item[1]])

        return res

# @lc code=end

