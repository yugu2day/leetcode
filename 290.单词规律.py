#
# @lc app=leetcode.cn id=290 lang=python
#
# [290] 单词规律
#

# @lc code=start
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        pattern = list(pattern)
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        
        dic_p = dict()
        dic_s = dict()

        for i in range(0, len(pattern)):
            if pattern[i] in dic_p or s[i] in dic_s:
                if dic_s.get(s[i], "") != pattern[i] or dic_p.get(pattern[i], "") != s[i]:
                    return False
            else:
                dic_p[pattern[i]] = s[i]
                dic_s[s[i]] = pattern[i]
        return True
# @lc code=end

