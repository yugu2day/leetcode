#
# @lc app=leetcode.cn id=1295 lang=python
#
# [1295] 统计位数为偶数的数字
#

# @lc code=start
class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum([1 for n in nums if len(str(n))%2==0])
# @lc code=end

