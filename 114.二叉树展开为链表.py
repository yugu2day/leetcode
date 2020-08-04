#
# @lc app=leetcode.cn id=114 lang=python
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # 先处理左右节点，并得到左边最后一个点，连接右边节点


        if not root:
            return 
        
        self.flatten(root.left)
        self.flatten(root.right)
        
        if root.left:
            right = root.right
            root.right = root.left
            root.left = None
            tmp = root.right
            while tmp.right:
                tmp = tmp.right
            tmp.right = right
        



        
# @lc code=end

