#
# @lc app=leetcode.cn id=594 lang=python
#
# [594] 最长和谐子序列
#

# @lc code=start
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = dict()
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        
        res = 0
        for (k, v) in dic.items():
            if dic.get(k-1, 0) != 0:
                res = max(res, dic.get(k-1, 0) + v)
            if dic.get(k+1, 0) != 0:
                res = max(res, dic.get(k+1, 0) + v)

        return res
# @lc code=end

