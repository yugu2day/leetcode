#
# @lc app=leetcode.cn id=172 lang=python
#
# [172] 阶乘后的零
#

# @lc code=start
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 分解 1 - n 的阶乘中 有多少个因子为5
        return sum([self.getN(_) for _ in range(1, n+1)])

    def getN(self, n):
        res = 0
        while n % 5 == 0:
            n = n//5
            res += 1
        return res
# @lc code=end

