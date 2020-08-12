#
# @lc app=leetcode.cn id=297 lang=python
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # 层序遍历， 记录空值

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        res = []
        queue = [root]
        while queue:
            layer = []
            tmp = []
            while queue:
                node = queue.pop(0)
                if node:
                    layer.append(node.left)
                    layer.append(node.right)
                res.append(node.val if node else None)
            if set(layer) == {None}:
                break
            queue = layer
        return str(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = eval(data)
        root = TreeNode(data.pop(0))
        queue = [root]
        
        while data:
            layer = []
            while queue:
                node = queue.pop(0)
                if node:
                    val = data.pop(0)
                    if val != None:
                        node.left = TreeNode(val)
                        layer.append(node.left)
                    val = data.pop(0)
                    if val != None:
                        node.right = TreeNode(val)
                        layer.append(node.right)
            queue = layer
        
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

