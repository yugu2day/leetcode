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
        res = []
        queue = [root]
        while queue:
            next_queue = []
            row = []
            while queue:
                node = queue.pop(0)
                if not node:
                    continue 
                row.append(node.val)
                next_queue.append(node.left)
                next_queue.append(node.right)
            if row:
                res.append(row)
            queue = next_queue
        return res[::-1]
# @lc code=end

