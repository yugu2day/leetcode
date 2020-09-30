#
# @lc app=leetcode.cn id=205 lang=python
#
# [205] 同构字符串
#

# @lc code=start
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic_s = dict()
        dic_t = dict()

        if len(s) != len(t):
            return False
        if s == t:
            return True
        
        for i in range(0, len(s)):
            if s[i] in dic_s or t[i] in dic_t:
                if t[i] != dic_s.get(s[i],"") or s[i] != dic_t.get(t[i], ""):
                    return False
            else:
                dic_s[s[i]] = t[i]
                dic_t[t[i]] = s[i]
        return True

                
        
# @lc code=end

