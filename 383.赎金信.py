#
# @lc app=leetcode.cn id=383 lang=python
#
# [383] 赎金信
#

# @lc code=start
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dic_r, dic_m = dict(), dict()
        for ch in ransomNote:
            dic_r[ch] = dic_r.get(ch, 0) + 1
        for ch in magazine:
            dic_m[ch] = dic_m.get(ch, 0) + 1
        
        for k, v in dic_r.items():
            if v > dic_m.get(k, 0):
                return False
        return True
# @lc code=end

