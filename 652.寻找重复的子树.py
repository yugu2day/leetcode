#
# @lc app=leetcode.cn id=652 lang=python
#
# [652] 寻找重复的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        self.c = dict()
        res = []
        def helper(node):
            if not node:
                return "#"
            serial = "{},{},{}".format(node.val, helper(node.left), helper(node.right))
            self.c[serial] = self.c.get(serial, 0 ) + 1
            if self.c[serial] == 2:
                res.append(node)
            return serial

        helper(root)
        return res

        
# @lc code=end

