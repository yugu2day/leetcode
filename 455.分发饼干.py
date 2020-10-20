#
# @lc app=leetcode.cn id=455 lang=python
#
# [455] 分发饼干
#

# @lc code=start
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # 双指针
        res = 0
        gi, si = 0, 0
        g.sort()
        s.sort()
        while gi < len(g) and si < len(s):
            if g[gi] <= s[si]:
                res += 1
                gi += 1
            si += 1
        return res
# @lc code=end

