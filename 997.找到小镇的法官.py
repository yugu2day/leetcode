#
# @lc app=leetcode.cn id=997 lang=python
#
# [997] 找到小镇的法官
#

# @lc code=start
class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if n == 1:
            return 1
        d = collections.defaultdict(list) # 相信k 的人
        e = collections.defaultdict(list) # k 相信的人
        for [a, b] in trust:
            d[b].append(a)
            e[a].append(b)
        for p, c in d.items():
            if len(c) == n-1 and len(e[p]) == 0:
                return p
        return -1
# @lc code=end

