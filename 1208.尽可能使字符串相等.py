#
# @lc app=leetcode.cn id=1208 lang=python
#
# [1208] 尽可能使字符串相等
#

# @lc code=start
class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        left, right = 0, 0
        tmp = 0
        res = 0

        while right < len(s):
            if s[right] != t[right]:
                tmp += abs(ord(s[right]) - ord(t[right]))
            
            while left < len(s) and tmp > maxCost:
                if s[left] != t[left]:
                    tmp -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            
            if tmp <= maxCost:
                res = max(res, right-left+1)
            right += 1
        return res
# @lc code=end

