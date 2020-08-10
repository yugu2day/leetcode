#
# @lc app=leetcode.cn id=173 lang=python
#
# [173] 二叉搜索树迭代器
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    # 中序得到有序数组，遍历

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.t = self.inorder(root)
        self.i = 0

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        r = self.t[self.i]
        self.i += 1
        return r

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.i < len(self.t) 

    def inorder(self, node):
        if not node:
            return []
        res = []
        res += self.inorder(node.left)
        res.append(node.val)
        res += self.inorder(node.right)
        return res


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

