#
# @lc app=leetcode.cn id=671 lang=python
#
# [671] 二叉树中第二小的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 中序有序
        res = set()
        stack = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                res.add(node.val)
                node = node.right
        if len(res) <= 1:
            return -1
        else:
            r = sorted(list(res))
            return r[1]

            
# @lc code=end

