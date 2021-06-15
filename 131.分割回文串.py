#
# @lc app=leetcode.cn id=131 lang=python
#
# [131] 分割回文串
#

# @lc code=start
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        def helper(cur, s):
            if not s:
                res.append(cur)
                return
            for i in range(1, len(s)+1):
                if s[:i] == s[:i][::-1]:
                    tmp = cur + [s[:i]]
                    helper(tmp, s[i:])
            return
        helper([], s)
        return res
            
# @lc code=end

