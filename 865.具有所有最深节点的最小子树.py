#
# @lc app=leetcode.cn id=865 lang=python
#
# [865] 具有所有最深节点的最小子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def depth(node):
            if not node:
                return 0
            return 1 + max(depth(node.left), depth(node.right))


        # 得到左右节点的最深，如果左右深度相同，返回当前节点，否则按更深的子节点递归
        if not root:
            return None
        
        l = depth(root.left)
        r = depth(root.right)

        if l == r:
            return root
        if l > r:
            return self.lcaDeepestLeaves(root.left)
        else:
            return self.lcaDeepestLeaves(root.right)
    
# @lc code=end

