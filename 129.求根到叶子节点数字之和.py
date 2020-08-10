#
# @lc app=leetcode.cn id=129 lang=python
#
# [129] 求根到叶子节点数字之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 层序遍历， 更新节点的值
        # 当该节点为叶子节点时， 加上其值
        if not root:
            return 0
            
        queue = [root]
        self.res = 0

        while queue:
            layer = []
            while queue:
                node = queue.pop(0)
                if node.left:
                    node.left.val += node.val * 10
                    layer.append(node.left)
                if node.right:
                    node.right.val += node.val * 10
                    layer.append(node.right)
                if not node.left and not node.right:
                    self.res += node.val
            queue = layer
        return self.res

# @lc code=end

