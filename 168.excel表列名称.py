#
# @lc app=leetcode.cn id=168 lang=python
#
# [168] Excel表列名称
#

# @lc code=start
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ""
        while n >= 26:
            if n % 26 == 0:
                res = 'Z' + res
                n = n // 26 - 1
            else:
                res = chr(n % 26 + 64) + res
                n = n // 26
        
        if n != 26 and n > 0: 
            res = chr(n % 26 + 64) + res
        return res
# @lc code=end

