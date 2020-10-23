#
# @lc app=leetcode.cn id=482 lang=python
#
# [482] 密钥格式化
#

# @lc code=start
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = [_ for _ in S if _ != '-']
        first_len = len(S) % K

        tmp_len = 0
        res = []

        if first_len > 0:
            res = [''.join(_.upper() for _ in S[:first_len])]
        for i in range(first_len, len(S), K):
            res.append(''.join(_.upper() for _ in S[i:i+K]))

        
        return '-'.join(res)
        
# @lc code=end

