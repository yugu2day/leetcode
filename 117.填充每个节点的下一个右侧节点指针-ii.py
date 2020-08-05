#
# @lc app=leetcode.cn id=117 lang=python
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # 层序遍历的思路，设置右侧节点指针
        if not root:
            return root
        queue = [root]

        while queue:
            layer = []
            while queue:
                node = queue.pop(0)
                if queue:
                    node.next = queue[0]
                else:
                    node.next = None
                if node.left:
                    layer.append(node.left)
                if node.right:
                    layer.append(node.right)
            queue = layer
        return root
# @lc code=end

