#
# @lc app=leetcode.cn id=124 lang=python
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 分别计算左边，右边路径上的最大和
        # 比较后加上当前节点的值，继续向上
        if not root:
            return 0

        self.m = float('-inf')  # 记录发生过的最大值

        def helper(node):
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)

            self.m = max(self.m, max(0, left) + max(0, right) + node.val)
            return node.val + max(left, right, 0)
        helper(root)
        return self.m
# @lc code=end
