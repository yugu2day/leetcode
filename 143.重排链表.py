#
# @lc app=leetcode.cn id=143 lang=python
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        t = mid.next
        mid.next = None
        tail = self.reverse(t)
        tmp = head
        while tail:
            t = tmp.next
            tmp.next = tail
            tail = tail.next

            tmp = tmp.next
            tmp.next = t
            tmp = tmp.next

        return head
        
    
    def reverse(self, node):
        
        if not node or not node.next:
            return node

        cur = None
        p, n = node, node.next

        while n:
            t = n.next
            p.next = cur
            n.next = p
            cur = p
            p = n
            n = t
        return p

# @lc code=end

