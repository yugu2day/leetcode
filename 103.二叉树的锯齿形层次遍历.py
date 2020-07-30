#
# @lc app=leetcode.cn id=103 lang=python
#
# [103] 二叉树的锯齿形层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 同102题层序遍历，增加一个flag标识方向
        if not root:
            return []
        queue = [root]
        res = []
        flag = True
        while queue:
            tmp = []
            layer = []
            while queue:
                node = queue.pop(0)
                layer.append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            if flag:
                res.append(layer)
            else:
                res.append(layer[::-1])
            flag = True if not flag else False
            queue = tmp
        return res
# @lc code=end

