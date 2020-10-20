#
# @lc app=leetcode.cn id=447 lang=python
#
# [447] 回旋镖的数量
#

# @lc code=start
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res=0
        for i in points:
            dicts={}
            for j in points:
                if i==j:
                    continue
                dicts[(i[0]-j[0])**2+(i[1]-j[1])**2]=dicts.get((i[0]-j[0])**2+(i[1]-j[1])**2,0)+1
            for i in dicts.values():
                res+=i*(i-1)
        return res

        
# @lc code=end

