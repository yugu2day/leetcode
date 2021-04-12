#
# @lc app=leetcode.cn id=838 lang=python
#
# [838] 推多米诺
#

# @lc code=start
class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        tmp = ""
        while tmp != dominoes:
            tmp = dominoes
            dominoes = dominoes.replace("R.L", "X")
            dominoes = dominoes.replace(".L", "LL")
            dominoes = dominoes.replace("R.", "RR")
            dominoes = dominoes.replace("X", "R.L")
        return dominoes
# @lc code=end

