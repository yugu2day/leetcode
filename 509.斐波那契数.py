#
# @lc app=leetcode.cn id=509 lang=python
#
# [509] 斐波那契数
#

# @lc code=start
class Solution(object):


    dic = dict()
    dic[0] = 0
    dic[1] = 1

    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        # dict 保存数据作缓存
        if N in self.dic:
            return self.dic[N]
        return self.fib(N-1) + self.fib(N-2)
        
# @lc code=end

