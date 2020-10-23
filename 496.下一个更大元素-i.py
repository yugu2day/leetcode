#
# @lc app=leetcode.cn id=496 lang=python
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = dict()
        for i in range(0 ,len(nums2)):
            for j in range(i+1, len(nums2)):
                if nums2[j] > nums2[i]:
                    dic[nums2[i]] = nums2[j]
                    break
            else:
                dic[nums2[i]] = -1
        
        return [dic[num] for num in nums1]
# @lc code=end

