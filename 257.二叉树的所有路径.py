#
# @lc app=leetcode.cn id=257 lang=python
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # 层序遍历， 记录路径
        if not root:
            return []

        queue = [(root, [str(root.val)])]
        res = []
        while queue:
            layer = []
            while queue:
                node, path = queue.pop(0)
                if node.left:
                    layer.append((node.left, path[:] + [str(node.left.val)]))
                
                if node.right:
                    layer.append((node.right, path[:] + [str(node.right.val)]))
                if not node.left and not node.right:
                    res.append("->".join(path))
            queue = layer
        return res


# @lc code=end

