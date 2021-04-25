#
# @lc app=leetcode.cn id=1021 lang=python
#
# [1021] 删除最外层的括号
#

# @lc code=start
class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        l, r = 0, 0
        res = ""
        tmp = ""
        
        for ch in S:
            if ch == "(":
                l += 1
            if ch == ")":
                r += 1
            tmp += ch
            if l == r:
                tmp = tmp[1:-1]
                res += tmp
                l, r = 0, 0
                tmp = ""
        return res
# @lc code=end

