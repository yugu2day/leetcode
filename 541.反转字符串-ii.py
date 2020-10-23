#
# @lc app=leetcode.cn id=541 lang=python
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        last_len = len(s) % (2*k)
        res = ""
        for i in range(0, len(s)-last_len, 2*k):
            res += s[i:i+k][::-1] + s[i+k:i+2*k]

        if last_len >= k:
            res += s[len(s)-last_len:len(s)-last_len+k][::-1]
            res += s[len(s)-last_len+k:]
        else:
            res += s[len(s)-last_len:len(s)-last_len+k][::-1]
        return res

# @lc code=end

