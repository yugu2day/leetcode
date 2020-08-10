#
# @lc app=leetcode.cn id=199 lang=python
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 层序遍历， 记录最后一个值
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            layer = []
            while queue:
                node = queue.pop(0)
                if not queue:
                    res.append(node.val)
                if node.left:
                    layer.append(node.left)
                if node.right:
                    layer.append(node.right)
            queue = layer
        return res
# @lc code=end

