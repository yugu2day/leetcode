#
# @lc app=leetcode.cn id=331 lang=python
#
# [331] 验证二叉树的前序序列化
#

# @lc code=start
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        # 用栈记录节点和当前叶子结点数，迭代更新栈顶节点并判断
        # preorder = preorder.split(',')
        # if len(preorder) == 0:
        #     return True
        # if len(preorder) == 1 and preorder[0] == '#':
        #     return True
        
        # stack = []
        # for idx, n in enumerate(preorder):
        #     if n != "#":
        #         stack.append([n, 0])
        #     else:
        #         if not stack:
        #             return False
        #         # 一个节点为空
        #         if stack[-1][1] == 0:
        #             stack[-1][1] = 1
        #         else: # 两个节点为空
        #             while stack and stack[-1][1] + 1 >= 2:
        #                 stack.pop()
        #             if stack:
        #                 stack[-1][1] += 1
        #             else:
        #                 if idx != len(preorder) - 1:
        #                     return False

        # return len(stack) == 0

        # 按可分配空间计算
        preorder = preorder.split(',')
        space = 1
        for n in preorder:
            space -= 1
            if space < 0:
                return False
            if n != "#":
                space += 2
        return space == 0
                        
# @lc code=end

