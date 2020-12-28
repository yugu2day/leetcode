#
# @lc app=leetcode.cn id=674 lang=python
#
# [674] 最长连续递增序列
#

# @lc code=start
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        tmp_len = 1
        res = 1
        for index in range(1, len(nums)):
            if nums[index] <= nums[index - 1]:
                tmp_len = 1
            else:
                tmp_len += 1
            res = max(tmp_len, res)
        return res
# @lc code=end

