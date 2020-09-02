#
# @lc app=leetcode.cn id=449 lang=python
#
# [449] 序列化和反序列化二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        if not root:
            return ''
        queue = [root]

        while queue:
            node = queue.pop(0)
            if node is not None: 
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append(None)
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

