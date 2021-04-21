#
# @lc app=leetcode.cn id=328 lang=python
#
# [328] 奇偶链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        l1 = head
        connect = head.next
        l2 = connect
        while l2 and l2.next:
            l1.next = l2.next
            l1 = l1.next
            l2.next = l1.next
            l2 = l2.next
        l1.next = connect
        return head

# @lc code=end

