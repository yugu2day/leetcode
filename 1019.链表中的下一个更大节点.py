#
# @lc app=leetcode.cn id=1019 lang=python
#
# [1019] 链表中的下一个更大节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        head = self.reverseList(head)
        res = []
        # 单调栈
        stack = []
        tmp = head

        while tmp:

            if stack and stack[-1] > tmp.val:
                res.append(stack[-1])
            else:
                while stack and stack[-1] <= tmp.val:
                    stack.pop()
                if stack:
                    res.append(stack[-1])

            if not stack:
                res.append(0)

            stack.append(tmp.val)
            tmp = tmp.next

        return res[::-1]


    def reverseList(self, head):
        cur = None
        pnode, nnode = head, head.next

        while nnode:
            t = nnode.next
            pnode.next = cur
            nnode.next = pnode
            cur = pnode
            pnode = nnode
            nnode = t
        return pnode
        
# @lc code=end

