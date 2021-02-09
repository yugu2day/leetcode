#
# @lc app=leetcode.cn id=713 lang=python
#
# [713] 乘积小于K的子数组
#

# @lc code=start
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1: 
            return 0
        
        prod = 1
        ans, left = 0, 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans
        
# @lc code=end

