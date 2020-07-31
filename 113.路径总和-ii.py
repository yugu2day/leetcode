#
# @lc app=leetcode.cn id=113 lang=python
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        # 同112题，再加上记录路径
        if not root:
            return []

        res = []
        queue = [(root, root.val, [root.val])]
        while queue:
            tmp = []

            while queue:
                node, val, path = queue.pop(0)

                if node.left:
                    p = path[:]
                    p.append(node.left.val)
                    tmp.append((node.left, val+node.left.val, p))
                if node.right:
                    p = path[:]
                    p.append(node.right.val)
                    tmp.append((node.right, val+node.right.val, p))
                if not node.left and not node.right:
                    if val == sum:
                        res.append(path)
            queue = tmp
        return res

# @lc code=end

