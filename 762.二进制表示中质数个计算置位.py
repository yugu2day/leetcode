#
# @lc app=leetcode.cn id=762 lang=python
#
# [762] 二进制表示中质数个计算置位
#

# @lc code=start
class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        primes = {2, 3, 5, 7, 11, 13, 17, 19} 
        return sum([1 for num in range(L,R+1) if bin(num).count('1') in primes ])
# @lc code=end

