#
# @lc app=leetcode.cn id=637 lang=python
#
# [637] 二叉树的层平均值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        # 层序遍历
        queue = [root]
        res = []
        while queue:
            layer = []
            tmp = 0
            l = len(queue)
            while queue:
                node = queue.pop(0)
                tmp += node.val
                if node.left:
                    layer.append(node.left)
                if node.right:
                    layer.append(node.right)
            res.append(tmp*1.0 / l)
            tmp = 0
            queue = layer 
        return res
        
# @lc code=end

