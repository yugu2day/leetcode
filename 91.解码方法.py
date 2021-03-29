#
# @lc app=leetcode.cn id=91 lang=python
#
# [91] 解码方法
#

# @lc code=start
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * (len(s)+1)
        dp[0] = 1

        for i in range(1, len(s)+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if i >= 2 and 10 <= int(s[i-2:i]) <=26:
                dp[i] += dp[i-2]
        # print dp
        return dp[-1]
# @lc code=end

