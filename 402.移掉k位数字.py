#
# @lc app=leetcode.cn id=402 lang=python
#
# [402] 移掉K位数字
#

# @lc code=start
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) == k:
            return "0"

        stack = []

        for ch in num:
            while stack :
                if k > 0 and stack[-1] > ch:
                    stack.pop()
                    k -= 1
                else:
                    break
            stack.append(ch)

        while stack and stack[0] == "0":
            stack = stack[1:]
        stack = stack[:len(stack)-k]

        return ''.join(stack) if stack else "0"
                
# @lc code=end

