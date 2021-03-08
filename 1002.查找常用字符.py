#
# @lc app=leetcode.cn id=1002 lang=python
#
# [1002] 查找常用字符
#

# @lc code=start
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        res = []
        for ch in range(97, 123):
            appear = float('inf')
            for word in A:
                cnt = word.count(chr(ch))
                if cnt == 0:
                    appear = 0
                    break
                appear = min(appear, cnt)
            res += [chr(ch)] * appear
        return res


        
# @lc code=end

