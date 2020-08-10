#
# @lc app=leetcode.cn id=230 lang=python
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # 中序遍历， 计数
        cnt = 0
        stack = []
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                cnt += 1
                if cnt == k:
                    return node.val
                node = node.right
        return -1
        
# @lc code=end

