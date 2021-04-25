#
# @lc app=leetcode.cn id=1047 lang=python
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        for ch in S:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
# @lc code=end

