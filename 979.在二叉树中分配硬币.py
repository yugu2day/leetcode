#
# @lc app=leetcode.cn id=979 lang=python
#
# [979] 在二叉树中分配硬币
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        def helper(node):
            if not node:
                return 0
            # 计算左右子树的和，确定需要转移的金币
            l = helper(node.left)
            r = helper(node.right)
            self.res += abs(l) + abs(r)
            return l + r + node.val - 1
        helper(root)
        return self.res
# @lc code=end

