#
# @lc app=leetcode.cn id=606 lang=python
#
# [606] 根据二叉树创建字符串
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        # 递归获取字符串，如果右子树不在就不递归
        if not t:
            return ""
        res = "{}".format(t.val)
        if not t.left and not t.right:
            return "{}".format(t.val)
        res += "({})".format(self.tree2str(t.left))
        if t.right:
            res += "({})".format(self.tree2str(t.right))
        return res
# @lc code=end

