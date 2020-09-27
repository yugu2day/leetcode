#
# @lc app=leetcode.cn id=167 lang=python
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        a, b = 0, len(numbers) - 1
        while a < b:
            tmp = numbers[a] + numbers[b]
            if tmp == target:
                return [a+1,b+1]
            elif tmp < target:
                a += 1
            elif tmp > target:
                b -= 1
        return [-1,-1]
# @lc code=end

