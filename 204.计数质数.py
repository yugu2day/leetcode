#
# @lc app=leetcode.cn id=204 lang=python
#
# [204] 计数质数
#

# @lc code=start
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        arr = [True] * n
        arr[0] = False
        arr[1] = False
        res = 0

        for num in range(2, n):
            if arr[num]:
                res += 1
            tmp = 2
            while num * tmp < n:
                arr[num * tmp] = False
                tmp += 1
            
        # print(arr)
        return res


# @lc code=end

