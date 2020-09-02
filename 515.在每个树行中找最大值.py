#
# @lc app=leetcode.cn id=515 lang=python
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 层序遍历找最大值
        if not root:
            return []
        res = [root.val]
        queue = [root]
        while queue:
            tmp = []
            tmp_v = []
            while queue:
                node = queue.pop(0)
                if node.left:
                    tmp.append(node.left)
                    tmp_v.append(node.left.val)
                if node.right:
                    tmp.append(node.right)
                    tmp_v.append(node.right.val)
            queue = tmp
            if tmp_v:
                res.append(max(tmp_v))
        return res




# @lc code=end

