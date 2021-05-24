#
# @lc app=leetcode.cn id=77 lang=python
#
# [77] 组合
#

# @lc code=start
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        arr = [_ for _ in range(1, n+1)]
        res = []

        def helper(tmp, pos):
            if len(tmp) == k:
                res.append(tmp)        
                return

            for i in range(pos, len(arr)):
                helper(tmp[:]+[arr[i]], i+1)
        
        helper([], 0)
        return res
# @lc code=end

