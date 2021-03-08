#
# @lc app=leetcode.cn id=1089 lang=python
#
# [1089] 复写零
#

# @lc code=start
class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr) - 1:
            if arr[i] == 0:
                arr[i+1:] = [0] + arr[i+1:][:-1]
                i += 2
                continue
            i += 1
 
# @lc code=end

