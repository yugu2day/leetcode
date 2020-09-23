#
# @lc app=leetcode.cn id=88 lang=python
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        idx = (m + n) - 1
        m -= 1
        n -= 1
        while m >= 0 or n >= 0:

            if m < 0:
                nums1[idx] = nums2[n]
                idx -= 1
                n -= 1
                continue
            if n < 0:
                nums1[idx] = nums1[m]
                idx -= 1
                m -= 1
                continue
            
            if nums1[m] < nums2[n]:
                nums1[idx] = nums2[n]
                n -= 1
            else:
                nums1[idx] = nums1[m]
                m -= 1
            idx -= 1


# @lc code=end

