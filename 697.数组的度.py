#
# @lc app=leetcode.cn id=697 lang=python
#
# [697] 数组的度
#

# @lc code=start
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = collections.defaultdict(list)
        max_degree = 0
        min_len = len(nums)
        for idx, num in enumerate(nums):
            dic[num].append(idx)
            max_degree = max(max_degree, len(dic[num]))
        
        for _, arrs in dic.items():
            if len(arrs) == max_degree:
                min_len = min(min_len, arrs[-1] - arrs[0] + 1)
        return min_len
# @lc code=end

