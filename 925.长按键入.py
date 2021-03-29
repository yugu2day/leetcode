#
# @lc app=leetcode.cn id=925 lang=python
#
# [925] 长按键入
#

# @lc code=start
class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if len(name) > len(typed):
            return False
        if name == typed:
            return True

        i1, i2 = 0, 0
        while i1<len(name) and i2<len(typed):
            if name[i1] != typed[i2]:
                return False
            tmp = name[i1]
            c1, c2 = 0, 0

            while i1<len(name) and name[i1] == tmp:
                c1 += 1
                i1 += 1
            while i2<len(typed) and typed[i2] == tmp:
                c2 += 1 
                i2 += 1
            
            if c2 < c1:
                return False
        return i1 == len(name) and i2 == len(typed)
# @lc code=end

