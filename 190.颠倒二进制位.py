#
# @lc app=leetcode.cn id=190 lang=python
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        b = 0
        for _ in range(31):
            b = b | (n & 1)
            b = b << 1
            n = n >> 1
        b = b | (n & 1)
        return b
# @lc code=end

