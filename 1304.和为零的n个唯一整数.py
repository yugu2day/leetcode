#
# @lc app=leetcode.cn id=1304 lang=python
#
# [1304] 和为零的N个唯一整数
#

# @lc code=start
class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [] if n % 2 == 0 else[0]
    
        for i in range(1, n//2+1):
            res.append(-i)
            res.append(i)
        return res
        
# @lc code=end

