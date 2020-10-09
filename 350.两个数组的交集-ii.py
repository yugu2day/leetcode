#
# @lc app=leetcode.cn id=350 lang=python
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic_1, dic_2 = dict(), dict()
        for num in nums1:
            dic_1[num] = dic_1.get(num, 0) + 1
        
        for num in nums2:
            dic_2[num] = dic_2.get(num, 0) + 1
        
        res = []
        for k, v in dic_1.items():
            cnt = min(v, dic_2.get(k, 0))
            if cnt > 0:
                res += [k] * cnt
        return res
# @lc code=end

