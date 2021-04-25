#
# @lc app=leetcode.cn id=71 lang=python
#
# [71] 简化路径
#

# @lc code=start
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split("/")
        stack = []

        for p in path:
            if p == '.':
                continue
            elif p == '..':
                if stack:
                    stack.pop()
            elif not p:
                continue
            else:
                stack.append(p)
        return '/' + '/'.join(stack)
# @lc code=end

