#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 字典保存{num: index}， 遍历判断target - num 是否在字典内
        dic = dict()
        for index, num in enumerate(nums):
            if target - num in dic:
                return [dic[target-num], index]
            dic[num] = index
        return []

# @lc code=end

