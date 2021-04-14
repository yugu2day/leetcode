#
# @lc app=leetcode.cn id=61 lang=python
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        # 倒数第k个节点变成第一个, 找到倒数k+1个节点
        k = k % self.get_len(head)
        if k == 0:
            return head

        slow, fast = head, head
        for i in range(k):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        res = slow.next
        fast.next = head
        slow.next = None
        return res
    

    def get_len(self, head):
        if not head:
            return 0
        return 1 + self.get_len(head.next)
# @lc code=end

