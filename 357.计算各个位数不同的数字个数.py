#
# @lc app=leetcode.cn id=357 lang=python
#
# [357] 计算各个位数不同的数字个数
#

# @lc code=start
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 第一位数字9种可能，第二位数字9种可能（包括0）
        dp = [0] * (n+1)
        
        for i in range(1, n+1):
            dp[i] = self.get_n(i) + dp[i-1]
        dp[0] = 1
        return dp[-1]

    
    def get_n(self, n):
        if n == 1:
            return 10
        digits = n-1
        res = 9
        for i in range(0, digits):
            res = res * (9-i)
        return res
# @lc code=end

