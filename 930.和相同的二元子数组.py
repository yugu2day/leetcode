#
# @lc app=leetcode.cn id=930 lang=python
#
# [930] 和相同的二元子数组
#

# @lc code=start
class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        t = 0
        res = 0
        s = collections.defaultdict(int)

        for n in A:
            t += n

            if t == S:
                res += 1

            if t - S in s:
                res += s[t-S]

            s[t] += 1
        return res
        
# @lc code=end

