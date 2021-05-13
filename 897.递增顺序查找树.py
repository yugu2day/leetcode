#
# @lc app=leetcode.cn id=897 lang=python
#
# [897] 递增顺序查找树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        
        head, _ = self.getHeaderAndTail(root)
        return head
    
    def getHeaderAndTail(self, node):
        if not node:
            return node, node
        leftH, leftT = self.getHeaderAndTail(node.left)
        if leftT:
            leftT.right = node
            node.left = None
        rightH, rightT = self.getHeaderAndTail(node.right)

        node.right = rightH
        if not leftH:
            leftH = node
        if not rightT:
            rightT = node
        return (leftH, rightT)
        
# @lc code=end

