#
# @lc app=leetcode.cn id=1093 lang=python
#
# [1093] 大样本统计
#

# @lc code=start
class Solution(object):
    def sampleStats(self, count):
        """
        :type count: List[int]
        :rtype: List[float]
        """
        res = [None, float(0), float(0), float(0), float(0)]
        total = float(0)
        max_idx = 0
        max_cnt = 0

        total_cnt = sum(count)

        # total_cnt/2 -1, total_cnt/2
        t1, t2 = total_cnt/2, total_cnt/2+1
        m1, m2 = float(0), float(0)

        for idx, n in enumerate(count):
            if res[0] is None and n != 0:
                res[0] = idx
            if n != 0:
                res[1] = idx
                total += idx * n
            if n > max_cnt:
                max_idx = idx
                max_cnt = n
            
            if t1 > 0:
                if t1 - n <= 0:
                    m1 = idx
                t1 -= n
            if t2 > 0:
                if t2 - n <= 0:
                    m2 = idx
                t2 -= n
            

        res[2] = total / total_cnt
        res[4] = max_idx

        if total_cnt % 2 == 0:
            res[3] = (m1 + m2) / 2.0
        else:
            res[3] = m2
        

        return res
# @lc code=end

