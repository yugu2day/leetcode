#
# @lc app=leetcode.cn id=1389 lang=python
#
# [1389] 按既定顺序创建目标数组
#

# @lc code=start
class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        target = []
        while nums:
            target.insert(index[0], nums[0])
            nums.pop(0)
            index.pop(0)
        return target# @lc code=end

