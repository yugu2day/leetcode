#
# @lc app=leetcode.cn id=90 lang=python
#
# [90] 子集 II
#

# @lc code=start
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        visited = set()

        for idx, num in enumerate(nums):

            tmp = res[:]

            for sub in res:
                sub = sub + [num]
                if tuple(sorted(sub)) in visited:
                    continue
                visited.add(tuple(sorted(sub)))
                tmp.append(sub)

            res = tmp

        return res
# @lc code=end

