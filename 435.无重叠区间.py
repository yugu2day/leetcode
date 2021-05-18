#
# @lc app=leetcode.cn id=435 lang=python
#
# [435] 无重叠区间
#

# @lc code=start
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals = sorted(intervals, key=lambda x:(x[0], x[1]))
        # 动态规划 算最长无重叠区间，总长度相减
        dp = [1] * len(intervals)
        for i in range(1, len(intervals)):
            for j in range(0, i):
                if intervals[j][1] <= intervals[i][0]:
                    dp[i] = max(dp[i], dp[j]+1)

        return len(intervals) - max(dp)

# @lc code=end

