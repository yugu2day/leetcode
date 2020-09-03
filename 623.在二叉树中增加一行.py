#
# @lc app=leetcode.cn id=623 lang=python
#
# [623] 在二叉树中增加一行
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        # 层序遍历 + 点的插入
        queue = [root]
        cur = 1
        while queue:
            layer = []
            while queue:
                node = queue.pop(0)
                if cur + 1 == d:
                    self.insert(node, v)
                if node.left:
                    layer.append(node.left)
                if node.right:
                    layer.append(node.right)

            queue = layer
            cur += 1

        return root


    def insert(self, node, v):
        if node.left:
            tmp = node.left
            node.left = TreeNode(v)
            node.left.left = tmp
        else:
            node.left = TreeNode(v)
        
        if node.right:
            tmp = node.right
            node.right = TreeNode(v)
            node.right.right = tmp
        else:
            node.right = TreeNode(v)
        

        
# @lc code=end

