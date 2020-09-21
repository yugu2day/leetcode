#
# @lc app=leetcode.cn id=28 lang=python
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == needle:
            return 0
        len_h = len(haystack)
        len_n = len(needle)
        for i in range(0, len_h - len_n + 1):
            if haystack[i: i + len_n] == needle:
                return i
        return -1
# @lc code=end

