#
# @lc app=leetcode.cn id=278 lang=python
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n
        res = 1
        while start <= end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                res = mid
                end = mid - 1
            else:
                start = mid + 1
        return res
# @lc code=end

