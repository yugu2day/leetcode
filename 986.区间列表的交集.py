#
# @lc app=leetcode.cn id=986 lang=python
#
# [986] 区间列表的交集
#

# @lc code=start
class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for first in firstList:
            f1, f2 = first[0], first[1]
            for second in secondList:
                s1, s2 = second[0], second[1]
                if f1 > s2:
                    continue
                if f2 < s1:
                    break
                if f1 <= s2 and f2 >= s1:
                    res.append([max(f1, s1), min(f2, s2)])
        return res
# @lc code=end

