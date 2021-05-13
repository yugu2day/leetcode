#
# @lc app=leetcode.cn id=968 lang=python
#
# [968] 监控二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        leaf = 0
        monitor = 1
        others = 2
        self.res = 0

        def dfs(node):
            if not node:
                return -1
            left, right = dfs(node.left), dfs(node.right)
            if left == leaf or right == leaf:   # 左右节点均是叶子结点， 该节点为监控节点
                self.res += 1
                return monitor
            if left == monitor or right == monitor: # 左右节点存在监控节点， 该节点被监控
                return others
            return leaf # 左右节点既没有叶子结点也没有监控节点，该节点需要被上层节点监控
        
        if dfs(root) == leaf:
            self.res += 1
        return self.res
# @lc code=end

