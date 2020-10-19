#
# @lc app=leetcode.cn id=414 lang=python
#
# [414] 第三大的数
#

# @lc code=start
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return max(nums)

        a, b, c = float('-inf'), float('-inf'), float('-inf')

        for num in nums:
            if num > a:
                a, b, c = num, a, b
                continue
            if num > b and num != a:
                b, c = num, b
                continue
            if num > c and num != a and num != b:
                c = num
                continue

        return c if c != float('-inf') else a
# @lc code=end

