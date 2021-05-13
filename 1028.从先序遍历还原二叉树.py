#
# @lc app=leetcode.cn id=1028 lang=python
#
# [1028] 从先序遍历还原二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        root = self.get_first_node(S)
        S = S[len(str(root.val)):]
        if not S:
            return root

        stack = [(root, 0)] # 存放节点和对应的层数

        while S:
            if S.startswith('-'):
                depth = self.get_depth(S)
                S = S[depth:]
                continue
            
            node = self.get_first_node(S)
            S = S[len(str(node.val)):]
            
            while stack and stack[-1][1] >= depth:
                stack.pop()

            # 为父节点增加子节点，子节点入栈
            if stack[-1][0].left:
                stack[-1][0].right = node
            else:
                stack[-1][0].left = node
            stack.append((node, depth))
        return root

    def get_depth(self, S):
        depth = 0
        for i in range(0, len(S)):
            if S[i] != '-':
                break
            depth += 1
        return depth
    
    def get_first_node(self, S):
        num = 0
        for i in range(0, len(S)):
            if S[i] == '-':
                break
            num = num * 10 + int(S[i])
        return TreeNode(num)
# @lc code=end

