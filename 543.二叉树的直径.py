#
# @lc app=leetcode.cn id=543 lang=python
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        if not root:
            return 0
        
        def helper(node):
            # 获取到node的深度, 在获取的时候得到每个节点的直径进行对比
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            self.res = max(self.res, left + right)
            return max(left, right) + 1
        helper(root)
        return self.res
# @lc code=end

