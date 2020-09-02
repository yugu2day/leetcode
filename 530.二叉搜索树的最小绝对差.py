#
# @lc app=leetcode.cn id=530 lang=python
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 先序遍历， 取相邻节点差值的最小值

        stack = []
        node = root

        prev = None
        min_res = float('inf')
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if prev:
                    min_res = min(node.val - prev.val, min_res)
                prev = node
                node = node.right
        
        
        return min_res

                
# @lc code=end

