#
# @lc app=leetcode.cn id=342 lang=python
#
# [342] 4的幂
#

# @lc code=start
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        while num % 4 == 0:
            num = num // 4
        return num == 1
        
# @lc code=end

