#
# @lc app=leetcode.cn id=56 lang=python
#
# [56] 合并区间
#

# @lc code=start
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) <= 1:
            return intervals
        
        intervals.sort(key = lambda x:(x[0], x[1]))
        res = [intervals[0]]
        for interval in intervals[1:]:
            if res[-1][1] >= interval[0]: 
                res[-1] = [res[-1][0], max(res[-1][1], interval[1])]
            else:
                res.append(interval)
        return res
# @lc code=end

