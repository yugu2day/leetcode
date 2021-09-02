#
# @lc app=leetcode.cn id=275 lang=python
#
# [275] H 指数 II
#

# @lc code=start
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        start, end = 0, len(citations) - 1
        res = len(citations) - citations.count(0)
        while start <= end:

            mid = (start + end) // 2
            overP = len(citations) - mid # 引用次数大于等于timez的论文数
            if citations[mid] >= overP:
                res = overP
                end = mid - 1
            else:
                start = mid + 1
        return res
# @lc code=end

