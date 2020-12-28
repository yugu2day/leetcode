#
# @lc app=leetcode.cn id=976 lang=python
#
# [976] 三角形的最大周长
#

# @lc code=start
class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        for i in range(len(A)-3, -1, -1):
            if A[i] + A[i+1] > A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0 
# @lc code=end

