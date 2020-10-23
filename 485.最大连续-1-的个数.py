#
# @lc app=leetcode.cn id=485 lang=python
#
# [485] 最大连续1的个数
#

# @lc code=start
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = ''
        for n in nums:
            s += str(n)
        s = s.split('0')
        return max([len(_) for _ in s])
# @lc code=end

