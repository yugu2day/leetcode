#
# @lc app=leetcode.cn id=922 lang=python
#
# [922] 按奇偶排序数组 II
#

# @lc code=start
class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p1, p2 = 0, 1
        while p1 < len(nums) and p2 < len(nums):
            while p1 < len(nums) and nums[p1] % 2 == 0:
                p1 += 2
            while p2 < len(nums) and nums[p2] %2 != 0:
                p2 += 2
            if p1 < len(nums) and p2 < len(nums):
                nums[p1], nums[p2] = nums[p2], nums[p1]
        return nums
# @lc code=end

