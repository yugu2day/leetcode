#
# @lc app=leetcode.cn id=1110 lang=python
#
# [1110] 删点成林
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        def dfs(node):
            if not node:
                return None
            l = dfs(node.left)
            r = dfs(node.right)

            if node.val in self.to_delete:
                if l:
                    self.res.append(node.left)
                if r:
                    self.res.append(node.right)
                return None
            node.left = l
            node.right = r
            return node
        self.res = []
        self.to_delete = set(to_delete)
        if dfs(root) != None:
            self.res.append(root)
        return self.res
        
# @lc code=end

