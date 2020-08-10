#
# @lc app=leetcode.cn id=145 lang=python
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 递归
        # res = []
        # if not root:
        #     return []
        # res += self.postorderTraversal(root.left)
        # res += self.postorderTraversal(root.right)
        # res.append(root.val)
        # return res

        # 非递归
        if not root:
            return []
        self.res = []
        node = root
        stack = []
        while node or stack:
            if node:
                self.res.append(node.val)
                stack.append(node)
                node = node.right
            else:
                node = stack.pop()
                node = node.left
        return self.res[::-1]
                

# @lc code=end

