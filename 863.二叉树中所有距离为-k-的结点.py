#
# @lc app=leetcode.cn id=863 lang=python
#
# [863] 二叉树中所有距离为 K 的结点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        
        if K == 0:
            return [target.val]

        d = collections.defaultdict(list) # depth 和对应节点的关系
        
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.left:
                d[node.val].append(node.left.val)
                d[node.left.val].append(node.val)
                queue.append(node.left)
            if node.right:
                d[node.val].append(node.right.val)
                d[node.right.val].append(node.val)
                queue.append(node.right)
        # print d
        
        res = []
        def dfs(node, root, depth):
            for child in d[node]:
                if child == root:
                    continue
                dfs(child, node, depth+1)
                if depth == K:
                    res.append(child)
        dfs(target.val, -1, 1)

        return res
# @lc code=end

