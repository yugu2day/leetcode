#
# @lc app=leetcode.cn id=507 lang=python
#
# [507] 完美数
#

# @lc code=start
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return False
        import math
        cnt = 1
        sqrt_num = int(math.sqrt(num))
        for i in range(2, sqrt_num+1):
            if num % i == 0:
                cnt += i + num // i if i * i != num else i
        return cnt == num
# @lc code=end

