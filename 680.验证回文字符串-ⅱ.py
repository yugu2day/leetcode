#
# @lc app=leetcode.cn id=680 lang=python
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1]:
            return True

        start, end = 0, len(s) - 1

        while start <= end:
            if s[start] == s[end]:
                start += 1
                end -= 1
                continue
            else:

                if s[start:end] == s[start:end][::-1] or s[start+1:end+1] == s[start+1:end+1][::-1]:
                    return True
                else:
                    return False
        return True
# @lc code=end

