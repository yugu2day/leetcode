#
# @lc app=leetcode.cn id=125 lang=python
#
# [125] 验证回文串
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = [upper(_) for _ in s if 48 <= ord(_)<=57 or 97<=ord(_)<=122 or 65<=ord(_)<=90]

        return s == s[::-1]
# @lc code=end

