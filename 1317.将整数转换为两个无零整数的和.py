#
# @lc app=leetcode.cn id=1317 lang=python
#
# [1317] 将整数转换为两个无零整数的和
#

# @lc code=start
class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        for i in range(1, n // 2+1):
            if '0' in str(i):
                continue
            if '0' in str(n-i):
                continue
            return [i, n-i]
# @lc code=end

