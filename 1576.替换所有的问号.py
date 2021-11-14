#
# @lc app=leetcode.cn id=1576 lang=python
#
# [1576] 替换所有的问号
#

# @lc code=start
class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        lyst = list(s)

        for idx in range(0, len(s)):
            if lyst[idx] != '?':
                continue
            for ch in range(97, 123):
                c = chr(ch)
                if idx > 0 and lyst[idx-1] == c:
                    continue
                if idx < len(s) -1 and lyst[idx+1] == c:
                    continue
                lyst[idx] = c
                break
        return ''.join(lyst)
# @lc code=end

