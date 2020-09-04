#
# @lc app=leetcode.cn id=653 lang=python
#
# [653] 两数之和 IV - 输入 BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.res = []
        def preorder(node):
            if not node:
                return 
            preorder(node.left)
            self.res.append(node.val)
            preorder(node.right)
        preorder(root)
        l, r = 0, len(self.res) - 1
        while l < r:
            if self.res[l] + self.res[r] == k:
                return True
            elif self.res[l] + self.res[r] < k:
                l += 1
            elif self.res[l] + self.res[r] > k:
                r -= 1
        return False



# @lc code=end

