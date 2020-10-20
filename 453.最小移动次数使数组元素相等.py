#
# @lc app=leetcode.cn id=453 lang=python
#
# [453] 最小移动次数使数组元素相等
#

# @lc code=start
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 相当于每次对1个数减1， 到所有数等于最小数
        return sum(nums) - min(nums) * len(nums)
# @lc code=end

