#
# @lc app=leetcode.cn id=106 lang=python
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # 后序遍历数组最后一个节点为当前root节点
        # 中序遍历查找root节点，root节点左边为左子树，右边为右子树
        if not inorder:
            return None
        root = TreeNode(postorder.pop())
        left_len = inorder.index(root.val)

        left_inorder = inorder[:left_len]
        left_postorder = postorder[:left_len]

        right_inorder = inorder[left_len+1:]
        right_postorder = postorder[left_len:]

        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)

        return root

# @lc code=end

