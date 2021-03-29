#
# @lc app=leetcode.cn id=1385 lang=python
#
# [1385] 两个数组间的距离值
#

# @lc code=start
class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        res = 0
        for num1 in arr1:
            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    break
            else:
                res += 1
        return res
# @lc code=end

