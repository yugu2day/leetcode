#
# @lc app=leetcode.cn id=508 lang=python
#
# [508] 出现次数最多的子树元素和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        # 递归计数
        self.dic = {}
        res = []

        def helper(node):
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            self.dic[node.val + left + right] = self.dic.get(node.val + left + right, 0) + 1
            return node.val + left + right
        
        helper(root)
        max_cnt = max(self.dic.values())
        for k, v in self.dic.items():
            if v == max_cnt:
                res.append(k)
        return res
        
# @lc code=end

