#
# @lc app=leetcode.cn id=86 lang=python
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        r1, r2 = ListNode(0), ListNode(1)
        l1, l2 = r1, r2

        tmp = head
        while tmp:
            if tmp.val < x:
                l1.next = tmp
                l1 = l1.next
            else:
                l2.next = tmp
                l2 = l2.next
            tmp = tmp.next
        
        l1.next = r2.next
        l2.next = None
        return r1.next
# @lc code=end

