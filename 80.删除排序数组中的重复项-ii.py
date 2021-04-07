#
# @lc app=leetcode.cn id=80 lang=python
#
# [80] 删除排序数组中的重复项 II
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = 0, 0
        while fast < len(nums):
            if slow < 2:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
                continue
            if fast < len(nums) and nums[fast] == nums[slow-2]:
                fast += 1
            else:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1

        return slow
# @lc code=end

