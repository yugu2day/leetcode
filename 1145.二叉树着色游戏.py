#
# @lc app=leetcode.cn id=1145 lang=python
#
# [1145] 二叉树着色游戏
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        """
        self.red_left, self.red_right = 0, 0
        self.x = x


        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            if node.val == self.x:
                self.red_left = l
                self.red_right = r
            return l + r + 1
        
        # 计算x点将树分成的3部分，最大的一部分如果占据一半以上的点即可胜利
        total = dfs(root)
        if (total - self.red_left - self.red_right - 1) * 2 > total:
            return True
        
        if self.red_left * 2 > total or self.red_right * 2 > total:
            return True
        return False
        
# @lc code=end

