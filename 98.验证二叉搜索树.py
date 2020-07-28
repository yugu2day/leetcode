#
# @lc app=leetcode.cn id=98 lang=python
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 中序遍历， 结果是否有序判断是否二叉搜索树
        res = []
        stack = []
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                res.append(node.val)
                node = node.right
        return sorted(res) == res and len(res) == len(set(res))

# @lc code=end

