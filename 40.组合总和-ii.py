#
# @lc app=leetcode.cn id=40 lang=python
#
# [40] 组合总和 II
#

# @lc code=start
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        res = []
        def helper(tmp, target, candidates):
            
            if target == 0:
                res.append(tmp)
            for index, num in enumerate(candidates):
                if num > target :
                    continue
                if index > 0 and candidates[index] == candidates[index - 1]:
                    continue
                helper(tmp[:] + [num], target - num, candidates[index+1:])

        helper([], target, candidates)
        return res
# @lc code=end

