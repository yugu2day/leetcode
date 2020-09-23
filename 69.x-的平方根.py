#
# @lc app=leetcode.cn id=69 lang=python
#
# [69] x 的平方根
#

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        res = -1
        start, end = 1, x // 2
        while start <= end:
            # print(start, end)
            mid = (start+end) // 2
            if mid * mid <= x:
                res = mid
                start = mid + 1
            else:
                end = mid - 1
        return res
# @lc code=end

