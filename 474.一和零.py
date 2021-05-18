#
# @lc app=leetcode.cn id=474 lang=python
#
# [474] 一和零
#

# @lc code=start
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # dp[m][n] 表示最多 m个0 n个1的最大子集大小
        dp = [[0] * (n+1) for _ in range(m+1)]
        for s in strs:
            sm, sn = self.get_m_n(s)
            if sm > m or sn > n:
                continue

            for row in range(m, sm-1, -1):
                for col in range(n, sn-1, -1):
                    dp[row][col] = max(dp[row][col], 1+dp[row-sm][col-sn])
        
        return dp[m][n]

    def get_m_n(self, s):
        m, n = 0, 0
        for ch in s:
            if ch == "0":
                m+=1
            else:
                n+=1
        return m,n
# @lc code=end

