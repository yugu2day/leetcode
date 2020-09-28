#
# @lc app=leetcode.cn id=171 lang=python
#
# [171] Excel表列序号
#

# @lc code=start
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        while s:
            tmp = ord(s[0]) - 64
            res = 26 * res + tmp
            s = s[1:]
        return res

# @lc code=end

