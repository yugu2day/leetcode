#
# @lc app=leetcode.cn id=313 lang=python
#
# [313] 超级丑数
#

# @lc code=start
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        dp = [0] * n
        dp[0] = 1
        times = [0] * len(primes)
        for i in range(1, len(dp)):
            m = min([dp[_] * primes[idx] for idx, _ in enumerate(times)])
            dp[i] = m
            for idx, j in enumerate(times):
                if dp[j] * primes[idx] == m:
                    times[idx] += 1
        return dp[-1]
# @lc code=end

