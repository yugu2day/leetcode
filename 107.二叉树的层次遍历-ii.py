#
# @lc app=leetcode.cn id=107 lang=python
#
# [107] 二叉树的层次遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 层次遍历， 反置数组
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            tmp = []
            layer = []
            while queue:
                node = queue.pop(0)
                layer.append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            res.append(layer)
            queue = tmp
        return res[::-1]
# @lc code=end

