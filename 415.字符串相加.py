#
# @lc app=leetcode.cn id=415 lang=python
#
# [415] 字符串相加
#

# @lc code=start
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = num1[::-1], num2[::-1]
        res = ""
        tmp = 0
        for i in range(0, max(len(num1), len(num2))):

            n1 = 0 if i >= len(num1) else int(num1[i])
            n2 = 0 if i >= len(num2) else int(num2[i]) 
            
            n = n1 + n2 + tmp
            res += str(n % 10)
            tmp = n // 10
        return str(tmp) + res[::-1] if tmp !=0 else res[::-1]

# @lc code=end

