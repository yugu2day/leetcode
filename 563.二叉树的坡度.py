#
# @lc app=leetcode.cn id=563 lang=python
#
# [563] 二叉树的坡度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.res = 0
        def helper(node):
            # 获取节点的和
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            self.res += abs(left - right)
            return left + right + node.val
        helper(root)
        return self.res
        
# @lc code=end

