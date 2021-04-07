#
# @lc app=leetcode.cn id=1221 lang=python
#
# [1221] 分割平衡字符串
#

# @lc code=start
class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        cr, cl = 0, 0
        res = 0
        for ch in s:
            if ch == "R":
                cr += 1
            else:
                cl += 1
            if cr == cl:
                res += 1
                cr, cl = 0, 0
        return res
# @lc code=end

