#
# @lc app=leetcode.cn id=95 lang=python
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        #
        # 递归得到子数组的子树组合，分别和当前index进行匹配加入结果数组
        #
        if n == 0:
            return []

        import copy
        arr = [_ for _ in range(1, n+1)]

        def get_sub_tree(arr):
            if not arr:
                return [None]
            if len(arr) == 1:
                return [TreeNode(arr[0])]

            res = []
            for index in range(0, len(arr)):
                for left in get_sub_tree(arr[:index]):
                    for right in get_sub_tree(arr[index+1:]):

                        root = TreeNode(arr[index])
                        left = copy.deepcopy(left)
                        right = copy.deepcopy(right)
                        root.left = left
                        root.right = right
                        res.append(root)
            return res
        
        res = get_sub_tree(arr)
        return res
# @lc code=end

