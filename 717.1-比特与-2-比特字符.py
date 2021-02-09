#
# @lc app=leetcode.cn id=717 lang=python
#
# [717] 1比特与2比特字符
#

# @lc code=start
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if bits == [0]:
            return True
        elif len(bits) < 2:
            return False
            
        if bits[0] == 0:
            return self.isOneBitCharacter(bits[1:])
        else:
            return self.isOneBitCharacter(bits[2:])
        
# @lc code=end

