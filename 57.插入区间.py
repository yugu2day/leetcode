#
# @lc app=leetcode.cn id=57 lang=python
#
# [57] 插入区间
#

# @lc code=start
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        arr2 = []
        left, right = newInterval[0], newInterval[1]
        # 拿出所有和新区间重叠的区间
        for interval in intervals:
            if interval[1] >= newInterval[0] and interval[0] <= newInterval[1]:
                left = min(left, interval[0])
                right = max(right, interval[1])

            else:
                arr2.append(interval)

        arr2.append([left, right])
        arr2.sort(key=lambda x:(x[0],x[1]))
        
        return arr2
# @lc code=end

