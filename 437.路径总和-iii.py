#
# @lc app=leetcode.cn id=437 lang=python
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        # dfs遍历，记录路径可能的情况
        def dfs(node, path):
            if node is None:
                return 0
            path = [num + node.val for num in path] + [node.val]
            return path.count(sum) + dfs(node.left, path) + dfs(node.right, path)

        
        return dfs(root, [])

# @lc code=end

