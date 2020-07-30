#
# @lc app=leetcode.cn id=102 lang=python
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #
        # 广度优先搜索
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
        return res
# @lc code=end

