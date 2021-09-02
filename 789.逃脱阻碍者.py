#
# @lc app=leetcode.cn id=789 lang=python
#
# [789] 逃脱阻碍者
#

# @lc code=start
class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        distance = abs(target[0]) + abs(target[1])
        for [x, y] in ghosts:
            if abs(x-target[0]) + abs(y-target[1]) <= distance:
                return False
        return True
# @lc code=end

