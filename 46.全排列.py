#
# @lc app=leetcode.cn id=46 lang=python
#
# [46] 全排列
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(pos):
            if pos == len(nums):
                self.res.append(nums[:])
            
            for i in range(pos, len(nums)):
                nums[i], nums[pos] = nums[pos], nums[i]
                dfs(pos+1)
                nums[i], nums[pos] = nums[pos], nums[i]
        self.res = []
        dfs(0)
        return self.res
# @lc code=end

