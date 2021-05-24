#
# @lc app=leetcode.cn id=60 lang=python
#
# [60] 排列序列
#

# @lc code=start
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # 123..n 以1开头，后面n-1！种排列情况
        # k - (n-1)! 可以确定首位
        arr = [str(_) for _ in range(1, n+1)]
        res = self.getk(arr, k)
        return ''.join(res)

    def getk(self, arr, k):
        if len(arr) == 1 or k <= 1:
            return arr

        n = len(arr) - 1

        mul = 1
        for i in range(1, n+1):
            mul *= i

        idx = k / mul - 1 if k % mul  == 0 else k / mul
        return [arr[idx]] + self.getk(arr[:idx] + arr[idx+1:], k-mul*idx)
# @lc code=end

