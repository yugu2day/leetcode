#
# @lc app=leetcode.cn id=1035 lang=python
#
# [1035] 不相交的线
#

# @lc code=start
class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # 最长公共子序列dp[m][n]
        dp = [[0] * (len(nums2)+1) for _ in range(len(nums1)+1)]

        for i in range(1, len(nums1) + 1):
            num1 = nums1[i-1]
            for j in range(1, len(nums2)+1):
                num2 = nums2[j-1]
                if num1 == num2:
                    dp[i][j] = dp[i-1][j-1] + 1
                    continue
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
# @lc code=end

