#
# @lc app=leetcode.cn id=993 lang=python
#
# [993] 二叉树的堂兄弟节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        depth = 0

        def search(root, node, depth):
            if not root:
                return None, 0
            if root.val == node:
                return root, 0
            if root.left and root.left.val == node:
                return root, depth
            if root.right and root.right.val == node:
                return root, depth
            p, d = search(root.left, node, depth+1)
            if p:
                return p, d
            return search(root.right, node, depth+1)
        
        f1, d1 = search(root, x, 0)
        f2, d2 = search(root, y, 0) 
        return f1 != f2 and d1 == d2
        
# @lc code=end

