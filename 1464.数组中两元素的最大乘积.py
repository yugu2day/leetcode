#
# @lc app=leetcode.cn id=1464 lang=python
#
# [1464] 数组中两元素的最大乘积
#

# @lc code=start
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        # return max((nums[-1]-1)*(nums[-2]-1), (nums[0]-1)*(nums[1]-1))
        return (nums[-1]-1)*(nums[-2]-1)
        
# @lc code=end

