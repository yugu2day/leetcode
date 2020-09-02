#
# @lc app=leetcode.cn id=538 lang=python
#
# [538] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        # 从右向左的先序
        stack = []
        node = root
        tmp = 0
        while stack or node:
            if node:
                stack.append(node)
                node = node.right
            else:
                node = stack.pop()
                node.val += tmp
                tmp = node.val
                node = node.left
        return root

# @lc code=end

