#
# @lc app=leetcode.cn id=105 lang=python
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # 前序第一个节点root为顶点， 中序到root为左边子树，root之后为右边子树

        if not preorder:
            return None
        
        root = TreeNode(preorder.pop(0))
        left_len = inorder.index(root.val)

        left_preorder = preorder[:left_len]
        left_inorder = inorder[:left_len]
        right_preorder = preorder[left_len:]
        right_inorder = inorder[left_len+1:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root

# @lc code=end

