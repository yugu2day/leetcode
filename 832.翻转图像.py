#
# @lc app=leetcode.cn id=832 lang=python
#
# [832] 翻转图像
#

# @lc code=start
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """        
        A = [row[::-1] for row in A]
        for idx, row in enumerate(A):
            A[idx] = [abs(item - 1) for item in row]
        return A
        
# @lc code=end

