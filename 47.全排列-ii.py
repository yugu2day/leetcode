#
# @lc app=leetcode.cn id=47 lang=python
#
# [47] 全排列 II
#

# @lc code=start
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        def helper(nums, tmp):
            if not nums:
                res.append(tmp)
                return
                
            for index in range(0, len(nums)):
                if index > 0 and nums[index] == nums[index-1]:
                    continue
                helper(nums[:index] + nums[index+1:], tmp+[nums[index]])
                        
        helper(nums, [])
        return res    
# @lc code=end

