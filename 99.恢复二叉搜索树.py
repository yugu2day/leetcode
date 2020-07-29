#
# @lc app=leetcode.cn id=99 lang=python
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # 中序遍历， 找到第一个比后一个点大的点，和最后一个比前一个点小的点。
        # 两两交换

        dic = {}
        res = []

        stack = []
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                res.append(node.val)
                dic[node.val] = node
                node = node.right
        
        n1, n2 = None, None
        # 找到需要交换的两个点
        for i in range(0, len(res)):
            if i < len(res) - 1 and res[i] > res[i+1] and n1 is None:
                n1 = res[i]
            if i>0 and res[i] < res[i-1]:
                n2 = res[i]


        dic[n1].val, dic[n2].val = dic[n2].val, dic[n1].val
        return root


# @lc code=end

