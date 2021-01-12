#
# @lc app=leetcode.cn id=16 lang=python
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = float('inf')

        for index, num in enumerate(nums):
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            j, k = index + 1, len(nums) - 1
            while j < k:
                tmp_sum = num + nums[j] + nums[k]
                if abs(tmp_sum - target) < abs(res - target):
                    res = tmp_sum
                if tmp_sum > target:
                    k -= 1
                elif tmp_sum < target:
                    j += 1
                else:
                    return target
        return res
# @lc code=end

