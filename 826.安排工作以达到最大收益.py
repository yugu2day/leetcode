#
# @lc app=leetcode.cn id=826 lang=python
#
# [826] 安排工作以达到最大收益
#

# @lc code=start
class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        d = zip(difficulty, profit)
        d = sorted(d, key=lambda x:x[0])

        worker.sort()
        cur_idx = 0  # 记录当前工人能干的工作index
        max_profit = 0 # 当前难度下最大的利益值
        res = 0

        for w in worker:
            while cur_idx < len(d) and d[cur_idx][0] <= w:
                max_profit = max(max_profit, d[cur_idx][1])
                cur_idx += 1
            res += max_profit

        return res
        
# @lc code=end

