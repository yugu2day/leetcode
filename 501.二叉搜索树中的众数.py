#
# @lc app=leetcode.cn id=501 lang=python
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def __init__(self):
        self.max_counter = 0
        self.pre = float("-inf")
        self.counter = 0
        self.res = []


    def findMode(self, root):
        def dfs(root):
            if not root:
                return 
            dfs(root.left)

            # 计算count
            if root.val == self.pre:    
                self.counter += 1
            else:
                self.counter = 0
            self.pre = root.val
            # count与最大cnt进行比较
            if self.counter > self.max_counter: 
                self.max_counter = self.counter
                self.res = [root.val]
            elif self.counter == self.max_counter:
                self.res.append(root.val)

            dfs(root.right)

        dfs(root)
        return self.res

        


        
# @lc code=end

