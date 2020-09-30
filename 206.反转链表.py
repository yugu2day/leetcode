#
# @lc app=leetcode.cn id=206 lang=python
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def helper(node):
            if not node or not node.next:
                return node
            tail = helper(node.next)
            node.next.next = node
            node.next = None
            return tail
        
        return helper(head)

# @lc code=end

