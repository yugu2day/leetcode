#
# @lc app=leetcode.cn id=39 lang=python
#
# [39] 组合总和
#

# @lc code=start
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        def helper(tmp, target, candidates):

            if target == 0:
                res.append(tmp)
            for index, c in enumerate(candidates):
                if c <= target:
                    helper(tmp[:] + [c], target - c, candidates[index:])

        helper([], target, candidates)
        return res
# @lc code=end

