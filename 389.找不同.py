#
# @lc app=leetcode.cn id=389 lang=python
#
# [389] 找不同
#

# @lc code=start
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = sorted(list(s))
        t = sorted(list(t))

        for index in range(0, len(s)):
            if s[index] != t[index]:
                return t[index]
        return t[-1]

# @lc code=end

