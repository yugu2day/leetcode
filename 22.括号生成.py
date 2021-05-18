#
# @lc app=leetcode.cn id=22 lang=python
#
# [22] 括号生成
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        self.n = n

        def helper(l, r, s):
            if l == r and l == self.n:
                self.res.append(s)
                return
                
            if l < self.n:
                helper(l+1, r, s+'(')
            if l > r:
                helper(l, r+1, s+')')

        helper(1, 0, '(')
        return self.res
# @lc code=end

