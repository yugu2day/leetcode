#
# @lc app=leetcode.cn id=7 lang=python
#
# [7] 整数反转
#

# @lc code=start
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 判断正负， 临时变量交换值后返回对应符号的数
        if x == 0:
            return 0
        flag = True if x > 0 else False
        
        x = abs(x)
        tmp = 0
        while x:
            tmp = tmp * 10 + x % 10
            x = x // 10
        
        if tmp > pow(2, 31) - 1 or tmp < -pow(2, 31):
            return 0

        return tmp if flag else -tmp
# @lc code=end

