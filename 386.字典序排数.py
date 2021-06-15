#
# @lc app=leetcode.cn id=386 lang=python
#
# [386] 字典序排数
#

# @lc code=start
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        def helper(former):
            if former > n:
                return

            res.append(former)
            for i in range(0, 10):
                if former*10+i <= n:
                    helper(former*10+i)

        for i in range(1, 10):
            helper(i)
        return res
# @lc code=end

