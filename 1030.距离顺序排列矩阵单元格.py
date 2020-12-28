#
# @lc app=leetcode.cn id=1030 lang=python
#
# [1030] 距离顺序排列矩阵单元格
#

# @lc code=start
class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        import collections
        dic = collections.defaultdict(list)
        for row in range(0, R):
            for col in range(0, C):
                dic[abs(row - r0) + abs(col - c0)].append([row, col])
        
        res = []
        for distance in sorted(dic.keys()):
            res.extend(dic[distance])
        return res
# @lc code=end

