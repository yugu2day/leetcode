#
# @lc app=leetcode.cn id=462 lang=python
#
# [462] 最少移动次数使数组元素相等 II
#

# @lc code=start
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        left, right = 0, len(nums) - 1
        res = 0
        while left < right:
            # 中位数为p
            # 位数等于 p - l + r - p = 右边点 - 左边点
            res += nums[right] - nums[left]
            left += 1
            right -= 1
        return res
            
# @lc code=end

