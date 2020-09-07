#
# @lc app=leetcode.cn id=655 lang=python
#
# [655] 输出二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        # 1层 - 1
        # 2层 - 3   2 + 1
        # 3层 - 7   4 + 3
        # 4层 - 15  8 + 7
        # n层       pow(2, n-1) + f(n-1)
        if not root:
            return []
        d = self.getDepth(root)
        l = self.getLen(d)
        self.res = [[""]*l for _ in range(d)]

        self.fill(root, 0, l-1, 1)
        return self.res


    def fill(self, node, l, r, d):
        # 根据长度生成每层的位置
        if not node:
            return
        idx = (l + r) // 2
        self.res[d-1][idx] = str(node.val)
        self.fill(node.left, l, idx - 1, d+1)
        self.fill(node.right, idx+1, r, d+1)


    def getLen(self, d):
        # 根据层数获取每层的长度
        if d <= 1:
            return d
        l = pow(2, d-1) + self.getLen(d-1)
        return l
    
    def getDepth(self, root):
        # 获取二叉树层数
        if not root:
            return 0

        return max(self.getDepth(root.left), self.getDepth(root.right)) + 1
# @lc code=end

