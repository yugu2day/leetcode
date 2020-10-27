#
# @lc app=leetcode.cn id=599 lang=python
#
# [599] 两个列表的最小索引总和
#

# @lc code=start
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dic1, dic2 = dict(), dict()
        for idx, name in enumerate(list1):
            dic1[name] = idx

        for idx, name in enumerate(list2):
            dic2[name] = idx
        
        res = []
        min_idx = float('inf')
        
        for k, v in dic1.items():
            if k not in dic2:
                continue
            if v + dic2[k] < min_idx:
                res = [k]
                min_idx = v + dic2[k]
            elif v + dic2[k] == min_idx:
                res += [k]
        return res
# @lc code=end

