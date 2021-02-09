#
# @lc app=leetcode.cn id=532 lang=python
#
# [532] 数组中的 k-diff 数对
#

# @lc code=start
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = dict()
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        res = 0
        for num in set(nums):
            if num - k in dic:
                if num - k == num:
                    if dic[num] > 1:
                        res += 1
                else:
                    res += 1
        return res
# @lc code=end

