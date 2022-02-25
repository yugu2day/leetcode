#
# @lc app=leetcode.cn id=2119 lang=python
#
# [2119] 反转两次的数字
#

# @lc code=start
class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        reverse = self.reverse(num)
        return num == self.reverse(reverse)

    def reverse(self, num):
        res = 0
        while num:
            res = res * 10 + num % 10
            num = num // 10
        return res
        # @lc code=end

