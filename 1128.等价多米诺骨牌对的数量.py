#
# @lc app=leetcode.cn id=1128 lang=python
#
# [1128] 等价多米诺骨牌对的数量
#

# @lc code=start
class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        res = 0
        d = dict()
        for [i, j] in dominoes:
            t = "{}|{}".format(j, i) if j < i else "{}|{}".format(i, j)
            d[t] = d.get(t, 0) + 1

        for v in d.values():
            res += v * (v-1) / 2
        return res
# @lc code=end

