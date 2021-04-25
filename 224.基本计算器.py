#
# @lc app=leetcode.cn id=224 lang=python
#
# [224] 基本计算器
#

# @lc code=start
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbols = [1] # 记录括号外的符号情况，与实时符号进行判断负负得正
        sign = 1

        res = 0
        i = 0
        while i < len(s):

            if s[i] == ' ':
                i += 1
            elif s[i] == '+':
                sign = symbols[-1]
                i += 1
            elif s[i] == '-':
                sign = -symbols[-1]
                i += 1
            elif s[i] == '(':
                symbols.append(sign)
                i += 1
            elif s[i] == ')':
                symbols.pop()
                i += 1
            else:
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1

                res += num * sign
        return res
# @lc code=end

