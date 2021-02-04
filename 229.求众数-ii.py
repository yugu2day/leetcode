#
# @lc app=leetcode.cn id=229 lang=python
#
# [229] 求众数 II
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n1, n2, c1, c2 = 0, 0, 0, 0

        for num in nums:
            
            if num == n1:
                c1 += 1
            elif num == n2:
                c2 += 1
            elif c1 <= 0:
                n1, c1 = num, 1
            elif c2 <= 0:
                n2, c2 = num, 1
            else:
                c1 -= 1
                c2 -= 1

        res = []
        n = len(nums) // 3
        if nums.count(n1) > n:
            res.append(n1)
        if n2 != n1 and nums.count(n2) > n:
            res.append(n2)
        return res
# @lc code=end

