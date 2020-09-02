#
# @lc app=leetcode.cn id=450 lang=python
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
        
    def next(self, root):
        """
        One step right and then always left
        """
        root = root.right
        while root.left:
            root = root.left
        return root.val
    
    def prev(self, root):
        """
        One step left and then always right
        """
        root = root.left
        while root.right:
            root = root.right
        return root.val
        
    def deleteNode(self, root, key):
        # 当前节点与左子树最大的节点互换，或者与右子树最小的节点互换
        if not root:
            return None
        

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        else:

            if not (root.left or root.right):
                root = None

            elif root.right:
                root.val = self.next(root)
                root.right = self.deleteNode(root.right, root.val)
  
            else:
                root.val = self.prev(root)
                root.left = self.deleteNode(root.left, root.val)
                        
        return root


        
# @lc code=end

