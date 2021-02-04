#
# @lc app=leetcode.cn id=216 lang=python
#
# [216] 组合总和 III
#

# @lc code=start
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []

        def helper(tmp, arr):
            if tmp == n and len(arr) == k:
                res.append(arr)
            for i in range(arr[-1]+1, 10):
                if tmp + i <= n:
                    new_arr = arr[:] + [i]
                    bfs(tmp + i, new_arr)
        
        for i in range(1, 9):
            helper(i, [i])
        return res
# @lc code=end

