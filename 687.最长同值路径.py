#
# @lc app=leetcode.cn id=687 lang=python
#
# [687] 最长同值路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        def helper(node):
            # 返回 左边或右边 最长路径， 并将当前最长路径与左右路径和进行比较
            if not node:
                return 0
            if node.left:
                l = helper(node.left)
                if node.val == node.left.val:
                    left = l + 1 
                else:
                    left = 0
            else:
                left = 0

            if node.right:
                r = helper(node.right)
                if node.val == node.right.val:
                    right = r + 1 
                else:
                    right = 0
            else:
                right = 0
            self.res = max(self.res, left + right)
            return max(left, right)
        helper(root)
        return self.res
            
# @lc code=end

