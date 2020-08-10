#
# @lc app=leetcode.cn id=222 lang=python
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 递归
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)



        
# @lc code=end

