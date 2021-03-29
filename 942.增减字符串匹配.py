#
# @lc app=leetcode.cn id=942 lang=python
#
# [942] 增减字符串匹配
#

# @lc code=start
class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        i1, i2 = 0, len(S)
        res = []
        
        for i in range(0, len(S)):
            if S[i] == 'I':
                res.append(i1)
                i1 += 1
            else:
                res.append(i2)
                i2 -= 1

        if S[i] == 'I':
            res.append(i1)
        else:
           res.append(i2)
        return res

# @lc code=end

