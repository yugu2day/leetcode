#
# @lc app=leetcode.cn id=844 lang=python
#
# [844] 比较含退格的字符串
#

# @lc code=start
class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        return self.f(s) == self.f(t)
    

    def f(self, s):
        s1 = []
        for ch in s:
            if ch != "#":
                s1.append(ch)
            else:
                if s1:
                    s1.pop()
        return ''.join(s1)
# @lc code=end

