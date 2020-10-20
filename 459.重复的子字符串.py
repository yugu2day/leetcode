#
# @lc app=leetcode.cn id=459 lang=python
#
# [459] 重复的子字符串
#

# @lc code=start
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tmp_len = 1
        while tmp_len < len(s):
            if len(s) % tmp_len != 0:
                tmp_len += 1
                continue
            for i in range(0, len(s), tmp_len):
                if s[:tmp_len] != s[i:i+tmp_len]:
                    break
            else:
                return True
            tmp_len += 1
        return False
# @lc code=end

