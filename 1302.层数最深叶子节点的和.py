#
# @lc app=leetcode.cn id=1302 lang=python
#
# [1302] 层数最深叶子节点的和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.deep = 0
        self.res = 0

        def dfs(node, depth):
            if not node:
                return 
            if depth == self.deep:
                self.res += node.val
            elif depth > self.deep:
                self.deep = depth
                self.res = node.val
            
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        
        dfs(root, 0)
        return self.res
# @lc code=end

