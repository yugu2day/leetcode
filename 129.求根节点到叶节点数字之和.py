#
# @lc app=leetcode.cn id=129 lang=python
#
# [129] 求根到叶子节点数字之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = [root]
        res = 0
        while queue:
            node = queue.pop(0)
            if not node.left and not node.right:
                res += node.val
            if node.left:
                node.left.val += node.val * 10
                queue.append(node.left)
            if node.right:
                node.right.val += node.val * 10
                queue.append(node.right)
        return res
# @lc code=end

