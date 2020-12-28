#
# @lc app=leetcode.cn id=682 lang=python
#
# [682] 棒球比赛
#

# @lc code=start
class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        s = []
        for o in ops:
            if o == "+":
                s.append(s[-1] + s[-2])
            elif o == "D":
                s.append(s[-1] * 2)
            elif o == "C":
                s.pop()
            else:
                s.append(int(o))
        return sum(s)
# @lc code=end

