#
# @lc app=leetcode.cn id=559 lang=python
#
# [559] N叉树的最大深度
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        if not root.children:
            return 1

        max_d = float('-inf')
        for child in root.children:
            d = self.maxDepth(child) + 1
            max_d = max(max_d, d)
        return max_d
        

        
# @lc code=end

