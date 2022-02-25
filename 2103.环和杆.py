#
# @lc app=leetcode.cn id=2103 lang=python
#
# [2103] 环和杆
#

# @lc code=start
class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        dic = collections.defaultdict(set)
        for i in range(0, len(rings), 2):
            dic[rings[i+1]].add(rings[i])

        res = 0
        for k, v in dic.items():
            if len(v) == 3:
                res += 1
        return res
# @lc code=end

