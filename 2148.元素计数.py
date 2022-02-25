#
# @lc app=leetcode.cn id=2148 lang=python
#
# [2148] 元素计数
#

# @lc code=start
class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_num = min(nums)
        max_num = max(nums)
        if min_num == max_num:
            return 0
        return len(nums) - (nums.count(min(nums)) + nums.count(max(nums)))
# @lc code=end

