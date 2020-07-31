#
# @lc app=leetcode.cn id=112 lang=python
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # 层序遍历， 获取从根节点到叶子结点的和
        if not root:
            return False
        queue = [(root, root.val)]

        while queue:
            tmp = []
            while queue:
                node, val = queue.pop(0)
                if node.left:
                    tmp.append((node.left, node.left.val + val))
                if node.right:
                    tmp.append((node.right, node.right.val + val))
                if not node.left and not node.right:
                    if val == sum:
                        return True
            queue = tmp
        return False
# @lc code=end

