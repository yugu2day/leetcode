#
# @lc app=leetcode.cn id=1800 lang=python
#
# [1800] 最大升序子数组和
#

# @lc code=start
class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 维护当前连续递增子序列的和，有不符合条件的重新开始计算
        tmp = 0
        res = 0
        for idx, num in enumerate(nums):
            if idx == 0 or num > nums[idx-1]:
                tmp += num
                res = max(res, tmp)
            else:
                tmp = num
        return res
# @lc code=end

