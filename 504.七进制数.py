#
# @lc app=leetcode.cn id=504 lang=python
#
# [504] 七进制数
#

# @lc code=start
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return str(num)
        flag = True if num >= 0 else False
        res = ""
        num = abs(num)
        while num:
            res = str(num%7) + res
            num = num // 7
        return res if flag else '-' + res

# @lc code=end

