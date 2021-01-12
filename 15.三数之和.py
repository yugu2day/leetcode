#
# @lc app=leetcode.cn id=15 lang=python
#
# [15] 三数之和
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        
        nums.sort()
        res = []

        for index, num in enumerate(nums[:-2]):
            if num > 0:
                break
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            tmp_sum = abs(num)
            combinations = self.twoSum(tmp_sum, nums[index+1:])
            for cmb in combinations:
                res.append(list(cmb) + [num])
        return res
    

    def twoSum(self, target, nums):
        res = set()
        dic = dict()
        for index, num in enumerate(nums):

            if num in dic:
                if num < target - num:
                    res.add((num, target - num))
                else:
                    res.add((target - num, num))
            else:
                dic[target - num] = 1
        return list(res)
# @lc code=end

