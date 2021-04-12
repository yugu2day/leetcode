#
# @lc app=leetcode.cn id=845 lang=python
#
# [845] 数组中的最长山脉
#

# @lc code=start
class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = 0
        for i in range(1, len(arr)-1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                left, right = i-1, i+1
                while left - 1 >= 0 and arr[left] > arr[left-1]:
                    left -= 1
                while right + 1 < len(arr) and arr[right] > arr[right+1]:
                    right += 1
                res = max(res, right - left + 1)
        return res
# @lc code=end

