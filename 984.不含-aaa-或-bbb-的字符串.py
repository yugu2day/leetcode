#
# @lc app=leetcode.cn id=984 lang=python
#
# [984] 不含 AAA 或 BBB 的字符串
#

# @lc code=start
class Solution(object):
    def strWithout3a3b(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: str
        """
        if a == b:
            return 'ab' * a
        res = ''
        if a > b:
            while a > b and b > 0:
                res += "aab"
                a -= 2
                b -= 1
            res += "ab" * a if b else "a" * a

        else:
            while b > a and a > 0:
                res += 'bba'
                b -= 2
                a -= 1
            res += 'ba' * b if a else "b" * b
        return res
# @lc code=end

