#
# @lc app=leetcode.cn id=1200 lang=python
#
# [1200] 最小绝对差
#

# @lc code=start
class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        res = []
        min_gap = float('inf')

        for i in range(0, len(arr)-1):
            if arr[i+1] - arr[i] < min_gap:
                res = [arr[i], arr[i+1]]
            elif arr[i+1] - arr[i] == min_gap:
                res.append([arr[i], arr[i+1]])
        return res
# @lc code=end

