#
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        dic = {')': '(', ']':'[', '}':'{'}

        while s:
            ch = s[0]
            if ch in dic:
                if not stack or stack[-1] != dic[ch]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(ch)

            s = s[1:]
        return True if not stack else False
# @lc code=end

