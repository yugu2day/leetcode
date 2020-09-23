#
# @lc app=leetcode.cn id=67 lang=python
#
# [67] 二进制求和
#

# @lc code=start
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a, b = int(a, 2), int(b,2)
        while b != 0:
            a, b = a^b, (a&b) << 1
        return bin(a)[2:]
        
# @lc code=end

