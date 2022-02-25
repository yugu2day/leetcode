#
# @lc app=leetcode.cn id=2011 lang=python
#
# [2011] 执行操作后的变量值
#

# @lc code=start
class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        res = 0
        for op in operations:
            if op == '--X' or op == 'X--':
                res -= 1
            else:
                res += 1
        return res
# @lc code=end

