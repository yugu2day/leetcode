#
# @lc app=leetcode.cn id=2161 lang=python
#
# [2161] 根据给定数字划分数组
#

# @lc code=start
class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        less, more = [], []
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                more.append(num)
        return less + [pivot] * (len(nums)-len(less)-len(more)) + more
# @lc code=end

