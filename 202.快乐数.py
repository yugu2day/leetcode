#
# @lc app=leetcode.cn id=202 lang=python
#
# [202] 快乐数
#

# @lc code=start
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()
        while n != 1:
            tmp = 0
            while n:
                tmp = tmp + (n%10) * (n%10)
                n = n // 10
            if tmp in visited:
                return False
            else:
                visited.add(tmp)
            n = tmp
        return True
# @lc code=end

