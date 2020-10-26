#
# @lc app=leetcode.cn id=589 lang=python
#
# [589] N叉树的前序遍历
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
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # 递归
        # if not root:
        #     return []
        # res = [root.val]
        # for child in root.children:
        #     res += self.preorder(child)
        # return res
        if not root:
            return []

        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(node.children[::-1])
        return res
# @lc code=end

