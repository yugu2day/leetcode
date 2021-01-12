#
# @lc app=leetcode.cn id=33 lang=python
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start ,end = 0 ,len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[start] == target:
                return start
            if nums[end] == target:
                return end

            if nums[mid] > nums[end]:
                if target > nums[mid]:
                    start = mid + 1
                else:
                    if target < nums[mid]:
                        if target < nums[end]:
                            start = mid + 1
                        else:
                            end = mid - 1
            else:
                if target < nums[mid]:
                    end = mid - 1
                else:
                    if target > nums[end]:
                        end = mid - 1
                    else:
                        start = mid + 1
        return -1
# @lc code=end

