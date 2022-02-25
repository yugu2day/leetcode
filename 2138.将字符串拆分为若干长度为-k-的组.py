#
# @lc app=leetcode.cn id=2138 lang=python
#
# [2138] 将字符串拆分为若干长度为 k 的组
#

# @lc code=start
class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        res = []
        for idx in range(0 ,len(s), k):
            res.append(s[idx:idx+k])
        
        res[-1] += (k - len(res[-1])) * fill
        return res
# @lc code=end

