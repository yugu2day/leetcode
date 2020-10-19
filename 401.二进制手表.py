#
# @lc app=leetcode.cn id=401 lang=python
#
# [401] 二进制手表
#

# @lc code=start
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        return ["{}:{:02d}".format(h,m) for h in range(0, 12) for m in range(0,60) if bin(h).count('1') + bin(m).count('1') == num]
        
# @lc code=end

