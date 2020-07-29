#
# @lc app=leetcode.cn id=101 lang=python
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 中序遍历，看数组前后是否一致


        def helper(l, r):
            # 递归比较两个节点
            if not l and not r:
                return True
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            return helper(l.left, r.right) and helper(l.right, r.left)
            
            
        if not root:
            return True
        
        return helper(root.left, root.right)
        

        

        
# @lc code=end

