#
# @lc app=leetcode.cn id=34 lang=python
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        total_len = len(nums)
        left = self.binaryLeftSearch(nums, target)
        if left == -1:
            return [-1, -1]

        right = self.binaryRightSearch(nums, target)
        return [left, right]

    def binaryLeftSearch(self, nums, target):
        # 获取最左边的idx
        res = -1
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                res = mid
                right = mid - 1

        return res

    def binaryRightSearch(self, nums, target):
        # 获取最右边的idx
        res = -1
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                res = mid
                left = mid + 1

        return res
# @lc code=end

