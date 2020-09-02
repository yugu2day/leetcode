#
# @lc app=leetcode.cn id=513 lang=python
#
# [513] 找树左下角的值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 层序遍历
        queue = [root]
        while queue:
            tmp = []
            res = queue[0].val
            while queue:
                node = queue.pop(0)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            if not tmp:
                return res
            else:
                queue = tmp
        return 0
# @lc code=end

