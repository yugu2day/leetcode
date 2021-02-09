#
# @lc app=leetcode.cn id=724 lang=python
#
# [724] 寻找数组的中心索引
#

# @lc code=start
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        tmp = 0

        for idx, n in enumerate(nums):
            if tmp == (total_sum - n) / 2 and (total_sum - n) % 2 == 0:
                return idx
            tmp += n
        return -1

        
# @lc code=end

