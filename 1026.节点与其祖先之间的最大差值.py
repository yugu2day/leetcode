#
# @lc app=leetcode.cn id=1026 lang=python
#
# [1026] 节点与其祖先之间的最大差值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        def dfs(node):
            if not node:
                return -1, -1
            
            left_min, left_max = dfs(node.left)
            if left_min == -1 and left_max == -1:
                left_min = node.val
                left_max = node.val
            
            right_min, right_max = dfs(node.right)
            if right_min == -1 and right_max == -1:
                right_min = node.val
                right_max = node.val

            self.res = max(self.res, abs(left_min-node.val), abs(left_max-node.val), abs(right_min-node.val), abs(right_max-node.val))
            return min(node.val, left_min, right_min), max(node.val, left_max, right_max)

        dfs(root)
        return self.res   
# @lc code=end

