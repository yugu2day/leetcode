#
# @lc app=leetcode.cn id=645 lang=python
#
# [645] 错误的集合
#

# @lc code=start
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        set_sum = sum(set(nums))
        n = len(nums)
        return [sum(nums) - set_sum, (1 + n) * n //2 - set_sum]
# @lc code=end

