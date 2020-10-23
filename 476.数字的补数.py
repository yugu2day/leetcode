#
# @lc app=leetcode.cn id=476 lang=python
#
# [476] 数字的补数
#

# @lc code=start
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        tmp = num
        target = 1
        while tmp:
            target = target << 1 
            tmp = tmp >> 1
        target = target - 1

        return num ^ target
# @lc code=end

