#
# @lc app=leetcode.cn id=405 lang=python
#
# [405] 数字转换为十六进制数
#

# @lc code=start
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        h = '0123456789abcdef'
        res = ''
        while num and len(res) < 8:
            res = h[num & 0xf] + res
            num = num >> 4
        return res
# @lc code=end

