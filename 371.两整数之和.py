#
# @lc app=leetcode.cn id=371 lang=python
#
# [371] 两整数之和
#

# @lc code=start
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        a &= 0xFFFFFFFF
        b &= 0xFFFFFFFF
        while b:
            carry = a & b
            a ^= b
            b = ((carry) << 1) & 0xFFFFFFFF
            # print((a, b))
        return a if a < 0x80000000 else ~(a^0xFFFFFFFF)

# @lc code=end

