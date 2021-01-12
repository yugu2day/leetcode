#
# @lc app=leetcode.cn id=4 lang=python
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        len1, len2 = len(nums1), len(nums2)
        half_len = (len1 + len2 + 1) // 2
        

        start, end = 0, len1
        while start <= end:
            mid1 = (start + end) // 2
            mid2 = half_len - mid1

            if mid1 > 0 and nums1[mid1 - 1] > nums2[mid2]:
                end = mid1 - 1 
            elif mid1 != len1 and nums1[mid1] < nums2[mid2-1]:
                start = mid1 + 1
            else:
                break

        if mid1 == 0:
            left = nums2[mid2 - 1]
        elif mid2 == 0:
            left = nums1[mid1 - 1]
        else:
            left = max(nums1[mid1-1], nums2[mid2-1]) 
        if (len1 + len2) % 2 == 1:
            return left

        if mid1 == len1:
            right = nums2[mid2]
        elif mid2 == len2:
            right = nums1[mid1]
        else:
            right = min(nums1[mid1], nums2[mid2])

        return (left + right) / 2.0
# @lc code=end

