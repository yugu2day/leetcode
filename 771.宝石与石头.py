#
# @lc app=leetcode.cn id=771 lang=python
#
# [771] 宝石与石头
#

# @lc code=start
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        res = 0
        jewels = set(jewels)
        for s in stones:
            if s in jewels:
                res += 1
        return res
# @lc code=end

