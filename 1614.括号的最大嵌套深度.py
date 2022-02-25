#
# @lc app=leetcode.cn id=1614 lang=python
#
# [1614] 括号的最大嵌套深度
#

# @lc code=start
class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        stack = []
        for ch in s:
            if ch == '(':
                stack.append('(')
            elif ch == ')':
                stack.pop()
            res = max(res, len(stack))
        return res
# @lc code=end

