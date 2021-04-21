#
# @lc app=leetcode.cn id=92 lang=python
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if left == right:
            return head

        tmp = ListNode(0)
        tmp.next = head
        res = tmp


        for i in range(0, left-1):
            tmp = tmp.next

        l, r = self.reverseK(tmp.next, right-left+1)

        tail = tmp.next
        tmp.next = l
        tail.next = r

        return res.next
    
    def reverseK(self, node, K):
        if not node or K <= 1:
            return node, node.next
        head, tail = self.reverseK(node.next, K-1)
        node.next.next = node
        node.next = None
        return head, tail
# @lc code=end

