#
# @lc app=leetcode.cn id=81 lang=python
#
# [81] 搜索旋转排序数组 II
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[start] == target or nums[end] == target or nums[mid] == target:
                return True
            
            while start < end and nums[start] == nums[end]:
                start += 1
                end -= 1

            if nums[start] == target or nums[end] == target or nums[mid] == target:
                return True
            
            if nums[mid] <= nums[end]:
                if target > nums[mid]:
                    if target > nums[end]:
                        end = mid - 1
                    else:
                        start = mid + 1
                else:
                    end = mid - 1
            
            else: # nums[mid] > nums[end]
                if target < nums[end]:
                    start = mid + 1
                else:
                    if target > nums[mid]:
                        start = mid + 1
                    else:
                        end = mid - 1

        return False
# @lc code=end

