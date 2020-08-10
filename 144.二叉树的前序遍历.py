#
# @lc app=leetcode.cn id=144 lang=python
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 递归

        # if not root:
        #     return []
        # self.res = []
        # self.res.append(root.val)
        # self.res += self.preorderTraversal(root.left)
        # self.res += self.preorderTraversal(root.right)
        # return self.res

        # 非递归，使用栈
        if not root:
            return []
        self.res = []
        node = root
        stack = []
        while node or stack:
            if node:
                self.res.append(node.val)
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                node = node.right
        return self.res
                

# @lc code=end

