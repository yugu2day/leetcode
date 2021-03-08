#
# @lc app=leetcode.cn id=985 lang=python
#
# [985] 查询后的偶数和
#

# @lc code=start
class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        s = sum([num for num in A if num % 2 == 0])
        res = []
        for [a, idx] in queries:
            if (A[idx] + a) % 2 == 0:
                if A[idx] % 2 != 0:
                    s += A[idx] + a
                else:
                    s += a
            else:
                if A[idx] % 2 == 0:
                    s -= A[idx]
            A[idx] = A[idx] + a
            res.append(s)
        return res
        
# @lc code=end

