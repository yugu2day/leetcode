#
# @lc app=leetcode.cn id=572 lang=python
#
# [572] 另一个树的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        # 递归遍历s, 节点值与t顶点相等时进行比较
        if not s and not t:
            return True
        if not s or not t:
            return False
        
        if s.val == t.val:
            if self.isSame(s, t):
                return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def isSame(self, t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        if t1.val != t2.val:
            return False
        return self.isSame(t1.left, t2.left) and self.isSame(t1.right, t2.right)

# @lc code=end

