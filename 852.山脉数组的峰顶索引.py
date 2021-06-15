#
# @lc app=leetcode.cn id=852 lang=python
#
# [852] 山脉数组的峰顶索引
#

# @lc code=start
class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) / 2
            if arr[mid] > arr[mid-1]:
                if arr[mid] > arr[mid+1]:
                    return mid
                else:
                    left = mid + 1
            else:
                right = mid - 1
        return left
# @lc code=end

