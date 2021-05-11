#
# @lc app=leetcode.cn id=872 lang=python
#
# [872] 叶子相似的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        # 先序取叶子
        n1, n2 = [], []
        self.helper(root1, n1)
        self.helper(root2, n2)
        return n1 == n2
    

    def helper(self, node, res):
        if not node:
            return
        if not node.left and not node.right:
            res.append(node.val)
            return
        if node.left:
            self.helper(node.left, res)
        if node.right:
            self.helper(node.right, res)
# @lc code=end

