#
# @lc app=leetcode.cn id=53 lang=python
#
# [53] 最大子序和
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 维护临时变量，和小于0时从头算起
        if not nums:
            return 0

        tmp = nums[0]
        res = nums[0]
        for num in nums[1:]:

            if tmp + num< 0:
                tmp = num
            else:
                tmp = max(tmp + num, num)
            
            res = max(tmp, res)

        return max(res, tmp)

# @lc code=end

