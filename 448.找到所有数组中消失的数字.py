#
# @lc app=leetcode.cn id=448 lang=python
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = list()
        for num in nums:
            nums[abs(num) - 1] = - abs(nums[abs(num) - 1])

        for index, num in enumerate(nums):
            if num > 0:
                res.append(index + 1)
        return res
        

# @lc code=end

