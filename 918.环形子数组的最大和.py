#
# @lc app=leetcode.cn id=918 lang=python
#
# [918] 环形子数组的最大和
#

# @lc code=start
class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # 两种情况 连续的最大 分割的最大
        # 如果分割的最大，则找连续的最小
        s = sum(A)
        n1, n2 = A[0], A[0]
        r1, r2 = A[0], A[0]
        for num in A[1:]:
            if n1 + num > num:
                n1 = num + n1
                r1 = max(r1, n1)
            else:
                n1 = num
                r1 = max(n1, r1)
            
            if n2 + num < n2:
                n2 = min(num, n2+num)
                r2 = min(n2, r2)
            else:
                n2 = min(n2 + num, num)
                r2 = min(n2, r2)

        return max(r1, s-r2) if s != r2 else r1

# @lc code=end

