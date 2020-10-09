#
# @lc app=leetcode.cn id=367 lang=python
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False
        if num <= 1:
            return True
        l, r = 1, num // 2
        while l <= r:
            mid = (l + r) // 2
            if mid * mid == num:
                return True
            if mid * mid > num:
                r = mid - 1
            if mid * mid < num:
                l = mid + 1
        return False
# @lc code=end

