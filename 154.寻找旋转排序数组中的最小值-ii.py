#
# @lc app=leetcode.cn id=154 lang=python
#
# [154] 寻找旋转排序数组中的最小值 II
#

# @lc code=start
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[mid] < nums[end]:
                end = mid - 1
            elif nums[mid] == nums[end]:
                end -= 1
            else:
                start = mid + 1
        return nums[start]
# @lc code=end

