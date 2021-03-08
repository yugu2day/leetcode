#
# @lc app=leetcode.cn id=896 lang=python
#
# [896] 单调数列
#

# @lc code=start
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        
        if A[0] < A[-1]:
            flag = True
        else:
            flag = False

        for i in range(0, len(A) - 1):
            if flag:
                if A[i] <= A[i+1]:
                    continue
            else:
                if A[i] >= A[i+1]:
                    continue
            return False
        return True
# @lc code=end

