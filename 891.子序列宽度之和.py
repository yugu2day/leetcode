#
# @lc app=leetcode.cn id=891 lang=python
#
# [891] 子序列宽度之和
#

# @lc code=start
class Solution(object):
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        sums=0
        for i in range(len(A)):
            sums+=(pow(2,i,1000000007)-pow(2,len(A)-1-i,1000000007))*A[i]
        return sums%1000000007
# @lc code=end

