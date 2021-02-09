#
# @lc app=leetcode.cn id=454 lang=python
#
# [454] 四数相加 II
#

# @lc code=start
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        dic = dict()
        for a in A:
            for b in B:
                dic[a+b] = dic.get(a+b, 0) + 1
        
        res = 0
        for c in C:
            for d in D:
                if -c-d in dic:
                    res += dic[-c-d]
        return res
# @lc code=end

