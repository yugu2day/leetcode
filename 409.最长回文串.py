#
# @lc app=leetcode.cn id=409 lang=python
#
# [409] 最长回文串
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = dict()
        for ch in s:
            dic[ch] = dic.get(ch, 0) + 1

        res = 0
        flag = False
        for _, v in dic.items():
            if v % 2 == 0:
                res += v
            else:
                res += v - 1
                flag = True

        return res + 1 if flag else res

# @lc code=end

