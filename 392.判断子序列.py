#
# @lc app=leetcode.cn id=392 lang=python
#
# [392] 判断子序列
#

# @lc code=start
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 双指针，各自从头向尾遍历
        i1, i2 = 0, 0
        while i1 < len(s) and i2 < len(t):
            if s[i1] == t[i2]:
                i1 += 1
                i2 += 1 
            else:
                i2 += 1
        
        return i1 == len(s)

# @lc code=end

