#
# @lc app=leetcode.cn id=344 lang=python
#
# [344] 反转字符串
#

# @lc code=start
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        r = len(s) - 1
        l = 0

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        



# @lc code=end

