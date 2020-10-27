#
# @lc app=leetcode.cn id=643 lang=python
#
# [643] 子数组最大平均数 I
#

# @lc code=start
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # 滑动窗口
        tmp = sum(nums[:k])
        max_val = tmp
        for i in range(k, len(nums)):
            tmp = tmp + nums[i] - nums[i-k]
            max_val = max(max_val, tmp)
        return (max_val * 1.0) / k
# @lc code=end

