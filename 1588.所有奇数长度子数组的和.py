#
# @lc app=leetcode.cn id=1588 lang=python
#
# [1588] 所有奇数长度子数组的和
#

# @lc code=start
class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = 0
        lyst = [0]
        for num in arr:
            lyst.append(lyst[-1] + num)

        for i in range(1, len(lyst)):
            for sub in range(i-1, -1, -2):
                res += lyst[i] - lyst[sub]
        return res
# @lc code=end

