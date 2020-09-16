#
# @lc app=leetcode.cn id=9 lang=python
#
# [9] 回文数
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 负数没有回文数，正数转字符串之后进行比较
        if x < 0:
            return False
        return str(x) == str(x)[::-1]
# @lc code=end

