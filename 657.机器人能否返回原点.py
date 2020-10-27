#
# @lc app=leetcode.cn id=657 lang=python
#
# [657] 机器人能否返回原点
#

# @lc code=start
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")
 # @lc code=end

