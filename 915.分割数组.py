#
# @lc app=leetcode.cn id=915 lang=python
#
# [915] 分割数组
#

# @lc code=start
class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # 从右到左遍历一次，维护最小栈
        stack = []
        for num in A[::-1]:
            if not stack or num <= stack[-1]:
                stack.append(num)
        
        max_num = A[0]
        for index, num in enumerate(A):
            # 为最小栈中的值时，最小栈推出
            if num == stack[-1]:
                stack.pop()
            # 比较左边最大值与最小栈的比较
            max_num = max(num, max_num)
            if max_num <= stack[-1]:
                return index + 1
        return len(A)
        
# @lc code=end

